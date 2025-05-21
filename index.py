import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml
Product_name = []
product_price = []
Descriptions = []
Reviews = []

for i in range(2,12):
    url="https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page="+str(i)
    r=requests.get(url)
    #print(r)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_= "DOjaWF gdgoEp")


    #product names find 
    name = box.find_all("div", class_="KzDlHZ") 
    for i in name : 
        name = i.text 
        Product_name.append(name)

    #print(Product_name)   

    #products prices find
    prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
    for i in prices: 
        prices = i.text
        product_price.append(prices)

    #print(product_price)

    #product Descriptions find 
    Description = box.find_all("ul", class_="G4BRas")
    for i in Description:
        Description =i.text
        Descriptions.append(Description)
    #print(Descriptions)

    #product Reviews

    Review = box.find_all("div", class_="XQDdHH")
    for i in Review:
        Review = i.text
        Reviews.append(Review)

    #print(Reviews)

min_length = min(len(Product_name), len(product_price), len(Descriptions), len(Reviews))

Product_name = Product_name[:min_length]
product_price = product_price[:min_length]
Descriptions = Descriptions[:min_length]
Reviews = Reviews[:min_length]

df = pd.DataFrame({
    "Product Name": Product_name,
    "Prices": product_price,
    "Description": Descriptions,
    "Review": Reviews
})

print(df.head())  # Print first few rows to verify

df.to_csv("D:/lalit work/Flipkart mobile under 50000.csv")





    #print(soup)
    #while True:
    #np = soup.find("a", class_="_9QVEpD").get("href")
    #cnp="https://www.flipkart.com"+np
    #print(cnp)

   # url = cnp
    #r = requests.get(url)
    #soup = BeautifulSoup(r.text,"lxml")