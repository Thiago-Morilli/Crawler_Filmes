import requests
from bs4 import BeautifulSoup


class Rentola:

    def __init__(self):
    
        self.url = "https://rentola.pt/"

    def requisicao(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        get_link = soup.find("div", class_="flex mb-2 w-max gap-4").find_all("a")[5]
        link = get_link.get("href")
        link_updated = ("https://rentola.pt" + link)
        response = requests.get(link_updated)
        soup = BeautifulSoup(response.text, "html.parser")

        for get_link in soup.find_all("a", class_="absolute inset-0 z-[1]"):
            link = get_link.get("href")
            link_updated = ("https://rentola.pt" + link)
            response = requests.get(link_updated)
            soup = BeautifulSoup(response.text, "html.parser")
            self.extracting_data(soup)


    def extracting_data(self, soup):

        title = soup.find("h1", class_="text-[32px] font-bold").text
        information = soup.find("p", class_="line-clamp-5").text
        type_property = soup.find("p", class_="text-sm font-[400]").text            
        price = soup.find("p", class_="mb-6 text-[32px] font-bold").text
        entry_price = soup.find("span", class_="font-medium text-primary-100").text
        if entry_price != "Ilimitado":
            entry_price = entry_price
        rooms = soup.find_all("p", class_="text-sm font-[400]")[1].text
        location = soup.find("p", class_="text-primary-100").text
        available = soup.find("span", class_="text-sm text-grey-400")
        
        

Rentola().requisicao() 