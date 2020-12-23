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





### ASIL DERS KONU YAPTIĞIMIZ KAYITLARI SAYMAK####
def getProducts():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="a_002209",
        database="node-app"
    )

    mycursor=mydb.cursor()

    mycursor.execute('select count(*) from products') 
## products tablosunun satırlarının sayısını bulur.

##filtreleyipte sayma yaptırabiliriz.
##mycursor.execute('select count(*) from products where price> 5000')
##fiyatı 5000 ten büyük olan satırların sayısını getirir.

##  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< OO >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##

##ortalama almak için avg() kullanılır.
    mycursor.execute('select avg(price) from products')
##fiyat  kolonunun ortalamasını alır.

## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< OO >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
## toplam almak için sum () kullanılır.
    mycursor.execute('select sum(price) from products')
## fiaytların toplamını verir.

## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< OO >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
## max ve min değerini bulmak için max() veya min() kullanılır.
    mycursor.execute('select max(price) from products')
##price kolonunun max fiyatlı olanını getirir.
    mycursor.execute('select min(price) from products')
## price kolonunun min fiyatlı olanını getirir.

## filteleme ile birlikte kullanmak istersek;
    mycursor.execute('select name from products where price=(select min(price) from products)')
## fiyatı price kolonunun min olanının adını getir.


    result=mycursor.fetchone()

    print(result)



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