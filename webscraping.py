import requests
from bs4 import BeautifulSoup #extração de dados

url = "https://www.mercadolivre.com.br/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}#ajuda na compatibilidade

requisicao = requests.get(url, headers=headers)
print(requisicao)

site = BeautifulSoup(requisicao.text, "html.parser")

valores = site.find_all("span", class_="andes-money-amount--cents-superscript")
titulo = site.find_all("a", class_="poly-component__title")


for preco in valores: #armazena cada item da lista valores na variavel preco
    valor_extraido = preco.get_text()#extrair texto
    print(valor_extraido)

    #for tituloPreco in titulo:
       # titulo_extraido = tituloPreco.get_text()
   #  print(titulo_extraido)



