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

        test = soup.find("div", class_="mt-4 grid grid-flow-row grid-cols-1 gap-x-8 gap-y-4 xl:grid-cols-3").find_all("div", class_="flex justify-between rounded-xl border border-grey-200 bg-grey-100 p-4")
        print(test)
        title = soup.find("h1", class_="text-[32px] font-bold").text
        information = soup.find("p", class_="line-clamp-5").text
        type_property = soup.find("p", class_="text-sm font-[400]").text
        price = soup.find("p", class_="mb-6 text-[32px] font-bold").text
        rooms = soup.find_all("p", class_="text-sm font-[400]")[1].text
        size = soup.find_all("p", class_="text-sm font-[400]")[2].text
        meter_price = soup.find_all("p", class_="text-sm font-[400]")[7].text
        if meter_price != "Sim":
            meter_price = meter_price
        #price_per_meter = soup.find("div", class_="flex justify-between rounded-xl border border-grey-200 bg-grey-100 p-4").find("p", class_="text-sm font-[400]")[8].text
        washing_machine = soup.find()
        
        print()

Rentola().requisicao() 