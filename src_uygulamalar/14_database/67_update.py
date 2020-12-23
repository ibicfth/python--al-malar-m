import mysql.connector

'''
def updateProduct(): ##class ta mutlaka self tanımlamlıyız ama class olmadığında gerek yok
    mydb_connection=mysql.connector.connect(host="localhost",user="root",password="a_002209",database="node-app")
    mycursor=mydb_connection.cursor()

    sql="UPDATE products SET  name='samsung s10' where id=5"

##id=5 olan satırın name ini samsung s10 olarak günceller
##bunu ayrı nesne tanımlamadan direk execute ün içinede yazabilirdik


## birden fazla kolonuda güncelleyebilriz.
##sql="UPDATE products SET  name='samsung s10',price=5000 where id=5"
    mycursor.execute(sql)
    try:
        mydb_connection.commit()
        print(F"toplam: {mycursor.rowcount} adet veri güncellendi.")
    except mysql.connector.Error as err:
        print('hata: ',err)
    finally:
        mydb_connection.close()

updateProduct()

'''

##yukardaki programı kullanıcıdan alınan değerlere göre işlemesi için;

def updateProduct(id,name,price): ##class ta mutlaka self tanımlamlıyız ama class olmadığında gerek yok
    mydb_connection=mysql.connector.connect(host="localhost",user="root",password="a_002209",database="node-app")
    mycursor=mydb_connection.cursor()

    sql="UPDATE products SET  name='%s',price='%s' where id='%s'"
    values=(name,price,id)

##id=5 olan satırın name ini samsung s10 olarak günceller
##bunu ayrı nesne tanımlamadan direk execute ün içinede yazabilirdik


## birden fazla kolonuda güncelleyebilriz.
##sql="UPDATE products SET  name='samsung s10',price=5000 where id=5"
    mycursor.execute(sql,values)
    try:
        mydb_connection.commit()
        print(F"toplam: {mycursor.rowcount} adet veri güncellendi.")
    except mysql.connector.Error as err:
        print('hata: ',err)
    finally:
        mydb_connection.close()

updateProduct(1,'iphone 12',8900)