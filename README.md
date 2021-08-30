# Back-End-Portifolio

```
Como realizar o Run Server em sua Maquina Local e deixar o programa pronto para o desenvolvimento.
```

Roteiro para rodar o Programa em Maquina Local usando Ubuntu.

Este programa devera obrigatoriamente usar:

-> python3.8.10 com todas as libs de desenvolvimento pre instaladas.

-> sqlite3

Primeiro Passo - O Repositorio.

Clonar o repositorio:

1-git clone https://github.com/mlobf/Back-End-Portifolio.git

No caso de algum imprevisto, o repositorio tambem estara disponivel via google drive com o endereço compartilhado por email para marcoslemeborbafilho@gmai.com. Qual problema basta me mandar um email.

Proximo Passo - venv

Paralelo ao diretorio clonado, cria um ambiente virtual Python3.8.10 via terminal:

1-Python3.8.10 -m venv myvenv

Ative o respectivo ambiente via terminal:

2-source myvenv/bin/activate

Instale as dependencias contidas no arquivo requirements.txt no ambiente virtual criado via terminal:

3-pip3.8 install -r /requirements.txt

Proximo Passo - Criando Super Usuario.

1- Digite na CLI: python manage.py createsuperuser.

2 - Preencha todos os campos solicitados.

Proximo Passo - realizando as migrações no Banco de Dados.

1-Dentro da pasta "./Back-End-Portifolio/backend_portifolio/" digite no terminal: python manage.py makemigrations

2- Depois ....: python manage.py migrate.

Proximo Passo - rodando o app no servidor local.

1-Dentro da pasta "./Back-End-Portifolio/backend_portifolio/" digite no terminal: python manage.py runserver

2- Entre com seu navegador na Url gerada no terminal e nela complemente o endereço com "/list-all-xls/".

Proximo Passo - abrindo a tela de administração do Django.

1- Loging como super usuario no seguinte endereço:  "/admin/".
