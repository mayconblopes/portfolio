<h1>Meu Portfolio</h1>
Este projeto foi criado durante a minha <strong>Certificação Google Ux Design</strong>. Um dos trabalhos requeridos 
foi a criação de um portfolio, recomendando-se a utilização de sistemas de criação de páginas como Wix, 
mas eu preferi colocar a mão na massa e fazer tudo em Python e Django para o backend e usando CSS, HMTL e Javascript 
para o FrontEnd.

A seguir, algumas curiosidades e soluções de código que achei interessante registrar.

<h2>Logo</h2>
Para o logo, utilizei uma estilização do meu proprio nome, simulando traços de pincel. Para criar o estilo, usei uma 
ferramenta online chamada <a target="_blank" href="https://www.tailorbrands.com/">Tailorbrands</a>. Editei o resulado 
no Gimp, acrescentando alguns elementos. 
<br/>

<a target="_blank" href="https://youtu.be/XdeOzhISS34"><img src="https://i.postimg.cc/hvWPtxD6/logo.gif"></a>
<br/>

Depois vetorizei a imagem com outra ferramenta online chamada
<a target="_blank" href="https://products.aspose.app/svg/pt/image-vectorization">Aspose</a>. 

<h2>Tema: cores e fonts</h2>
Minha inspiração para este projeto foi o tema do Ridge Racer Type 4, um game das antigas, com design muito bonito, 
abusando do amarelo e do preto. Algumas imagens que usei de referência:<br>
<img src="https://greenhillszone.files.wordpress.com/2016/03/gfs_13419_2_2.jpg" width="250px">
<img src="https://cdn.dribbble.com/users/335922/screenshots/14084341/media/6e960ed27b325d29e1d380f428b0244c.jpeg" width="250px">

<h2>O dilema da gravata</h2>
<a target="_blank" href="https://youtu.be/z_tYQXtl5e4"><img src="https://i.postimg.cc/Nfnw2xDr/gravata-gimp.gif"></a>
<br>
A cor original da gravata é cinza, mas eu não queria que em todas as fotos a gravata tivesse a mesma cor sem graça... 
então tingi digitalmente utilizando o excelente <a target="_blank" href="https://www.gimp.org/">Gimp</a>, que 
inclusive foi utilizado ao longo de todo o projeto para edição de imagens e ícones.

<h2>Favicon</h2>
Falando em Gimp, foi com ele que eu criei o Favicon do site. Usei a mesma foto acima (do dilema da gravata) para 
criar uma silhueta nas cores do tema do site. Também usei o Gimp para isso.
<br>
<img src="https://i.postimg.cc/Dwxrt7pM/favicon.png" width="250px">
<br>

<h2>O conteúdo detalhado do About</h2>
No conteúdo About ("Um pouco mais sobre mim"), após clicar no botão "Saiba mais" um conteúdo mais detalhado é apresentado,
com uma quantidade maior de texto. Isso fazia com que o usuário tivesse que rolar a página de volta ao início do conteúdo 
About para começar a ler novamente o novo texto. Para melhorar a experiência do usuário, criei um código javascript 
que automaticamente rola a página para o início do novo texto.

<h2>Models do Django para evitar alteração no código fonte</h2>
Criei diversos modelos (Model.models) para que a edição do conteúdo do site pudesse ser modificada sem necessidade de 
alterar o código fonte da página, mas tão somente os próprios modelos. Por exemplo: para criar uma nova competência 
profissional ou uma nova experiência de trabalho, basta criar um novo objeto correspondente na página de 
Administração que cuidará de salvar o objeto no banco de dados e o site buscará os objetos no banco para serem 
automaticamente exibidos no site. Também otimizei algumas funções do Admin do Django para facilitar a 
personalização do conteúdo do site e como este é exibido. Por exemplo, criei um atributo "index_order" no 
modelo referente às competências profissionais e ao alterar o conteúdo deste atributo, a posição do objeto na página 
é modificada, de forma que se torna possível escolher a posição de cada um desses elementos do site diretamente no 
Admin. Além disso, alterei o Admin para permitir edição de certos campos diretamente na ListView dos models.
<img src="https://i.postimg.cc/D01n3bzg/Admin-list-editable.png">
<br/>
<h2>Alternância de classes no HTML para influenciar o CSS dinamicamente, sem JavaSript</h2>
Na linha do tempo das minhas experiências profissionais, eu queria que cada bloco ficasse de um lado da linha do 
tempo, conforme imagem abaixo:<br>
<img src="https://i.postimg.cc/h42PT0y4/tragetoria-profissional.png">
<br/>

Consegui fazer isso de forma muito interessante e rápida sem usar JavaScript, alterando dinamicamente a classe dos 
elementos de acordo com a ordem de listagem. O primeiro elemento a ser exibido vai para o lado esquerdo, o 
segundo vai para o lado direito, o terceiro novamente para o lado esquerdo e assim sucessivamente. 
Não queria que a lógica disso estivesse na view, pois não é uma regra de negócio, mas sim uma mera 
regra para exibição dos itens na tela. Por isso tinha que ficar no template. Sendo assim, utilizei o template tag 
'cycle' do Django, que é uma solução muito elegante para este caso. Veja a documentação do 'cycle' 
<a target="_blank" href="https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#cycle">aqui</a>.
Utilizei o mesmo princípio de alteração dinâmica de HTML por meio de template tags do Django em outros 
trechos do código, como por exemplo para criar IDs dinâmicas para as janelas modais na seção de portfolio.

<h2>Sobre as janelas modais</h2>
As janelas modais são aquelas que exibem conteúdos novos dentro da página atual, ou seja, sem abrir uma nova página. 
Eu usei bastante deste recurso no Portfolio:
<br>
<a target="_blank" href="https://www.youtube.com/watch?v=Mhuz1PnIfqU"><img src="https://i.postimg.cc/SsDbZr2M/Janelas-modais-Adobe-Express.gif"></a>

<br>
Para saber mais sobre como criar janelas modais de forma muito prática, recomendo os seguintes links:
<ol>
    <li><a href="https://getbootstrap.com/docs/4.0/components/modal/">Getbootstrap</a></li>
    <li><a href="https://lokeshdhakar.com/projects/lightbox2/#getting-started">Lightbox</a></li>
</ol>

<h2>Blog</h2>
Adicionei ao projeto um blog 100% funcional.

<hr>
Essas são apenas algumas curiosidades e não uma lista completa de todas as etapas do desenvolvimento deste projeto, 
o qual pode ser melhor entendido olhando-se o código neste respositório e o histórico de commits.

