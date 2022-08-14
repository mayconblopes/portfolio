<h2>O dilema da gravata</h2>
[![gravata-gimp.gif](https://i.postimg.cc/Nfnw2xDr/gravata-gimp.gif)](https://postimg.cc/GHvfZGZc)
<br>
A cor original da gravata é cinza, mas eu não queria que em todas as fotos a gravata tivesse a mesma cor sem graça... 
então tingi digitalmente utilizando o excelente <a target="_blank" href="https://www.gimp.org/">Gimp</a>.

<h2>Centralizando o conteúdo About</h2>
No conteúdo About ("Um pouco mais sobre mim"), após clicar no botão "Saiba mais" um conteúdo mais detalhado é apresentado,
com uma quantidade maior de texto. Isso fazia com que o usuário tivesse que rolar a página de volta ao início do conteúdo 
About para começar a ler novamente o novo texto.

<h2>Models do Django para evitar alteração no código fonte</h2>
Criei diversos modelos (Model.models) para que a edição do conteúdo do site pudesse ser modificada sem necessidade de 
alterar o código fonte da página, mas tão somente os próprios modelos. Por exemplo: para criar uma nova competência 
profissional ou uma nova experiência de trabalho, basta criar um novo objeto correspondente na página de Administração e este objeto 
automaticamente será exibido no site. Também otimizei algumas funções do Admin do Django para facilitar a 
personalização do conteúdo do site e como este é exibido. Por exemplo, criei um atributo "index_order" no 
modelo referente às competências profissionais e ao alterar o conteúdo deste atributo, a posição do objeto na página 
é modificada, de forma que se torna possível escolher a posição de cada um desses elementos do site diretamente no 
Admin. Além disso, alterei o Admin para permitir edição de certos campos diretamente na ListView dos models.
[![Admin-list-editable.png](https://i.postimg.cc/D01n3bzg/Admin-list-editable.png)](https://postimg.cc/30rPgNm4)