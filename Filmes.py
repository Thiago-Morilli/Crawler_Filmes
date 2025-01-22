import requests
from bs4 import BeautifulSoup

class ProbreFlix:

    def __init__(self):
    
        self.url = "https://pobreflix.life/"

    def requisicao(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
    
        """for category in soup.find("ul", class_="sub-menu").find_all("a"):"""
        
        category = soup.find("ul", class_="sub-menu").find_all("a")[0]
        get_link = category.get("href")
        response = requests.get(get_link)
        soup = BeautifulSoup(response.text, "html.parser")
        
        for filme in soup.find("div", class_="items normal").find_all("a"):
            get_link = filme.get("href")
            response = requests.get(get_link)
            soup = BeautifulSoup(response.text, "html.parser")
            print(response)
       
        

ProbreFlix().requisicao()