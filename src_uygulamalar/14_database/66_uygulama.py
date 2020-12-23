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
# ogrenciler=[
#     ("2214","fatihx","ibiç",datetime(1991,10,7),"E"),
#     ("2017","naimx", "akın",datetime(1991,5,27),'E')
# ]
# Ekleme.students_ekleme(ogrenciler)

mycursor=mydb.cursor()

##soru: 1 tüm öğrenci kayıtlarını alınız.
# mycursor.execute('select * from student')
# result=mycursor.fetchall()

# for st in result:
#     print(st)

##soru: 2 tüö öğrencilerin no,ad,soyadını alnız sadece.
# mycursor.execute('select * from student')
# result=mycursor.fetchall()

# for st in result:
#     print(st[1],st[2],st[3])

##yada
# mycursor.execute('select StudentNumber,Name,Surname from student')
# result=mycursor.fetchall()
# for st in result:
#     print(st)

##soru 3 sadece kız öğrencilerin ad ve soyadılarını bulunuz.
# mycursor.execute("select Name,Surname from student where Gender='K'")
# result=mycursor.fetchall()
# for st in result:
#     print(st)

##soru 4 2003 doğumlu öğrenci bilgilerini alınız
# mycursor.execute("select * from student where Birthdate like '2003%'")
# result=mycursor.fetchall()
# for st in result:
#     print(st)


##soru 5 ismi fatih ve doğum tarihi 1991 olan öğrenci bilgileri
# mycursor.execute("select * from student where Name='fatih' and Birthdate like '1991%'")
# result=mycursor.fetchall()
# for st in result:
#     print(st)

##soru 6 adı veya soyadı içinde ne geçen kişileri listeleyiniz.
# mycursor.execute("select * from student where Name like '%ne%' or Surname like '%ne%' ")
# result=mycursor.fetchall()
# for st in result:
#     print(st)

##soru 7 kaç erkek öğrenci vardır.
# mycursor.execute("select count(*) from student where Gender='E'")
# result=mycursor.fetchall()
# print(result)

##soru 8 kız öğrencileri harf sırasına göre getiriniz.
mycursor.execute("select * from student where Gender='K' order by Name,Surname")
result=mycursor.fetchall()
for st in result:
    print(st)