import requests
from bs4 import BeautifulSoup


class Rentola:

    def __init__(self):
        
        self.url = "https://rentola.pt/"
        self.data_dict = {}


    def requisicao(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        get_link = soup.find("div", class_="flex mb-2 w-max gap-4").find_all("a")[5]
        link = get_link.get("href")
        link_updated = ("https://rentola.pt" + link)
        response = requests.get(link_updated)
        soup = BeautifulSoup(response.text, "html.parser")
        self.entering_category(link_updated)
        

    def entering_category(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        self.entering_properties(soup)
        self.next_page(soup)

    def entering_properties(self, soup):
        for get_link in soup.find_all("a", class_="absolute inset-0 z-[1]"):
            link = get_link.get("href")
            link_updated = ("https://rentola.pt" + link)
            response = requests.get(link_updated)
            soup = BeautifulSoup(response.text, "html.parser")
            self.extracting_data(soup, link_updated)


    def extracting_data(self, soup, link_apdated):

        self.data_dict["Title"] = soup.find("h1", class_="text-[32px] font-bold").text
        self.data_dict["Information"] = soup.find("p", class_="line-clamp-5").text
        self.data_dict["Type_property"] = soup.find("p", class_="text-sm font-[400]").text            
        self.data_dict["Price"] = soup.find("p", class_="mb-6 text-[32px] font-bold").text
        entry_price = soup.find("span", class_="font-medium text-primary-100").text
        if entry_price != "Ilimitado":
            self.data_dict["Entry_price"] = entry_price
        self.data_dict["Rooms"] = soup.find_all("p", class_="text-sm font-[400]")[1].text
        self.data_dict["Location"] = soup.find("p", class_="text-primary-100").text
        Available = soup.find_all ("div", class_="mb-4 flex justify-between")[2].find_all("span")[1].text
        if Available != "Ilimitado" and "ASAP":
            self.data_dict["Available"] = Available
          
        else:
            self.data_dict["Available"] = soup.find_all ("div", class_="mb-4 flex justify-between")[1].find_all("span")[1].text
          
        self.data_dict["link"] = link_apdated

        print(self.data_dict)
        print("-=" * 90)

    def next_page(self, soup):

        #page = soup.find("div", class_="flex items-end gap-2 sm:mx-6").find_all("a")[3].text
        page_int = int(476)
       
        for cont in range(0,page_int + 1):
            
            links = (f"https://rentola.pt/alugar?page={cont}")
            self.entering_category(links)

            print(links)
            print("*" * 90)

            

"""page = soup.find("a", class_="inline-flex shrink-0 items-center justify-center outline-none transition-colors disabled:cursor-not-allowed disabled:opacity-50 h-[40px] text-base bg-transparent text-primary-100 rounded-lg font-medium").get("href")
final = soup.find("a", class_="inline-flex shrink-0 items-center justify-center outline-none transition-colors disabled:cursor-not-allowed disabled:opacity-50 h-[40px] text-base bg-transparent text-grey-400 pointer-events-none cursor-not-allowed opacity-50 rounded-lg font-medium")
if "/alugar?page=" in page:
    page = page
    print(page)"""
            #link = page.get("href")
            #link_updated = (self.url + link)
            
            #self.entering_category(link_updated)
Rentola().requisicao() 