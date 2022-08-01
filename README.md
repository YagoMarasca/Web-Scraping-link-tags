# Web-Scraping-link-tags

Salva um arquivo Excel (XLS) com a lista de links presentes em uma URL

getLinks(URL, depth, fileName)
Ex: getLinks(“https://www.google.com.br”, 2, “linksEnttry.xls”)
Descobre todos os links/urls contidos na página apontada por URL.

Salva um arquivo Excel (XLS) com o nome passado em fileName
Colunas do Excel a ser retornado: “link” (url absoluta do link),”atualTime”(hora que o link foi
encontrado).

Um link não deve ser inserido mais de uma vez na listagem.
O parâmetro depth indica quantos níveis devemos descer na procura

Ex: (0) Somente os links contidos na página URL, (1) Todos de URL e os que estão nas
páginas que estão na lista de links de URL (2) Todos os anteriores e mais os que estão nas
páginas abertas dos links anteriores.... E assim continua descendo a profundidade de
acordo com o número informado.
