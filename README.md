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
