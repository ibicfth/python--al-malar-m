import mysql.connector


'''
def deleteProduct(): ##class ta mutlaka self tanımlamlıyız ama class olmadığında gerek yok
    mydb_connection=mysql.connector.connect(host="localhost",user="root",password="a_002209",database="node-app")
    mycursor=mydb_connection.cursor()

    sql="DELETE FROM products where id=6"
## id=6 olan kaydı sil.
    
##farklı şekilde sorgulama örneği;
## sql="DELETE FROM products where name like '%s7%'"
##name kolonunda içinde s7 geçen verilerin satırlarını sil.

    mycursor.execute(sql)
    try:
        mydb_connection.commit()
        print(F"toplam: {mycursor.rowcount} adet veri silindi.")
    except mysql.connector.Error as err:
        print('hata: ',err)
    finally:
        mydb_connection.close()

deleteProduct()

'''
##dışardan verilen parametreye göre silme işlemi yaptırmak içim;


def deleteProduct(id): ##class ta mutlaka self tanımlamlıyız ama class olmadığında gerek yok
    mydb_connection=mysql.connector.connect(host="localhost",user="root",password="a_002209",database="node-app")
    mycursor=mydb_connection.cursor()

    sql="DELETE FROM products where id=%s"
    values=(id,) ##(,) koymak zorundayız
    
##farklı şekilde sorgulama örneği;
## sql="DELETE FROM products where name like '%s7%'"
##name kolonunda içinde s7 geçen verilerin satırlarını sil.

    mycursor.execute(sql,values)
    try:
        mydb_connection.commit()
        print(F"toplam: {mycursor.rowcount} adet veri silindi.")
    except mysql.connector.Error as err:
        print('hata: ',err)
    finally:
        mydb_connection.close()

deleteProduct(8)