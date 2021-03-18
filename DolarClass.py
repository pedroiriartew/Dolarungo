from bs4 import BeautifulSoup
import requests

#Corregir en caso de que sea mejor hacer una clase con métodos estáticos o una clase con métodos de clase
#
#
class Dolar:

    def __init__(self, url):
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        self.valor = self.soup.find_all('div', 'value')#Encontra el div con la clase value

    def GetValorCompra(self):
        return self.valor[0].text
    
    def GetValorVenta(self):
        return self.valor[1].text