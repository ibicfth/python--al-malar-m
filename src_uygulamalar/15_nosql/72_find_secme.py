import pymongo

myclient=pymongo.MongoClient("mongodb+srv://fatihibic:a_002209@cluster0.0t4vk.mongodb.net/deneme")
mydb=myclient["deneme"] 
mycollection=mydb["product"]

## tek bir veri için find_one çoklu verilerde find kullanılır.
# result=mycollection.find_one() 
# print(result)

# for i in mycollection.find():
#     print(i)

##---------------------------------------------

##şimdide find mehtodunun parametrelerini inceleyelim;
##ilk parametresi guery>>where gibi 
##ikincisi ise kolon parametresi 

# for i in mycollection.find({},{'_id':0,'price':1}):
#     print(i)


##_id anahtarı istisna gelmesini isteiğimiz kolonlara 1 veririz diğer kolonları yazmayız sıfır vermeyiz.
##örn={'_id':0,'name':0,price':1}) hata veirir name: 0 yerine name yi yazmamalıyız.


for i in mycollection.find({},{'_id':0,'price':0}):
    print(i)


##yada _id anahatarı istisna gelmesini istemediğimiz kolonlara 0 veririz ve,
##gelmesini isteiğimiz kolonları belirtmeyiz
##örn={'_id':0,'name':0,price':1}) hata veirir price: 1 yerine name yi yazmamalıyız.


##yani karışık seçme yaptıramayız ya gelmesini isteiklerimizi yada
##gelmesini istemediklermizi belirtebiliriz _id: istisna
