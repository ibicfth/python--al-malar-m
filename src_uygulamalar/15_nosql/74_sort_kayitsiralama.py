import pymongo

myclient=pymongo.MongoClient("mongodb+srv://fatihibic:a_002209@cluster0.0t4vk.mongodb.net/test")
mydb=myclient["deneme"] 
mycollection=mydb["product"]

result=mycollection.find() ##hepsini getirir.ancak biz belli bi sıralama ile getirmek istersek;

## tabi her key anahtarlarını kendi içinde sıralar.
result=mycollection.find().sort('name')  ##name kolonunu alfabetik olarak sıralar varsayılan 1 dir

result=mycollection.find().sort('name', 1) ##yukardaki ile aynı alfabetik artar şekilde
result=mycollection.find().sort('name', -1) ## alfabetik azalan şekilde 

## ----liste şeklindede sıralama yaptırtabiliriz.
result=mycollection.find().sort([('name', 1),('price',-1)])
##burda isme göre alfabetik artan ve isimleri aynı olanlarıda fiyatı azalana göre sıralar.
for i in result:
    print(i)