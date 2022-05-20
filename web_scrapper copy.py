#   baixar python pelo instalador normal
#   pip install requests no cmd
#   pip install bs4 no cmd

from bs4 import BeautifulSoup


html_doc = """
<html>

<title>Another title</title>
<head>

</head>
<body>
    <p class="title"><b>Dornes Story</b></p>

    <p class="story">Once upon a time

        <a href="https://https://example.com/elsie" class="sister" id="link1">Elsie</a>
        <a href="https://https://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="https://https://example.com/tillie" class="sister" id="link3">Tillie</a>
    </p>

</body>
</html>
"""

soup = BeautifulSoup(html_doc,'html.parser')

#print(soup.title.get_text()) # pega a tag title inteira
#print(soup.title.get_text()) # pega o texto dentro do title
#print(soup.title.parent.name)  # busca a tag que esta acima do p, que no caso é a html
#print(soup.p['class']) #busca classe do primeiro p que encontrar
#print(soup.find('p'))  #busca tag inteira do primeiro p que encontrar
#print(soup.find_all('p')) # busca todos os p do documento
#print(soup.find_all(id="link1")) # pega tudo que tem o id link1
print(soup.find(id="link1").get_text()) # pega todo texto que tem o id link1




