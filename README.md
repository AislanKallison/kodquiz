🚀 KodQuiz - Quiz de Python
O KodQuiz é uma aplicação web interativa desenvolvida com o framework Flask. O objetivo é oferecer um ambiente divertido e visualmente atraente para que alunos de 13 a 17 anos testem seus conhecimentos em lógica de programação e sintaxe Python.

Este projeto foi desenvolvido como parte do processo seletivo para a vaga de Professor na Kodland.

🛠️ Tecnologias Utilizadas
Backend: Python 3.x e Flask.

Frontend: HTML5, CSS3 (Customizado) e Bootstrap 5.

Template Engine: Jinja2 (Herança de templates e blocos).

Arquitetura: Estrutura de pastas padronizada para aplicações Flask (Static/Templates).

📁 Estrutura do Projeto
Plaintext
KODQUIZ/
├── static/              # Arquivos estáticos (CSS e Imagens)
│   ├── imagens/         # Assets visuais (Logos e Backgrounds)
│   └── styles.css       # Estilização global da aplicação
├── templates/           # Páginas HTML (Templates Jinja2)
│   ├── base.html        # Estrutura base e Navbar
│   ├── index.html       # Página inicial com fundo customizado
│   ├── quiz.html        # Interface das perguntas
│   └── results.html     # Exibição da pontuação final
├── app.py               # Lógica principal do servidor Flask
└── requirements.txt     # Dependências do projeto
🚀 Como Executar o Projeto
Clone o repositório:

Bash
git clone https://github.com/seu-usuario/kodquiz.git
cd kodquiz
Crie um ambiente virtual (Recomendado):

Bash
python -m venv .venv
# No Windows:
.venv\Scripts\activate
Instale as dependências:

Bash
pip install -r requirements.txt
Inicie o servidor:

Bash
python app.py
O site estará disponível em http://127.0.0.1:5000.

✨ Funcionalidades Principais
Interface Responsiva: Navbar personalizada com a identidade visual da Kodland.

Identidade Visual: Fundo dinâmico (the new digital WONDERLAND) aplicado via CSS diretamente no template.

Lógica de Quiz: Processamento de respostas e cálculo de pontuação no backend.

Navegação Fluida: Sistema de herança de templates para manutenção facilitada do código.
