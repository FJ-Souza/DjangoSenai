<h1 align="center">
  <br>
  <a href="#"><img src="https://narmament.com/src/imagem/logo.png" alt="Nascimento" width="200"></a>
  <br>
  Nascimento
  <br>
</h1>

## Descrição:
<p>Nesse repositorio iremos realizar um passo a passo de criação de uma aplicação em django, para ficar de base para consulta dos alunos. Todos procedimentos de configurações será realizados e documentado para auxilio do desenvolvimento individual de cada um dos alunos no programa Trilhas de Futuro.</p>

# Passo a Passo

## Pré-requisitos:
-Instalação do Mysql: [Mysql](https://dev.mysql.com/downloads/installer/)<br>
-Instalação do Python: [Python](https://www.python.org/downloads/)<br>
-Instalação do Workbeanch: [WorkBeanch](https://dev.mysql.com/downloads/workbench/)<br>
-Instalação do VSCode: [VSCode](https://code.visualstudio.com/download)<br>

## 0- Criação de VENV e instalação do Django:
<b>0.0-</b> Código para criar a VENV "python -m venv 'nome_do_ambiente_virtual': "
```bash
python3 -m venv igor
```
<b>0.1-</b> Ativando a VENV windows "nome_da_venv\Scripts\activate":
```bash
 C:\python\Django> .\igor\Script\activate 
```
<b>0.2-</b> Verificando se a VENV está ativa pelo <b>VSCode</b>:<br>
    - Caso a sua Venv esteja ativa você vai verificar um nome dela na frete do caminho da pasta igual a imagem abaixo. 
    <br><br>
![venv](https://github.com/IMNascimento/DjangoSenai/assets/28989407/424b222b-40ea-48b6-8568-ff43cf9e99d7)
<br><br>
**0.3-** Instalando o Django:
```bash
 (igor)C:\python\Django> pip install django
```
**0.4-** Iniciando um projeto Django com o comando "django-admin startproject 'nome_do_projeto'":
```bash
 (igor)C:\python\Django> django-admin startproject trilhas
```
## 1- Servidor Django:
Após iniciar um projeto Django devemos inicializar um servidor para testarmos nossa aplicação, para isso iremos fazer os seguintes passos.<br><br>
**1.0-** Iniciar um servidor "python manage.py runserver":
```bash
(igor)C:\python\Django> cd trilhas
(igor)C:\python\Django\trilhas> python manage.py runserver
```
**1.1-** Verifique se o servidor funcionou normalmente acessando o endereço "127.0.0.1:8000":<br>
    - Caso tenha funcionado corretamente ele irá aparecer a imagem abaixo.<br><br>
![dajngo](https://github.com/IMNascimento/DjangoSenai/assets/28989407/888d6c30-7939-4085-a02f-e6f6df3938a3)
<br>
    - Caso queira trocar de porta ou ip de acesso inicie com o código "python manage.py runserver 0.0.0.0:0000" no lugares do zero você vai passar o ip e a porta.<br>
    - Agora podemos criar varios aplicativos dentro do nosso projeto.<br><br>
**1.2-** Criando um aplicativo "python manage.py startapp nome_do_aplicativo":
```bash
(igor)C:\python\Django\trilhas> python manage.py startapp siteTrilhas
```
## 2- Registrando App no Django:
**2.0-** Para verificar o nome do app criado você vai na pasta do app no arquivo app.py, vamos demonstrar com a foto abaixo:
![app](https://github.com/IMNascimento/DjangoSenai/assets/28989407/b64f64ae-4e7e-47b1-8316-73c4501809cb)<br>
-Como podemos verificar na foto temos em vermelho o sistema de diretorio até o arquivo e destacado de verde temos o nome do nosso app.<br>
**2.1-** Agora vamos registrar esse app vamos na pasta do nosso projeto e encontraremos o arquivo "settings.py" nele iremos inserir o nome da nossa aplicação como iremos verificar na foto a seguir:
![registro](https://github.com/IMNascimento/DjangoSenai/assets/28989407/25de48b3-2f5d-433a-8895-07ba60582974)
<br>
-Deixamos novamente com a cor vermelho o sistema de diretorio até o arquivo e marcado de verde a linha com nome que seria inserido.<br>
- Agora que nossa aplicação já foi cadastrada podemos testar se ela irá funcionar corretamente. Para isso precisaremos criar urls para o carregamento externo de nossa página. Veremos essa criação na próxima etapa.

## 3- Criando Url no App Django:
**3.0-** Criação de um arquivo urls.py dentro do seu app que no nosso caso chama "siteTrilhas":
![url](https://github.com/IMNascimento/DjangoSenai/assets/28989407/1b3bf2eb-b78c-4c4b-8693-254a718bdb19)<br>
**3.1-** Quando criarmos esse arquivo url o editor irá informa que não existe o método para isso iremos criar ele em seguida.
![view](https://github.com/IMNascimento/DjangoSenai/assets/28989407/eb553e1c-4356-4980-800d-ad52bb5fd3d6)<br>
**3.2-** Como vimos na imagem acima criamos uma view para exibir um texto "Olá mundo." na nossa página web. Por último Precisamos registrar nossas rotas. <br>
![rotas](https://github.com/IMNascimento/DjangoSenai/assets/28989407/0b5da0d5-b9f2-431c-8e8a-91a3f6c77dfc)<br>
- Agora registramos nossa rota basta apenas você acessar e verificar se o acesso funcionou corretamente na web. Deixamos marcado de vermelho na imagem o sistema de diretorio para o seu auxilio e deixamos na marcação verde os itens que deve ser adicionado no seu arquivo para o funcionamento correto.




## Dicas:
**Replicação de ambientes:**
- Para replicar ambientes venvs vamos utilizar o modulo no python chamado freeze. Para que ele possa salvar em um arquivo txt todos os modulos e bibliotecas que utilizamos no projeto.
- Basta utilizar o comando "pip freeze > nome_arquivo.txt":
```bash
(igor)C:\python\Django> pip freeze > requeriments.txt
```
- Agora para você voltar e criar um servidor igual basta utilizar o comando "pip install -r nome_do_arquivo.txt"
```bash
(igor)C:\python\Django> pip install -r requeriments.txt
```
**Desativação de uma VENV:**
- Para desativar uma VENV basta apenas executar o comando "deactivate":
 ```bash
(igor)C:\python\Django> deactivate
C:\python\Django>
``` 


