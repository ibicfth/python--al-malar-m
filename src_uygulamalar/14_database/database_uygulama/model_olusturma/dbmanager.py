import mysql.connector
from datetime import datetime
from baglanti_kur import mydb
from student import Student
from teacher import Teacher
from Class import Class
class DbManager:
    def __init__(self):
        self.connection=mydb
        self.cursor=self.connection.cursor() #(connection yerine mydb yazmak gerekebilir)
      

    def getStudentById(self,id):
        sql="select * from student where id=%s"
        values=(id,)
        self.cursor.execute(sql,values)
        try:
            obj=self.cursor.fetchone()
            #return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])
            return Student.CreateStudent(obj)
        except mysql.connector.Error  as err:
            print("error: ",err)

    def getClasses(self):
        sql="select * from class"
        
        self.cursor.execute(sql)
        try:
            obj=self.cursor.fetchall()
            
            return Class.CreateClass(obj)
           
        except mysql.connector.Error  as err:
            print("error: ",err)
    def getStudentsByClassId(self,classid):
        sql="select * from student where ClassId=%s"
        values=(classid,)
        self.cursor.execute(sql,values)
        try:
            obj=self.cursor.fetchall()
         
            return Student.CreateStudent(obj)
            #return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])
        except mysql.connector.Error  as err:
            print("error: ",err)

    def addStudent(self,student: Student):
        sql=("INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) values(%s,%s,%s,%s,%s,%s)")
        values=(student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid)
        
        self.cursor.execute(sql,values)

        try: 
            self.connection.commit()
            print(f"{self.cursor.rowcount} adet kayıt eklendi.")
        except mysql.connector.Error as err:
            print("hata: ",err)
        finally:
            print("kayıt işleminiz gerçekleştirilmiştir.")
            

    def editStudent(self,student: Student):
        sql=("UPDATE student SET StudentNumber=%s, Name=%s, Surname=%s, Birthdate=%s, Gender=%s, ClassId=%s where id=%s ")
        values=(student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid,student.id)
        
        self.cursor.execute(sql,values)

        try: 
            self.connection.commit()
            print(f"{self.cursor.rowcount} adet kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("hata: ",err)
        finally:
            print("kayıt işleminiz gerçekleştirilmiştir.")
    def addTeacher(self,teacher: Teacher):
        pass

    def aditTeacher(self,teacher: Teacher):
        pass

   




    # def __del__(self):  ##görmüyor
    #     self.connection.close()
    #     print('db kapandı.')

db=DbManager()

# student= db.getStudentById(7) ## objenin elemanını çağırırken
# print(student.name)

##alternatif

# student= db.getStudentById(7)
# print(student[0].name)  ##liste içinden eleman çağırırken

## classid kolonuna göre getirmek iin;
#students=db.getStudentsByClass(1)

##kayıt eklemek için;
#öncelikle tek tek 7 elemanı vermek yerine hazır kayıtı getirip bir yerini değiştiripi 
#ekleme yapalım

# student=db.getStudentById(1)
# student[0].name="değistir"
# student[0].studentNumber="7789"

# db.addStudent(student[0]) ##yukarıda çağrılıp değştirilen satırı database e ekler.


##yeni satır ekleme değilde sadece güncelleme yapmak için;

student=db.getStudentById(12)  ## bu şuan bir liste ve içinde de tuple listesi var liste=[(),()]
student[0].name="mehtapı"  ##sadece id=12 olan tek bir tuple elemanı olduğundan sıfır olmalı

db.editStudent(student[0])