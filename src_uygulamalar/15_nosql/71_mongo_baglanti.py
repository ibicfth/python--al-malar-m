import pymongo

## 1 -- compass ile yerele  localhosta bağlantı için;  mongodb://localhost:27017

##compassta yerel database uzaktaki(netteki) ile aynı değildir.tabiki compass ile uzaktakinede bağlantı yapabilriz. 
#myclient=pymongo.MongoClient("mongodb://localhost:27017")

##şimdide veritabanındaki bir database e ulaşmak için;
#mydb=myclient["node-app"]

##pythondan olmayan bir database i sadece isim ile olulturamayız:
##mutlaka collection ve bu collection içinde en az bir veri olması lazım.
##yani şuan node-app oluşturamayacagız.


##------------------------------------------
##şimdide veritabanında olan database leri görüntüleyelim
#print(myclient.list_database_names())

## 2 -- uzak database bağlanmak için  mongodb+srv://fatihibic:<password>@cluster0.0t4vk.mongodb.net/test


# myclient=pymongo.MongoClient("mongodb+srv://fatihibic:a_002209@cluster0.0t4vk.mongodb.net/test")

# print(myclient.list_database_names())


## ---------------------------------------------
##şimdide python ile yeni bir database oluşturup collection ekleyelim:
# myclient=pymongo.MongoClient("mongodb+srv://fatihibic:a_002209@cluster0.0t4vk.mongodb.net/test")

# mydb=myclient["deneme"] ##olmayan database
# mycollection=mydb["product"] ## node-app databaseinin içinde product tablosunu oluşturduk
# ##ancak yeni bir data bse oluşturabilmek için adımların hepsinin tamamalamalıyız.
# ## database olulturma adımları;
# ##1- database adı tanımla
# ##2- database içinde bir collection tanımla
# ##3- bu collection içine bir veri var.

# ##şimdi veri verelim product collectiona 
# veri_1={"name":"fatih","surname":"ibic"}
# result=mycollection.insert_one(veri_1)  ## tekbir veri insert_one  veriyi product collectiona ekler.

# ##-----------------------------------
# ##her bir verinin key_id si vardor ve kendi oluşturur.bunu göstermek için; inserted_id çok kayıt varsa;insert_ids
# print(result.inserted_id)

##----------------------------------
## birden fazla kayıt ekleme;
myclient=pymongo.MongoClient("mongodb+srv://fatihibic:a_002209@cluster0.0t4vk.mongodb.net/test")
mydb=myclient["deneme"] 
mycollection=mydb["product"]
coklu_veriler=[
    {"name":"samsung s6","price":10000},
    {"name":"iphone","price":20000},
    {"name":"nokia","price":1500},
    {"name":"sony","price":1000},
    
]

mycollection.insert_many(coklu_veriler)