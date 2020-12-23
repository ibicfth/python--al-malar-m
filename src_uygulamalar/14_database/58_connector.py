import mysql.connector 


##### database ile bağlantı kur #######
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="a_002209"
    
# )

#print(mydb)

###################################
##kendimiz bi databae oluşturmak için;
#mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")  ## 2 kere çalıştırmak hata verdirir.oluşan data base bir daha oluşutulamaz

## server daki database leri görüntülemek için;
#mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#  print(x)

###################################################################################
## şimdi bi database bağlanıp tablo oluşturalım.
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="a_002209",
    database="mydatabase" ##yukarda oluşturduğumuz database te işlem yapacağız
)

mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255))")