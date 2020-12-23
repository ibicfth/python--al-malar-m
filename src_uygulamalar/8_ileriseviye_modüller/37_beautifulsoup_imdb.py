import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html=requests.get(url).content  #içeriği alır.kaynağını

#content=html.content  ##sayfanın kaynağını getirir
soup=BeautifulSoup(html,"html.parser")
list=soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=50) #sadece 1 tane tr getirir.
count=1
for tr in list:
    name=tr.find("td",{"class":"titleColumn"}).find("a").text
    year=tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")  ##strip karakter siler.
    rating=tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    print(f"{count}- {name.ljust(50,'_')} yılı: {year} değerlendirme: {rating}") ##ljust sola dayalı yazıdırır
    count+=1
