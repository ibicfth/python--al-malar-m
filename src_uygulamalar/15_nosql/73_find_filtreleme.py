import pymongo

myclient=pymongo.MongoClient("mongodb+srv://fatihibic:a_002209@cluster0.0t4vk.mongodb.net/test")
mydb=myclient["deneme"] 
mycollection=mydb["product"]

## find ın ilk parametresi query idi where anlamı var, aşağıda ilk parametreyi direk find içine 
##yazmak yerine filter nesnesi oluşturup içine yazdık.
## name i iphone olan verileri getir dedik.
# filter={"name" : "iphone"}

# result=mycollection.find(filter)  ##find({"name":"iphone"}) şeklindede olabilirdi.

# for i in result:
#     print(i)

##--------------------------------------------------

## _id:"5fa3d62e0b918d0596547d7c" ##data basede olan bir anahtar

##biz bu key anaharına göre arama yaptırmak istediğimizde hata alırız 
##bu key anahtarına göre arama yaptırabilmek için object_id olarak tanımlamalıyız.
##object ıd oluşturmak için modül

# from bson.objectid import ObjectId

# result=mycollection.find({"_id":ObjectId("5fa3d62e0b918d0596547d7c")})  ##find({"name":"iphone"}) şeklindede olabilirdi.

# print(result)

##-----------------------------------------------------

##diğer find kullanımları 


## 1--   $in   eşitlik parametresi;
# result=mycollection.find({
#     "name":{
#         "$in": ["samsung s6","samsung s7","samsung s8"]
#     }
# })# ilk parametre query idi. burda name key i samsung s6 ve samsung s7 olan verileri filtreler.


# result=mycollection.find({
#     "name":{
#         "$in": ["samsung"]
#     } 
# }) ##bişey getirmez isim tam yazılmalı..

##yada regular expression kullanılmalı. $regex
# result=mycollection.find({
#     "name":{
#         "$regex": "^s"
#     } 
# }) #name alanı s ile başlayanları getir.


## 2--   $gt   büyüklük parametresi;  $gte büyükeşit
# result=mycollection.find({
#     "price":{
#         "$gt": 2000
#     } 
# }) ## price 2000 den büyük olanları getirir.


## 3--   $eq eşit parametresi.
# result=mycollection.find({
#     "price":{
#         "$eq": 2000
#     }  
# }) ## price 2000 e eşit olanı getirir.

## 4--   $lt küçüklük parametresi yada $lte küçükeşit
# result=mycollection.find({
#     "price":{
#         "$lte": 2000
#     }  
# }) ## price 2000 den küçük eşit

# for i in result:
#     print(i)

##>>>>>>bunları mongodb queryoperators olarak aratabiliriz.