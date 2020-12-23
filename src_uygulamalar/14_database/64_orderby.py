##bu kısmı 59_uygulama.py da zaten yapmıştık
import mysql.connector

def insertProducts(list):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="a_002209",
        database="node-app"
    )

    mycursor=mydb.cursor()

    sql="INSERT INTO Products(name,price,imageUrl,description) values(%s,%s,%s,%s)" #%s yer tutucusonradan belirleyeceğiz
    #Products tablo adı
    values=list

    mycursor.executemany(sql,values) ##çoklu girdilerde execute değil executemany kullnılır.

    try:
        mydb.commit()  ##cursor.execute(sql,values) u çalıştırır.
        print(f"{mycursor.rowcount} tane kayıt eklendi") #rowcount eklenen kayıt adetini getirir.
        print(f"eklenen son kaydın id: {mycursor.lastrowid}")# son kaydın id numarasını getirir.
    except mysql.connector.Error as err:
        print('hata: ', err)
    finally:
        mydb.close()
        print('database kapatıldı')





### ASIL DERS KONU YAPTIĞIMIZ KAYITLARI SIRALAMAK ####
def getProducts():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="a_002209",
        database="node-app"
    )

    mycursor=mydb.cursor()

    mycursor.execute('select * from products order by name asc') 
## isme göre sıralama yapar. varsayılan asc : artan , dec: azalan

##birden fazla sıralama kriteri verebiliriz.
##mycursor.execute('select * from products order by name,price asc')
##önce ismegöre sıralar sonra sıralanları fiyata göre sıralar.
    result=mycursor.fetchall()

    for product in result:
        print(product)



####programa asıl eklenen yer üst kısım alt kısımda ise sadece bu sınıfı çağırdık gerisi vardı zaten. ####
list=[]
while True:
    name=input('ürün adı giriniz: ')
    price=float(input('ürün fiyatı giriniz: '))
    imageUrl=input('ürün resim adı giriniz: ')
    description=input('ürün açıklaması giriniz: ')

    list.append((name,price,imageUrl,description)) ##tuple listesi şeklinde ekleme yapıyoruz.
    result=input("kayıt yapmaya devam etmek istiyor musunuz (e/h): ")
    if result=='h':
        print(list)
        print("kayıt ekleme işlemi gerçekleştiriliyor ...")
        insertProducts(list)
        getProducts() ##yukarıdaki sınıfı çıkmadan çalıştırıp databasedeki verileri okuruz.
        break