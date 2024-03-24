import requests
from bs4 import BeautifulSoup #extração de dados
import pandas as pd

url = "https://www.mercadolivre.com.br/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}#ajuda na compatibilidade

requisicao = requests.get(url, headers=headers)
#print(requisicao)
site = BeautifulSoup(requisicao.text, "html.parser")

valores = site.find_all("span", class_="andes-money-amount__fraction")
titulo = site.find_all("a", class_="poly-component__title")

links = ['https://www.mercadolivre.com.br/' + titulo['href'] for titulo in titulo]

#listas separadas
produto, valor, link = [], [], []
for titulo, preco in zip(titulo, valores):
    produto.append(titulo.get_text().strip())
    valor.append(preco.get_text().strip())  
    link.append('https://www.mercadolivre.com.br/' + titulo['href']) 


# Criar o DataFrame fora do loop
df = pd.DataFrame({'Preço': valor, 'Produto': produto, 'Link': link})

df.head(10)



