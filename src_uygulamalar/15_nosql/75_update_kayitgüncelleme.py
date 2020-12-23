import pymongo

myclient=pymongo.MongoClient("mongodb+srv://fatihibic:a_002209@cluster0.0t4vk.mongodb.net/test")
mydb=myclient["deneme"] 
mycollection=mydb["product"]

# ##update_one  update_many
# mycollection.update_one(
#     {"name":"samsung s6"},
#     {"$set":{"name":"motorola"}}

#)
## aslında birden fazla samung s6 var ama update_one dediğimizden ilk bulduğunu sadece günceller.
##hepsini tek seferde istersek update_many ullanırız.



## ------- birden fazla keyi değiştirmek için

# mycollection.update_one(
#     {"name":"motorola"},
#     {"$set":{"name":"motorola xp", "price":1111}}

# )

##dışarda da yazabiliriz.
mevcut= {"name":"motorola"}
degistir={"$set":{"name":"motorola xp", "price":1111}}

mycollection.update_one(mevcut,degistir)

for i in mycollection.find():
    print(i)

###--------------- kaçtane kaydın günceelendiğini sayar: modified_count
result=mycollection.update_one(mevcut,degistir)

print(result.modified_count)
