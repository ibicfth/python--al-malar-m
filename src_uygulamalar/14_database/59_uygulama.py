import mysql.connector 


# def insertProduct(name,price,imageUrl,description):
#     mydb=mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="a_002209",
#         database="node-app"
#     )

#     mycursor=mydb.cursor()

#     sql="INSERT INTO Products(name,price,imageUrl,description) values(%s,%s,%s,%s)" #%s yer tutucusonradan belirleyeceğiz
#     values=(name,price,imageUrl,description)

#     mycursor.execute(sql,values)

#     try:
#         mydb.commit()  ##cursor.execute(sql,values) u çalıştırır.
#         print(f"{mycursor.rowcount} tane kayıt eklendi") #rowcount eklenen kayıt adetini getirir.
#         print(f"eklenen son kaydın id: {mycursor.lastrowid}")# son kaydın id numarasını getirir.
#     except mysql.connector.Error as err:
#         print('hata: ', err)
#     finally:
#         mydb.close()
#         print('database kapatıldı')



# name=input('ürün adı giriniz: ')
# price=float(input('ürün fiyatı giriniz: '))
# imageUrl=input('ürün resim adı giriniz: ')
# description=input('ürün açıklaması giriniz: ')

# insertProduct(name,price,imageUrl,description)


#########yukardaki tek bir kayıt işlemi için yapılmış program eğer çoklu kayıt yapacak isek;
## aşağıdaki gibi değişiklik yapabiliriz programda;

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
        break

