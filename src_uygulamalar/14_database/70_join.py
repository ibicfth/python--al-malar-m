import mysql.connector



def getProducts():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="a_002209",
        database="node-app"
    )

    mycursor=mydb.cursor()

    # sql="select * from products "
    # sql="select * from categories "
    # sql="select * from products inner join categories on products.category_id=categories.id"
##  products ile categories tablosunu inner join (ortak keşişim dir)
##  ortak keşişimin hangi kolonları olduğunu on ile belirtiriz. (on products.category_id=categories.id)

##ancak bu keşişimleri hem products tablosu hemde categories tablosu için yazar. isteğimiz kolonları getirmek için;
    #sql="select products.name,products.price,categories.name from products inner join categories on products.category_id=categories.id"


## filteleme yapmak istediğimizde ise;
    #sql="select products.name,products.price,categories.name from products inner join categories on products.category_id=categories.id where categories.name='name'"
##categories tablosunun name=telefon olanların bilgilerini getir.


##tabloları isimlendire biliriz örneğin categories>>c , products >> p yapalım.
    sql="select p.name,p.price,c.name from products as p inner join categories as c on p.category_id=c.id where c.name='telefon'"

    mycursor.execute(sql) 
    try:
        result=mycursor.fetchall()

        for product in result:
            print(product)
    except mysql.connector.Error as err:
        print('hata: ',err)
    finally:
        mydb.close()

getProducts()