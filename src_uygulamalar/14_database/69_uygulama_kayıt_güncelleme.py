import mysql.connector

## id ye göre alınan bir öğrenci bilgilerini güncelleme;

class Ogrenci:
    mydb_connector=mysql.connector.connect(host='localhost',user='root',password='a_002209',database='schooldb')
    mycursor=mydb_connector.cursor()
    def __init__(self,id,studentnumber,name,surname,birthdate,gender):
        if id is None:
            self.id=0
        else:
            self.id=id
        self.StudentNumber=studentnumber
        self.Name=name  
        self.Surname=surname
        self.Birthdate=birthdate
        self.Gender=gender

    @staticmethod
    def getStudent(id):
        sql="select * from student where id=%s"
        values=(id,)
        Ogrenci.mycursor.execute(sql,values)
        
        

        try:
            
            ##''' return Ogrenci.mycursor.fetchone() ''' 
            ##yerine
            gelen=Ogrenci.mycursor.fetchone()
            return Ogrenci(gelen[0],gelen[1],gelen[2],gelen[3],gelen[4],gelen[5])
##yapabiliriz. bu sayade Student clasını çağırırken parametre girmemize gerek kalmaz.
        except mysql.connector.Error as err:
            print('hata :', err)
        # finally: ##mydb_connect örü klass seviyesinde yaptık eğer her sınıf bitiminde kapatırsak sınıf  tekrar çağrıldığında yada bir sonraki sınıf çağrıldığında connection bağlı olmadığından hata verir.
        #     Ogrenci.mydb_connector.close()

    def updateStudent(self):
        sql="UPDATE student SET StudentNumber=%s, Name=%s, Surname=%s,Birthdate=%s,Gender=%s where id=%s"
        values=(self.StudentNumber,self.Name,self.Surname,self.Birthdate,self.Gender,self.id)
        Ogrenci.mycursor.execute(sql,values)

        try:
            Ogrenci.mydb_connector.commit()
            print(f"{Ogrenci.mycursor.rowcount} tane kayıt güncellendi..")
        except mysql.connector.Error as err:
            print('hata: ',err)
        # finally:##mydb_connect örü klass seviyesinde yaptık eğer her sınıf bitiminde kapatırsak sınıf  tekrar çağrıldığında yada bir sonraki sınıf çağrıldığında connection bağlı olmadığından hata verir.
        #     Ogrenci.mydb_connector.close()

# '''gelen=Ogrenci.getStudent(2) ##id=2 olan kayıtları getirir.''' ## artık 
# update=Ogrenci.getStudent(2) ## getirebiliriz.

# ##bu id=2 deki kayıtların updateStudent ile veri tabanına yazdırma için Ogrenci klasına veririz.
# '''update=Ogrenci(gelen[0],gelen[1],gelen[2],gelen[3],gelen[4],gelen[5])'''
# ## getStudend sınıfında bı kısmı Ogrenci kalsına otomatik gönderdiğimizden burda parametre vermeye gerek kalmadı, alternatif!
# ##burada clasa zaten içinde olan  verileri getirtip geri yolladık şimdi ise
# ##def__init__ teki değişkenleri değiştirip update yaptıralım ;

# update.Name='kalemi' ##Ogrenci klassının Name mini değiştirdik(self.Name=''kalem)
# update.Surname='bitti'

# ##şimdide yaptığımız değşikliği database yazdıralım;
# update.updateStudent()

#########################################################################################

###Eğer çoklu update yapmak istersek liste halinde;
## gender e göre update yaptıralım

    @staticmethod
    def getStudents(gender):
        sql="select * from student where Gender=%s"
        values=(gender,)
        Ogrenci.mycursor.execute(sql,values)
        
        

        try:
            
            return Ogrenci.mycursor.fetchall()  
          
        except mysql.connector.Error as err:
            print('hata :', err)

    @staticmethod
    def updateStudents(liste):
        sql="UPDATE student SET StudentNumber=%s, Name=%s, Surname=%s,Birthdate=%s,Gender=%s where id=%s"
##        values=liste ##listede gelecek ilk eleman id elemanı ama sql de id en sonda gelsin istiyoruz bunun için;
        values=[]
        sırala=[1,2,3,4,5,0] ## liste elemanlarının indexlerinin nasıl sıralanmasını istiyorsak ona göre
        for item in liste:
            item=[item[i] for i in sırala] ##liste elemanlarının indexlerini sırala dizisine göre getiri.
            values.append(item)  
        
        Ogrenci.mycursor.executemany(sql,values) ##çoklu listede executemany kullaılır.

        try:
            Ogrenci.mydb_connector.commit()
            print(f"{Ogrenci.mycursor.rowcount} tane kayıt güncellendi..")
        except mysql.connector.Error as err:
            print('hata: ',err)

students=Ogrenci.getStudents('K') ## kızların olduğu bir liste gelir.
##not students listesinin her bir elemanı tuple olan bir listedir ancak;
## tuple listesindeki bir elemanı değiştirme durumu söz konusu değil ya tuple baştan tanımlamak lazım,
##yada gelen her bir gelen tuple liste elemanını listeye cevirmek lazım
##yani tuple=(a,b,c,d,e) >>list(tuple) >>> tuple=[a,b,c,d,e] yapalım

liste=[]
for st in students: #students listesinin tuple olan her bir elemanını getiririz..
    st=list(st)  ## tuple lı listeye çeviririz
    st[2]='Ms' + st[2]## biz 2. indexte olan name leri değiştirmek istiyoruz
    liste.append(st)

Ogrenci.updateStudents(liste) ## oluşturduğumuz listeyi toplu güncelleme yapacağımız updateStudents sınıfına yolluyoruz.