import requests
from bs4 import BeautifulSoup
import mysql.connector


class Rentola:

    def __init__(self):
        
        self.url = "https://rentola.pt/"
        self.data_dict = {}


    def requisicao(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        get_link = soup.find("div", class_="flex mb-2 w-max gap-4").find_all("a")[5]
        link = get_link.get("href")
        link_updated = (self.url + link)
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
            link_updated = (self.url + link)
            response = requests.get(link_updated)
            soup = BeautifulSoup(response.text, "html.parser")
            self.extracting_data(soup, link_updated)


    def extracting_data(self, soup, link_apdated):

        self.data_dict["Title"] = soup.find("h1", class_="text-[32px] font-bold").text
        self.data_dict["Information"] = soup.find("p", class_="line-clamp-5").text
        self.data_dict["Type_property"] = soup.find("p", class_="text-sm font-[400]").text            
        self.data_dict["Price"] = soup.find("p", class_="mb-6 text-[32px] font-bold").text
        """entry_price = soup.find("span", class_="font-medium text-primary-100").text
        if entry_price != "Ilimitado":
            self.data_dict["Entry_price"] = entry_price"""
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

        self.save_mysql()
 
    def next_page(self, soup):

        link = soup.select('div [role="navigation"] a')
        test = link[len(link)-1].get("href")
        link_updated = (self.url + test)
        print("*" * 90)
        print(link_updated)
        print("*" * 90)
        self.entering_category(link_updated)


    def save_mysql(self):

        db_connection = mysql.connector.connect(
        host=("127.0.0.1"),
        port=("3306"),       
        user=("root"),      
        password=("998674629Th."),    
        database="Rentola" 
        )

        if db_connection.is_connected():
            print("Conexão com o banco de dados está ativa.")
        else:
            print("Conexão com o banco de dados falhou.")
            
        cursor = db_connection.cursor()
        


        insert_query = """
                        INSERT INTO  Properties(Title, Information, Type_property, Price, Rooms, Location, Available, link)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """
        

        cursor.execute(insert_query, (
                self.data_dict["Title"],
                self.data_dict["Information"],
                self.data_dict["Type_property"],
                self.data_dict["Price"],
                self.data_dict["Rooms"],
                self.data_dict["Location"],
                self.data_dict["Available"],
                self.data_dict["link"]
            ))
        db_connection.commit()


        print("Dados salvos com sucesso!")
    

        cursor.close()
        db_connection.close()

Rentola().requisicao() 