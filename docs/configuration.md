<h1>CONFIGURAÇÃO DE AMBIENTE VIRTUAL</h1>

Um ambiente virtual é um conjunto de diretórios que isolam versões do Python e de bibliotecas de forma local, separando-as das versões globais que acompanham o sistema operacional.
Essa abordagem permite que o desenvolvedor possa trabalhar em multiplos projetos ao mesmo tempo sem ter de se preocupar com a compatibilidade dos seus arquivos, tanto com o Python quanto com suas bibliotecas.

A seguir, faremos uma demonstração da criação de um virtualenv.

<h2>1) INSTALANDO O VIRTUALENV</h2>
Após a instalação inicial do Python, para instalar o virtualenv, abra um Terminal ou Prompt de Comando ou PowerShell e digite:

```shell-session
pip install virtualenv
```

Esse comando instala o pacote do virtualenv dentro da sua instalação do Python usando o pip, que é o pacote de instalações padrão do Python.

<h2>2) CRIANDO UM AMBIENTE VIRTUAL</h2>
Para criar um novo ambiente virtual basta, dentro da pasta do projeto, digitar o seguinte comando:

```shell-session
virtualenv -p 3.8 .virtualenv
```
Esse comando criará um ambiente chamado ```.virtualenv``` com a versão 3.8 do Python, específicada pelo parametro ```-p```

<h2>3) ACESSANDO O AMBIENTE VIRTUAL</h2>
Para acessar o novo ambiente virtual, esteja na pasta do projeto e digite:

<h3>3.1) Linux e Mac</h3>

```shell-session
source .virtualenv/bin/activate
```

<h3>3.2) Windows</h3>

```shell-session
.virtualenv/Scripts/activate
```

<h2>4) INSTALANDO PACOTES</h2>
Para instalar um pacote dentro do seu ambiente virtual, você primeiro precisará estar dentro do ambiente virtual (ver passo 3) e então digitar o seguinte comando:

```shell-session
pip install nome_do_pacote
```
De forma opcional você pode especificar a versão que deseja baixar do pacote:

```shell-session
pip install 'nome_do_pacote==1.4'
```

Além disso, é comum em projetos maiores, existir o arquivo chamado ```requirements.txt``` que agrega todas os pacotes utilizados em um projeto, para instalar os pacotes direto de um arquivo de requerimentos basta usar o seguinte comando:

```shell-session
pip install -r requirements.txt
```

Caso você esteja construindo um projeto do zero e deseje criar o arquivo de requerimentos, basta usar o seguinte comando:

```shell-session
pip freeze > requirements.txt
```

Para se aprofundar mais no assunto de pacotes e ambientes virtuais, recomendamos ler a documentação sobre [pip](https://pip.pypa.io/en/stable/) e [virtualenv](https://virtualenv.pypa.io/en/latest/).
