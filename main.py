import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=cotacao+dolar"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" }

requesicao = requests.get(link, headers=headers) #para conseguir modificar a pagina
print(requesicao)
#print(requesicao.text)
site = BeautifulSoup(requesicao.text, "html.parser")#organizar o html da pagina 
#print(site.prettify()) #ferramenta do beautify printar a organização - FUNÇÃO DO PYTHON


#RASPAGEM DE DADOS

titulo = site.find("title")
print(titulo)

#pesquisa = site.find_all("input") #pega todas as tags INPUT
#print(pesquisa[2]) #especifica qual tag deve ser pegada

pesquisa2 = site.find("textarea", class_="gLFyf")
print(pesquisa2)
print(pesquisa2["value"]) #pega um elemento especifico

cotacaoDolar = site.find("span",class_="SwHCTb")
print(cotacaoDolar["data-value"])#pega o valor da tag
print(cotacaoDolar.get_text())#pega apenas o texto
