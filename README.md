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
**2.0-** Para verificar o nome do app criado você vai na pasta do app no arquivo app.py, vamos demonstrar com a foto abaixo:<br>
![app](https://github.com/IMNascimento/DjangoSenai/assets/28989407/b64f64ae-4e7e-47b1-8316-73c4501809cb)<br>
-Como podemos verificar na foto temos em vermelho o sistema de diretorio até o arquivo e destacado de verde temos o nome do nosso app.<br>
**2.1-** Agora vamos registrar esse app vamos na pasta do nosso projeto e encontraremos o arquivo "settings.py" nele iremos inserir o nome da nossa aplicação como iremos verificar na foto a seguir:<br>
![registro](https://github.com/IMNascimento/DjangoSenai/assets/28989407/25de48b3-2f5d-433a-8895-07ba60582974)
<br>
-Deixamos novamente com a cor vermelho o sistema de diretorio até o arquivo e marcado de verde a linha com nome que seria inserido.<br>
- Agora que nossa aplicação já foi cadastrada podemos testar se ela irá funcionar corretamente. Para isso precisaremos criar urls para o carregamento externo de nossa página. Veremos essa criação na próxima etapa.

## 3- Criando Url no App Django:
**3.0-** Criação de um arquivo urls.py dentro do seu app que no nosso caso chama "siteTrilhas":<br>
![url](https://github.com/IMNascimento/DjangoSenai/assets/28989407/1b3bf2eb-b78c-4c4b-8693-254a718bdb19)<br>
**3.1-** Quando criarmos esse arquivo url o editor irá informa que não existe o método para isso iremos criar ele em seguida.<br>
![view](https://github.com/IMNascimento/DjangoSenai/assets/28989407/eb553e1c-4356-4980-800d-ad52bb5fd3d6)<br>
**3.2-** Como vimos na imagem acima criamos uma view para exibir um texto "Olá mundo." na nossa página web. Por último Precisamos registrar nossas rotas. <br>
![rotas](https://github.com/IMNascimento/DjangoSenai/assets/28989407/0b5da0d5-b9f2-431c-8e8a-91a3f6c77dfc)<br>
- Agora registramos nossa rota basta apenas você acessar e verificar se o acesso funcionou corretamente na web. Deixamos marcado de vermelho na imagem o sistema de diretorio para o seu auxilio e deixamos na marcação verde os itens que deve ser adicionado no seu arquivo para o funcionamento correto.

## 4- Criando Templates no App Django:
**4.0-** Primeiro dentro da pasta do seu app crie uma pasta chamada templates. No nosso casso nosso app chama "siteTrilhas" e dentro dessa pasta nós iremos criar uma pasta chamada "templates".<br>
**4.1-** Dentro dessa pasta crie um arquivo chamado index.html e coloque os seguintes códigos: 
```html5
<!DOCTYPE html>
<html lang="pt-br">
<head>
<title>Teste Template</title>
</head>
<body>
<h1>Estamos criando um template.</h1>
</body>
</html>
```
**4.2-** Agora vá no arquivo de view.py e coloque o código como está a imagem abaixo:<br>
![viewtemplate](https://github.com/IMNascimento/DjangoSenai/assets/28989407/3bf38177-dc78-43a2-afe9-d296a009de0c)<br>
**4.3-** Agora vá ao arquivo de urls.py e coloque o código a baixo:<br>
![template](https://github.com/IMNascimento/DjangoSenai/assets/28989407/3782f1fd-f47d-4780-a344-2db876d54c58)<br>
-Pronto após execução desses passos tente acessar o endereço 127.0.0.1:8000/pagina o acesso tem que ocorrer corretamente.

## 5- Criando e carregando arquivos estáticos Django:
**5.0-** Vamos no arquivo settings.py na pasta do seu projeto e na linha de templates altere como vai demonstrar a foto a baixo:<br>
![os](https://github.com/IMNascimento/DjangoSenai/assets/28989407/69b21f1e-fe85-409b-ac94-f46aea5a3048)<br>
**5.1-** Esse import OS nós adicionamos no inicio do arquivo settings.py.<br>
![temp](https://github.com/IMNascimento/DjangoSenai/assets/28989407/cbbdea71-6f9d-47f5-997b-291613c8884d)<br>
**5.2-** Agora circulado de vermelho temos o codigo que devemos colocar. Além dessas alterações temos que colocar no final do nosso arquivo o files statics como veremos na foto a seguir.<br>
![static](https://github.com/IMNascimento/DjangoSenai/assets/28989407/2b6124f7-d661-4919-b8fc-0bb3dd18b806)<br>
**5.3-** Como vemos na imagem a cima passamos um caminho de uma pasta static dentro de "trilhas/static", essa pasta static vai precisar ser criada na pastat base do seu projeto.<br>
**5.4-** Agora nesse projeto peque as pastas css, js, imagens e todos os itens de estilos e de javascript que vocês tiverem e coloquem dentro dessa pasta static.<br>
**5.5-** Após colocar os arquivos você precisa executar o comando para o django visualizar os novos arquivos o comando é "python .\manage.py collectstatic" lembrando que para executar os comandos você tem que estar dentro da pasta do trilhas:<br>
```bash
C:\DjangoSenai\trilhas> python .\manage.py collectstatic
```
**5.6-** Agora vamos trocar o código do nosso index.html que está dentro da pasta template no nosso app:<br>
```html5
<!DOCTYPE HTML>
<html>
	<head>
		<title>Fractal by HTML5 UP</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-preload">

		<!-- Header -->
			<header id="header">
				<div class="content">
					<h1><a href="#">Fractal</a></h1>
					<p>Just a simple, single page responsive<br />
					template brought to you by <a href="http://html5up.net">HTML5 UP</a></p>
					<ul class="actions">
						<li><a href="#" class="button primary icon solid fa-download">Download</a></li>
						<li><a href="#one" class="button icon solid fa-chevron-down scrolly">Learn More</a></li>
					</ul>
				</div>
				<div class="image phone"><div class="inner"><img src="images/screen.jpg" alt="" /></div></div>
			</header>

		<!-- One -->
			<section id="one" class="wrapper style2 special">
				<header class="major">
					<h2>Sed ipsum magna lorem tempus amet<br />
					vehicula et gravida elementum</h2>
				</header>
				<ul class="icons major">
					<li><span class="icon solid fa-camera-retro"><span class="label">Shoot</span></span></li>
					<li><span class="icon solid fa-sync"><span class="label">Process</span></span></li>
					<li><span class="icon solid fa-cloud"><span class="label">Upload</span></span></li>
				</ul>
			</section>

		<!-- Two -->
			<section id="two" class="wrapper">
				<div class="inner alt">
					<section class="spotlight">
						<div class="image"><img src="images/pic01.jpg" alt="" /></div>
						<div class="content">
							<h3>Magna sed ultrices</h3>
							<p>Morbi mattis ornare ornare. Duis quam turpis, gravida at leo elementum elit fusce accumsan dui libero, quis vehicula lectus ultricies eu. In convallis amet leo non sapien iaculis efficitur consequat lorem ipsum.</p>
						</div>
					</section>
					<section class="spotlight">
						<div class="image"><img src="images/pic02.jpg" alt="" /></div>
						<div class="content">
							<h3>Ultrices nullam aliquam</h3>
							<p>Morbi mattis ornare ornare. Duis quam turpis, gravida at leo elementum elit fusce accumsan dui libero, quis vehicula lectus ultricies eu. In convallis amet leo non sapien iaculis efficitur consequat lorem ipsum.</p>
						</div>
					</section>
					<section class="spotlight">
						<div class="image"><img src="images/pic03.jpg" alt="" /></div>
						<div class="content">
							<h3>Aliquam sed magna</h3>
							<p>Morbi mattis ornare ornare. Duis quam turpis, gravida at leo elementum elit fusce accumsan dui libero, quis vehicula lectus ultricies eu. In convallis amet leo non sapien iaculis efficitur consequat lorem ipsum.</p>
						</div>
					</section>
					<section class="special">
						<ul class="icons labeled">
							<li><span class="icon solid fa-camera-retro"><span class="label">Ipsum lorem accumsan</span></span></li>
							<li><span class="icon solid fa-sync"><span class="label">Sed vehicula elementum</span></span></li>
							<li><span class="icon solid fa-cloud"><span class="label">Elit fusce consequat</span></span></li>
							<li><span class="icon solid fa-code"><span class="label">Lorem nullam tempus</span></span></li>
							<li><span class="icon solid fa-desktop"><span class="label">Adipiscing amet sapien</span></span></li>
						</ul>
					</section>
				</div>
			</section>

		<!-- Three -->
			<section id="three" class="wrapper style2 special">
				<header class="major">
					<h2>Magna leo sapien gravida</h2>
					<p>Gravida at leo elementum elit fusce accumsan dui libero, quis vehicula<br />
					lectus ultricies eu. In convallis amet leo sapien iaculis efficitur.</p>
				</header>
				<ul class="actions special">
					<li><a href="#" class="button primary icon solid fa-download">Download</a></li>
					<li><a href="#" class="button">Learn More</a></li>
				</ul>
			</section>

		<!-- Four -->
		<!--
			<section id="four" class="wrapper">
				<div class="inner">

					<header class="major">
						<h2>Elements</h2>
					</header>

					<section>
						<h4>Text</h4>
						<p>This is <b>bold</b> and this is <strong>strong</strong>. This is <i>italic</i> and this is <em>emphasized</em>.
						This is <sup>superscript</sup> text and this is <sub>subscript</sub> text.
						This is <u>underlined</u> and this is code: <code>for (;;) { ... }</code>. Finally, <a href="#">this is a link</a>.</p>
						<hr />
						<header>
							<h4>Heading with a Subtitle</h4>
							<p>Lorem ipsum dolor sit amet nullam id egestas urna aliquam</p>
						</header>
						<p>Nunc lacinia ante nunc ac lobortis. Interdum adipiscing gravida odio porttitor sem non mi integer non faucibus ornare mi ut ante amet placerat aliquet. Volutpat eu sed ante lacinia sapien lorem accumsan varius montes viverra nibh in adipiscing blandit tempus accumsan.</p>
						<header>
							<h5>Heading with a Subtitle</h5>
							<p>Lorem ipsum dolor sit amet nullam id egestas urna aliquam</p>
						</header>
						<p>Nunc lacinia ante nunc ac lobortis. Interdum adipiscing gravida odio porttitor sem non mi integer non faucibus ornare mi ut ante amet placerat aliquet. Volutpat eu sed ante lacinia sapien lorem accumsan varius montes viverra nibh in adipiscing blandit tempus accumsan.</p>
						<hr />
						<h2>Heading Level 2</h2>
						<h3>Heading Level 3</h3>
						<h4>Heading Level 4</h4>
						<h5>Heading Level 5</h5>
						<h6>Heading Level 6</h6>
						<hr />
						<h5>Blockquote</h5>
						<blockquote>Fringilla nisl. Donec accumsan interdum nisi, quis tincidunt felis sagittis eget tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan faucibus. Vestibulum ante ipsum primis in faucibus lorem ipsum dolor sit amet nullam adipiscing eu felis.</blockquote>
						<h5>Preformatted</h5>
						<pre><code>i = 0;

while (!deck.isInOrder()) {
  print 'Iteration ' + i;
  deck.shuffle();
  i++;
}

print 'It took ' + i + ' iterations to sort the deck.';</code></pre>
					</section>

					<section>
						<h4>Lists</h4>
						<div class="row">
							<div class="col-6 col-12-medium">
								<h5>Unordered</h5>
								<ul>
									<li>Dolor pulvinar etiam.</li>
									<li>Sagittis adipiscing.</li>
									<li>Felis enim feugiat.</li>
								</ul>
								<h5>Alternate</h5>
								<ul class="alt">
									<li>Dolor pulvinar etiam.</li>
									<li>Sagittis adipiscing.</li>
									<li>Felis enim feugiat.</li>
								</ul>
							</div>
							<div class="col-6 col-12-medium">
								<h5>Ordered</h5>
								<ol>
									<li>Dolor pulvinar etiam.</li>
									<li>Etiam vel felis viverra.</li>
									<li>Felis enim feugiat.</li>
									<li>Dolor pulvinar etiam.</li>
									<li>Etiam vel felis lorem.</li>
									<li>Felis enim et feugiat.</li>
								</ol>
								<h5>Icons</h5>
								<ul class="icons">
									<li><a href="#" class="icon brands fa-twitter"><span class="label">Twitter</span></a></li>
									<li><a href="#" class="icon brands fa-facebook-f"><span class="label">Facebook</span></a></li>
									<li><a href="#" class="icon brands fa-instagram"><span class="label">Instagram</span></a></li>
									<li><a href="#" class="icon brands fa-github"><span class="label">Github</span></a></li>
								</ul>
							</div>
						</div>
						<h5>Actions</h5>
						<div class="row">
							<div class="col-6 col-12-medium">
								<ul class="actions">
									<li><a href="#" class="button primary">Default</a></li>
									<li><a href="#" class="button">Default</a></li>
								</ul>
								<ul class="actions small">
									<li><a href="#" class="button primary small">Small</a></li>
									<li><a href="#" class="button small">Small</a></li>
								</ul>
								<ul class="actions stacked">
									<li><a href="#" class="button primary">Default</a></li>
									<li><a href="#" class="button">Default</a></li>
								</ul>
								<ul class="actions stacked">
									<li><a href="#" class="button primary small">Small</a></li>
									<li><a href="#" class="button small">Small</a></li>
								</ul>
							</div>
							<div class="col-6 col-12-medium">
								<ul class="actions stacked">
									<li><a href="#" class="button primary fit">Default</a></li>
									<li><a href="#" class="button fit">Default</a></li>
								</ul>
								<ul class="actions stacked">
									<li><a href="#" class="button primary small fit">Small</a></li>
									<li><a href="#" class="button small fit">Small</a></li>
								</ul>
							</div>
						</div>
					</section>

					<section>
						<h4>Table</h4>
						<h5>Default</h5>
						<div class="table-wrapper">
							<table>
								<thead>
									<tr>
										<th>Name</th>
										<th>Description</th>
										<th>Price</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>Item One</td>
										<td>Ante turpis integer aliquet porttitor.</td>
										<td>29.99</td>
									</tr>
									<tr>
										<td>Item Two</td>
										<td>Vis ac commodo adipiscing arcu aliquet.</td>
										<td>19.99</td>
									</tr>
									<tr>
										<td>Item Three</td>
										<td> Morbi faucibus arcu accumsan lorem.</td>
										<td>29.99</td>
									</tr>
									<tr>
										<td>Item Four</td>
										<td>Vitae integer tempus condimentum.</td>
										<td>19.99</td>
									</tr>
									<tr>
										<td>Item Five</td>
										<td>Ante turpis integer aliquet porttitor.</td>
										<td>29.99</td>
									</tr>
								</tbody>
								<tfoot>
									<tr>
										<td colspan="2"></td>
										<td>100.00</td>
									</tr>
								</tfoot>
							</table>
						</div>

						<h5>Alternate</h5>
						<div class="table-wrapper">
							<table class="alt">
								<thead>
									<tr>
										<th>Name</th>
										<th>Description</th>
										<th>Price</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>Item One</td>
										<td>Ante turpis integer aliquet porttitor.</td>
										<td>29.99</td>
									</tr>
									<tr>
										<td>Item Two</td>
										<td>Vis ac commodo adipiscing arcu aliquet.</td>
										<td>19.99</td>
									</tr>
									<tr>
										<td>Item Three</td>
										<td> Morbi faucibus arcu accumsan lorem.</td>
										<td>29.99</td>
									</tr>
									<tr>
										<td>Item Four</td>
										<td>Vitae integer tempus condimentum.</td>
										<td>19.99</td>
									</tr>
									<tr>
										<td>Item Five</td>
										<td>Ante turpis integer aliquet porttitor.</td>
										<td>29.99</td>
									</tr>
								</tbody>
								<tfoot>
									<tr>
										<td colspan="2"></td>
										<td>100.00</td>
									</tr>
								</tfoot>
							</table>
						</div>
					</section>

					<section>
						<h4>Buttons</h4>
						<ul class="actions">
							<li><a href="#" class="button primary">Primary</a></li>
							<li><a href="#" class="button">Default</a></li>
						</ul>
						<ul class="actions">
							<li><a href="#" class="button large">Large</a></li>
							<li><a href="#" class="button">Default</a></li>
							<li><a href="#" class="button small">Small</a></li>
						</ul>
						<ul class="actions fit">
							<li><a href="#" class="button fit">Fit</a></li>
							<li><a href="#" class="button primary fit">Fit</a></li>
							<li><a href="#" class="button fit">Fit</a></li>
						</ul>
						<ul class="actions fit small">
							<li><a href="#" class="button primary fit small">Fit + Small</a></li>
							<li><a href="#" class="button fit small">Fit + Small</a></li>
							<li><a href="#" class="button primary fit small">Fit + Small</a></li>
						</ul>
						<ul class="actions">
							<li><a href="#" class="button primary icon solid fa-download">Icon</a></li>
							<li><a href="#" class="button icon solid fa-download">Icon</a></li>
						</ul>
						<ul class="actions">
							<li><span class="button primary disabled">Disabled</span></li>
							<li><span class="button disabled">Disabled</span></li>
						</ul>
					</section>

					<section>
						<h4>Form</h4>
						<form method="post" action="#">
							<div class="row gtr-uniform">
								<div class="col-6 col-12-xsmall">
									<input type="text" name="demo-name" id="demo-name" value="" placeholder="Name" />
								</div>
								<div class="col-6 col-12-xsmall">
									<input type="email" name="demo-email" id="demo-email" value="" placeholder="Email" />
								</div>
								<div class="col-12">
									<select name="demo-category" id="demo-category">
										<option value="">- Category -</option>
										<option value="1">Manufacturing</option>
										<option value="1">Shipping</option>
										<option value="1">Administration</option>
										<option value="1">Human Resources</option>
									</select>
								</div>
								<div class="col-4 col-12-small">
									<input type="radio" id="demo-priority-low" name="demo-priority" checked>
									<label for="demo-priority-low">Low</label>
								</div>
								<div class="col-4 col-12-small">
									<input type="radio" id="demo-priority-normal" name="demo-priority">
									<label for="demo-priority-normal">Normal</label>
								</div>
								<div class="col-4 col-12-small">
									<input type="radio" id="demo-priority-high" name="demo-priority">
									<label for="demo-priority-high">High</label>
								</div>
								<div class="col-6 col-12-small">
									<input type="checkbox" id="demo-copy" name="demo-copy">
									<label for="demo-copy">Email me a copy</label>
								</div>
								<div class="col-6 col-12-small">
									<input type="checkbox" id="demo-human" name="demo-human" checked>
									<label for="demo-human">Not a robot</label>
								</div>
								<div class="col-12">
									<textarea name="demo-message" id="demo-message" placeholder="Enter your message" rows="6"></textarea>
								</div>
								<div class="col-12">
									<ul class="actions">
										<li><input type="submit" value="Send Message" class="primary" /></li>
										<li><input type="reset" value="Reset" /></li>
									</ul>
								</div>
							</div>
						</form>
					</section>

					<section>
						<h4>Image</h4>
						<h5>Fit</h5>
						<div class="box alt">
							<div class="row gtr-uniform">
								<div class="col-12"><span class="image fit"><img src="images/pic04.jpg" alt="" /></span></div>
								<div class="col-4"><span class="image fit"><img src="images/pic01.jpg" alt="" /></span></div>
								<div class="col-4"><span class="image fit"><img src="images/pic02.jpg" alt="" /></span></div>
								<div class="col-4"><span class="image fit"><img src="images/pic03.jpg" alt="" /></span></div>
								<div class="col-4"><span class="image fit"><img src="images/pic02.jpg" alt="" /></span></div>
								<div class="col-4"><span class="image fit"><img src="images/pic03.jpg" alt="" /></span></div>
								<div class="col-4"><span class="image fit"><img src="images/pic01.jpg" alt="" /></span></div>
								<div class="col-4"><span class="image fit"><img src="images/pic03.jpg" alt="" /></span></div>
								<div class="col-4"><span class="image fit"><img src="images/pic01.jpg" alt="" /></span></div>
								<div class="col-4"><span class="image fit"><img src="images/pic02.jpg" alt="" /></span></div>
							</div>
						</div>
						<h5>Left &amp; Right</h5>
						<p><span class="image left"><img src="images/pic05.jpg" alt="" /></span>Fringilla nisl. Donec accumsan interdum nisi, quis tincidunt felis sagittis eget. tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac pellentesque praesent tincidunt felis sagittis eget. tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac pellentesque praesent. Donec accumsan interdum nisi, quis tincidunt felis sagittis eget. tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac pellentesque praesent tincidunt felis sagittis eget. tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac pellentesque praesent. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac pellentesque praesent tincidunt felis sagittis eget. tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac pellentesque praesent.</p>
						<p><span class="image right"><img src="images/pic05.jpg" alt="" /></span>Fringilla nisl. Donec accumsan interdum nisi, quis tincidunt felis sagittis eget. tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac pellentesque praesent tincidunt felis sagittis eget. tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac pellentesque praesent. Donec accumsan interdum nisi, quis tincidunt felis sagittis eget. tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac pellentesque praesent tincidunt felis sagittis eget. tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac pellentesque praesent. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac pellentesque praesent tincidunt felis sagittis eget. tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac pellentesque praesent.</p>
					</section>

				</div>
			</section>
		-->

		<!-- Footer -->
			<footer id="footer">
				<ul class="icons">
					<li><a href="#" class="icon brands fa-facebook-f"><span class="label">Facebook</span></a></li>
					<li><a href="#" class="icon brands fa-twitter"><span class="label">Twitter</span></a></li>
					<li><a href="#" class="icon brands fa-instagram"><span class="label">Instagram</span></a></li>
				</ul>
				<p class="copyright">&copy; Untitled. Credits: <a href="http://html5up.net">HTML5 UP</a></p>
			</footer>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>
```

**5.7-** Antes de testar agora vamos alterar os códigos da nossa inde.html para que ele possa encherga agora nosso css, js. No inicio do arquivo vamos colocar o {% load static %} e em cada link vamos colocar {% static 'caminho_do_seu_item/' %} como veremos os códigos a seguir:<br>
```html5
{% load static %}
<!DOCTYPE HTML>
<html>
	<head>
		<title>Nascimento</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="{% static 'assets/css/main.css' %}" />
		<noscript><link rel="stylesheet" href="{% static 'assets/css/noscript.css' %}" /></noscript>
	</head>
	<body class="is-preload">

		<!-- Header -->
			<header id="header">
				<div class="content">
					<h1><a href="#">Igor Nascimento</a></h1>
					<p>Aqui você colocara um curriculo seu,<br />
					no formato de pdf para ser baixado</p>
					<ul class="actions">
						<li><a href="#" class="button primary icon solid fa-download">Download</a></li>
						<li><a href="#one" class="button icon solid fa-chevron-down scrolly">Learn More</a></li>
					</ul>
				</div>
				<div class="image phone"><div class="inner"><img src="{% static 'images/screen.jpg' %}" alt="" /></div></div>
			</header>

		<!-- One -->
			<section id="one" class="wrapper style2 special">
				<header class="major">
					<h2>Seus principais serviços<br />
					você colocara aqui</h2>
				</header>
				<ul class="icons major">
					<li><span class="icon solid fa-camera-retro"><span class="label">Shoot</span></span></li>
					<li><span class="icon solid fa-sync"><span class="label">Process</span></span></li>
					<li><span class="icon solid fa-cloud"><span class="label">Upload</span></span></li>
				</ul>
			</section>

		<!-- Two -->
			<section id="two" class="wrapper">
				<div class="inner alt">
					<section class="spotlight">
						<div class="image"><img src="{% static 'images/pic01.jpg' %}" alt="" /></div>
						<div class="content">
							<h3>Magna sed ultrices</h3>
							<p>Morbi mattis ornare ornare. Duis quam turpis, gravida at leo elementum elit fusce accumsan dui libero, quis vehicula lectus ultricies eu. In convallis amet leo non sapien iaculis efficitur consequat lorem ipsum.</p>
						</div>
					</section>
					<section class="spotlight">
						<div class="image"><img src="{% static 'images/pic02.jpg' %}" alt="" /></div>
						<div class="content">
							<h3>Ultrices nullam aliquam</h3>
							<p>Morbi mattis ornare ornare. Duis quam turpis, gravida at leo elementum elit fusce accumsan dui libero, quis vehicula lectus ultricies eu. In convallis amet leo non sapien iaculis efficitur consequat lorem ipsum.</p>
						</div>
					</section>
					<section class="spotlight">
						<div class="image"><img src="{% static 'images/pic03.jpg'%}" alt="" /></div>
						<div class="content">
							<h3>Aliquam sed magna</h3>
							<p>Morbi mattis ornare ornare. Duis quam turpis, gravida at leo elementum elit fusce accumsan dui libero, quis vehicula lectus ultricies eu. In convallis amet leo non sapien iaculis efficitur consequat lorem ipsum.</p>
						</div>
					</section>
					<section class="special">
						<ul class="icons labeled">
							<li><span class="icon solid fa-camera-retro"><span class="label">cada icone seus serviços</span></span></li>
							<li><span class="icon solid fa-sync"><span class="label">Sed vehicula elementum</span></span></li>
							<li><span class="icon solid fa-cloud"><span class="label">Elit fusce consequat</span></span></li>
							<li><span class="icon solid fa-code"><span class="label">Lorem nullam tempus</span></span></li>
							<li><span class="icon solid fa-desktop"><span class="label">Adipiscing amet sapien</span></span></li>
						</ul>
					</section>
				</div>
			</section>

		<!-- Three -->
			<section id="three" class="wrapper style2 special">
				<header class="major">
					<h2>Seu nome completo </h2>
					<p>Um pouco sobre você e depois insira novamente o pdf<br />
					com o seu curriculo para download.</p>
				</header>
				<ul class="actions special">
					<li><a href="#" class="button primary icon solid fa-download">Download</a></li>
					<li><a href="#" class="button">Learn More</a></li>
				</ul>
			</section>

		<!-- Footer -->
			<footer id="footer">
				<ul class="icons">
					<li><a href="#" class="icon brands fa-facebook-f"><span class="label">Facebook</span></a></li>
					<li><a href="#" class="icon brands fa-twitter"><span class="label">Twitter</span></a></li>
					<li><a href="#" class="icon brands fa-instagram"><span class="label">Instagram</span></a></li>
				</ul>
				<p class="copyright">&copy; Untitled. Credits: <a href="http://html5up.net">HTML5 UP</a> , <a href="#">Nascimento</a> </p>
			</footer>

		<!-- Scripts -->
			<script src="{% static 'assets/js/jquery.min.js' %}"></script>
			<script src="{% static 'assets/js/jquery.scrolly.min.js' %}"></script>
			<script src="{% static 'assets/js/browser.min.js' %}"></script>
			<script src="{% static 'assets/js/breakpoints.min.js' %}"></script>
			<script src="{% static 'assets/js/util.js' %}"></script>
			<script src="{% static 'assets/js/main.js' %}"></script>

	</body>
</html>
```
**5.8-** Após ter executado esses passos acesse o navegador no endereço 127.0.0.1:8000 e teste verifique se seu layout apareceu corretamente.<br>









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


