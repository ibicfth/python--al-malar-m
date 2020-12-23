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





### ASIL DERS KONU YAPTIĞIMIZ KAYITLARI GETİRMEK ####
def getProducts():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="a_002209",
        database="node-app"
    )

    mycursor=mydb.cursor()

    mycursor.execute('select * from products') 
## product tablosundan tüm(*) verileri getir ['select * from products']

    result=mycursor.fetchall()
## fetchall çoklu tablo okumalarında kullanılır.

##tek vir veriyi almak için fetchone() kullnılır tek bir eleman satırı getirir.


    print(result) ##bu toplu liste halinde getirir ve okunurluğu zor olur alternatif;

## for product in result:
##      print(product)   ##elemanları tektek getirir.satır satır yani
'''
##yada aldıklarımızdan işimize yarar olanı göstermek için;
## for product in result:
##      print(f"name: {product[1]} fiyat: {product[2]}"")  ### 0.index  id numarası 

>>>>>  ancak bize ürün adı ve fiyatı gerekiyorken bütün verileri çağırmak yerine ;
sadece bu iki veriyi tablodan alabiliriz bunun için seçme işlemini şu şekilde yapabiliriz;
mycursor.execute('select name,price from products')

bunu for döngüsü olarak yazadırmak içinse 
for product in result:
    print(product)   yazdırılabilir yada formatlı yazdırabiliriz ancak 

formatlı yazdırmada tüm veri aldığımızda tablo id kolonu ile başlıyordu yani;
0. index id kolonunun verisiydi  biz select name,price from products ile aldığımız 
sadece 2 kolon var yani 0.kolon(index) name,1.index price formatlı yazarken dikkat et.

for product in result:
    print(f"name: {product[0]} fiyat: {product[1]}") şeklinde olmalıdır.




'''
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