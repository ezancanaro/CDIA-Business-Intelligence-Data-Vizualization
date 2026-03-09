📊 Business Intelligence e Data Visualization
Bem-vindo ao repositório oficial da disciplina de BI e Data Visualization do Bacharelado em Ciência de Dados e Inteligência Artificial.

Este repositório contém todo o material prático, códigos de exemplo, datasets e roteiros de exercícios que utilizaremos ao longo do semestre.

📂 Estrutura do Repositório
Para garantir que todos possamos trabalhar sem conflitos de código, o repositório está organizado da seguinte forma:

/conteudo: Slides, PDFs e materiais teóricos. (Conteúdo do Professor)

/exemplos: Notebooks (.ipynb) e scripts demonstrados em aula. (Conteúdo do Professor)

/dados: Datasets brutos (csv, json, sqlite) utilizados nos exemplos. (Conteúdo do Professor)

/entregas: Esta é a sua área de trabalho. É aqui que você deve criar as pastas para seus exercícios e trabalhos (ex: /entregas/lab01, /entregas/trabalho_final).

⚠️ Importante: Evite alterar arquivos nas pastas /conteudo, /exemplos ou /dados. Se quiser modificar um exemplo do professor, copie o arquivo para a sua pasta em /entregas antes de editar. Isso evitará conflitos quando você atualizar seu repositório.

🛠️ Guia de Configuração (Workflow)
Nesta disciplina, utilizaremos o fluxo de Forks. Você terá uma cópia deste repositório na sua conta, onde publicará suas resoluções.

1. Criar o Fork
No canto superior direito desta página, clique no botão Fork. Isso criará uma cópia exata deste repositório na sua conta do GitHub.

2. Clonar o seu Repositório
No seu terminal, clone o repositório que você acabou de criar (substitua SEU_USUARIO pelo seu user do GitHub):

Bash

git clone https://github.com/SEU_USUARIO/nome-da-disciplina.git
cd nome-da-disciplina
3. Configurar o "Upstream" (O Repositório do Professor)
Para receber atualizações (novas aulas, dados, correções), você precisa conectar seu repositório local ao repositório oficial da disciplina. Execute o comando abaixo:

Bash

# Adiciona o repositório oficial como uma fonte remota chamada 'upstream'
git remote add upstream https://github.com/PROFESSOR/nome-da-disciplina.git

# Verifica se deu certo (deve aparecer origin e upstream)
git remote -v
🔄 Como manter seu repositório atualizado
Sempre que um novo material for disponibilizado pelo professor, siga os passos abaixo para atualizar seu código local:

Baixe as atualizações do professor:

Bash

git fetch upstream
Mescle as atualizações no seu código: Certifique-se de estar na branch main (ou master) e faça o merge:

Bash

git checkout main
git merge upstream/main
Envie para o seu GitHub: Agora que seu computador local está atualizado, suba as alterações para o seu fork:

Bash

git push origin main
🐍 Ambiente de Desenvolvimento
Recomenda-se o uso de ambientes virtuais para evitar conflitos de bibliotecas.

Instalação das dependências
Um arquivo requirements.txt está disponível na raiz.

Bash

# Criação do ambiente virtual (exemplo com venv)
python -m venv .venv

# Ativação (Windows)
.venv\Scripts\activate

# Ativação (Linux/Mac)
source .venv/bin/activate

# Instalação dos pacotes
pip install -r requirements.txt
Principais Bibliotecas Utilizadas
Manipulação: pandas, numpy

Visualização: matplotlib, seaborn, plotly

ETL/Web: requests, beautifulsoup4, sqlalchemy

📝 Avaliações e Entregas
As entregas dos trabalhos (Trabalho 1 e Trabalho 2) deverão ser feitas via Commit no seu repositório pessoal (o Fork). O link do repositório deverá ser enviado na plataforma oficial da instituição na data estipulada.

Boas práticas de entrega:

Mantenha seus notebooks organizados e comentados.

Certifique-se de que os gráficos estão renderizando corretamente antes de subir.

Inclua um breve arquivo README.md dentro da pasta de cada projeto explicando o que foi feito.

Bom semestre a todos! 🚀