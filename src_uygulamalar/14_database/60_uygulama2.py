import mysql.connector
from datetime import datetime

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="a_002209",
    database="schooldb"
)

mycursor=mydb.cursor()

sql=("INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) values(%s,%s,%s,%s,%s)")
ogrenciler=[
    ("2204","fatih","ibiç",datetime(1991,10,7),"E"),
    ("2077","naim", "akın",datetime(1991,5,27),'E')
]

mycursor.executemany(sql,ogrenciler)

try:
    mydb.commit()
    print('{} tane kayıt eklendi.'.format(mycursor.rowcount))
except mysql.connector.Error as err:
    print("hata: ",err)
finally:
    print("kayıt işleminiz yapıldı.")
    mydb.close()


###### nesneye yönelik şekilde yapmak istersek; 61_uygulama_devam.py a bak