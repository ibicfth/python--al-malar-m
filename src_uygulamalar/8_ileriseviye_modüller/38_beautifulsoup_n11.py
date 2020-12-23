from bs4 import BeautifulSoup
import requests

url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html=requests.get(url).text

soup=BeautifulSoup(html,"html.parser")
list=soup.find_all("li",{"class":"column"},limit=1) ###sadece bir ürün için yaptık, limiti hiç vermezsek o sayfada gösterilen ürünlerin hepsi kadar bulur geitir.

for li in list:
    name=li.div.div.h3.text.strip() 
    link=li.div.div.a["href"] ##yada;
    link=li.div.div.a.get("href")
    oldprice=li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip('TL')
    newprice=li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip('TL')
    print(f"name: {name} link: {link} old price: {oldprice} new price: {newprice}")