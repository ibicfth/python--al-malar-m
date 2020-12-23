import pymongo

myclient=pymongo.MongoClient("mongodb+srv://fatihibic:a_002209@cluster0.0t4vk.mongodb.net/test")
mydb=myclient["deneme"] 
mycollection=mydb["product"]

##tek bir kayıt silme delete_one  delete_many
# for i in mycollection.find(): ##silinmeden önceki kayıtlar
#     print(i)

# print('*'*50)

# mycollection.delete_one({"name":"motorola"})

# for i in mycollection.find():##silinmeden sonraki kayıtlar
#     print(i)


##-------------------------------------------------------------------------
##bunu regular expresiion çoğulunu yapalaım

# mycollection.delete_many({"name":{"$regex":"^s"}})
# ## s ile başlayan bütün kaytları siler.

# for i in mycollection.find():##silinmeden sonraki kayıtlar
#     print(i)


##---------------------------------------------------
## delected_count silinen kayıt sayısını veriri.
result=mycollection.delete_many({"name":{"$regex":"^s"}})
print(result.deleted_count)