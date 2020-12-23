from baglanti_kur import mydb ##baglanti_kur.py dan alır 
from datetime import datetime
import mysql.connector

class Ekleme:
    mydb=mydb ##oluşturacağımız bütün sınıfların içinde kullanamabilmek için;
## sınıf seviyesinde oluşturduk.çağırmak için sınnıf adıyla birlikte çağrılmalıdır.
# # aynı şekilde mycursor de oluşturualım;
    mycursor=mydb.cursor()     
    def __init__(self,studentnumber,name,surname,birthdate,gender):
        self.studentnumber=studentnumber
        self.name=name
        self.surname=surname
        self.birthdate=birthdate
        self.gender=gender

    def student_insert(self):
      

        sql=("INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) values(%s,%s,%s,%s,%s)")
        ogrenciler=(self.studentnumber,self.name,self.surname,self.birthdate,self.gender)
          

        Ekleme.mycursor.execute(sql,ogrenciler)

        try:
            mydb.commit() 
            print('{} tane kayıt eklendi.'.format(Ekleme.mycursor.rowcount))
        except mysql.connector.Error as err:
            print("hata: ",err)
        finally:
            print("kayıt işleminiz yapıldı.")
            mydb.close()


##student_insert gibi instance method değil yani __init__ den parametre almaz, 
##bu sebeple bu sınıfı oluştururken self parametre olarak kullanılmaz.içten bişey almaz
##dışardan parametre alır sadece. aşağıda staticmethod oluşturduk.
    @staticmethod 
    def students_ekleme(ogrenciler):

        sql=("INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) values(%s,%s,%s,%s,%s)")
        values=ogrenciler
        Ekleme.mycursor.executemany(sql,values)

        try:
            mydb.commit()
            print(f"{Ekleme.mycursor.rowcount} adet kayıt eklendi.")
        except mysql.connector.Error as err:
            print("hata: ",err)
        finally:
            print("kayıt işleminiz gerçekleştirilmiştir.")
            mydb.close()


## tek bir kayıt eklemek için;
# hasan=Ekleme("721","hasan","dündar",datetime(1992,10,7),"E")
# hasan.student_insert()

##çoklu kayıt eklemek için;
ogrenciler=[
    ("2214","fatihx","ibiç",datetime(1991,10,7),"E"),
    ("2017","naimx", "akın",datetime(1991,5,27),'E')
]

Ekleme.students_ekleme(ogrenciler)