import pandas as pd
import matplotlib.pyplot as plt
import unicodedata

def converte_numerico(df:pd.DataFrame, col:str):
    df[col] = df[col].str.replace(',','.')
    df[col] = pd.to_numeric(df[col]) #Converter para numérico
    return df

#Documentação https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
data = pd.read_csv("EmendasParlamentares.csv",encoding="iso-8859-1",sep=';')
#Formatação dos floats
data.style.format({"floats": "{:,.2f}"})

# 1) Qual o valor total pago em emendas por ano? 
data = converte_numerico(data, 'Valor Pago')

pagos_ano = data.groupby('Ano da Emenda')['Valor Pago'].sum()

# 2) Qual é a média e o desvio padrão dos valores empenhados por região do Brasil?
data = converte_numerico(data, 'Valor Empenhado')

por_regiao = data.groupby('Região')['Valor Empenhado'].agg('mean','std')

# 3. Quais são os 10 autores que mais destinaram recursos (valor empenhado) na história do dataset?
por_autor = data.groupby('Nome do Autor da Emenda')['Valor Empenhado'].sum()

top_10 = por_autor.sort_values(ascending=False).head(10) #Ordeno decrescente 

# 4. Quantas emendas foram destinadas para o estado de Santa Catarina?
data['UF'] = data['UF'].str.upper()
print(data['UF'].unique())
emendas_sc = data[data['UF']=='SANTA CATARINA']
print(emendas_sc['UF'].count())
# Res: 2948

#5. Destas emendas, quais municípios se destacam no recebimento dos recursos por tipo?
print(emendas_sc['Tipo de Emenda'].unique())
ordenado = emendas_sc.sort_values(['Tipo de Emenda','Valor Empenhado'],ascending=False)
mun_identificados = ordenado[ordenado['Município']!='Sem informação']
mun_identificados = mun_identificados[ordenado['Município']!='Múltiplo']
#Lista de munícipios que mais receberam emendas
destaques = ordenado.groupby('Tipo de Emenda').head(2)[['Município','Tipo de Emenda', 'Valor Empenhado']]
#Lista ignorando emendas não identificadas ou para múltiplos municípios
destaques_identificados = mun_identificados.groupby('Tipo de Emenda').head(2)[['Município','Tipo de Emenda', 'Valor Empenhado']]

#6. Existem emendas onde o valor liquidado é significativamente diferente do valor pago? 
#'Valor Liquidado', 'Valor Pago'
data = converte_numerico(data, 'Valor Liquidado')
# Pagamento é feito após a liquidação. Importante saber se foi pago a mais do que liquidado
data['DiffLiqPago'] =data['Valor Pago'] - data['Valor Liquidado']  
data['DiffLiqPago_abs'] = data['DiffLiqPago'].abs() # Valor absoluto p comparação geral  
data['Percentual_diff'] = (data['Valor Pago'] / data['Valor Liquidado']) * 100

# Assumindo margem de 5000 como significativamente distinto. Outras métricas mais robustas existem
margem = 5000
significativos = data[data['DiffLiqPago'] > margem]
print(significativos[['Valor Liquidado','Valor Pago','DiffLiqPago']])
# Podemos tratar também pelo percentual > 5%, por exemplo:
significativos = data[((data['Percentual_diff'] > 105) | (data['Percentual_diff'] < 95)) & data['Valor Pago']!=0]
print(significativos[['Valor Liquidado','Valor Pago','Percentual_diff']].sort_values(['Percentual_diff']))
# Os casos mais absurdos (com a maior divergência) estarão ao fim do dataset
significativos[['Valor Liquidado','Valor Pago','Percentual_diff']].sort_values(['Percentual_diff']).tail(10)

#7. Qual o percentual de recursos que ficaram como "Restos a Pagar Cancelados" em relação ao total empenhado por ano? 
data = converte_numerico(data, 'Valor Restos A Pagar Cancelados')

por_ano = data.groupby('Ano da Emenda')
total_cancelado = por_ano['Valor Restos A Pagar Cancelados'].sum()
total_empenhado = por_ano['Valor Empenhado'].sum()
porcentagem = total_cancelado / total_empenhado * 100
print('Porcentagem:\n', porcentagem)

#8. Qual é a Subfunção mais comum para cada Região do país? 
por_regiao = data.groupby(['Região'])
#A moda é o valor que aparece mais vezes 
moda = por_regiao['Nome Subfunção'].agg(pd.Series.mode)

#9. Existem linhas com Cdigo Municpio IBGE ausente? Como isso afeta a análise por localidade? 
data[data['Código Município IBGE'].isna()] #O resutaldo é um df vazio, portanto, não existem

#10. O campo Município possui nomes duplicados com grafias diferentes (ex: acentuação)? 
municipios = data['Município'].unique()

def normalizacao_unicode(nome:str):
    if pd.isna(nome): return nome
    # Normaliza para a forma NFKD https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
    nfkd_form = unicodedata.normalize('NFKD', str(nome))
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)]).lower().strip()

df_comparacao = pd.DataFrame({'Original': municipios})
df_comparacao['Normalizado'] = df_comparacao['Original'].apply(normalizacao_unicode)

# 4. Agrupar por nomes normalizados e contar quantas variações originais existem
duplicados = df_comparacao.groupby('Normalizado')['Original'].unique()
grafias_diferentes = duplicados[duplicados.apply(len) > 1]

print("Municípios com nomes diferentes:\n", grafias_diferentes)