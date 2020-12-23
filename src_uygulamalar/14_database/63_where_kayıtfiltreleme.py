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





### ASIL DERS KONU YAPTIĞIMIZ KAYITLARI FİLTRELEMEK ####
def getProducts():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="a_002209",
        database="node-app"
    )

    mycursor=mydb.cursor()

    mycursor.execute('select * from products where id=1') 
##>>>>>>>>>>>>>>>>product tablosundan id=1 olanı getirir. <<<<<<<<<<<<<<<<<<<<<<

##mycursor.execute("select * from products where name='samsung s7'")
## name kolonunda samsung s7 ile eşleşen satırı kaydı getirir. 

## or , and yapılarını kullanabiliriz "select * from products where id=1 and price=2000")

##herhangi bir satırda metin içinde istediğimiz kelime geçen verilerin satırlarını getirmk için;
## mycursor.execute("select * from products where name LIKE '%Samsung%'")
##name kolonunda içinde samsung geçen verilerin satırlarını getir.

##bunu başı samsung sonu ne olurla olsun demek için '%Samsung%' yerine 'Samsung%' ile yaparz.
    result=mycursor.fetchall()


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