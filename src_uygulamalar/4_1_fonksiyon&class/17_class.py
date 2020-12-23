# #CLASS
# class Person :
#     addres='no information'
    
#     # attribute 2'ye ayrılır.
#     #class attribute


#     #object attribute buda yapıcı method sayesinde yapılır(constructure method)
#     #constructure method
#     def __init__(self, name, year) :
#         self.name=name
#         self.year=year
#         print('init methodu çalıştı.')


    
#         # methotlar 
#     def intro(self) :
#         print('hello there')

#     def calcularage(self):
#         return 2019-self.year
# #OBJECT(İNSTANCE)
# p1=Person('fatih',1991)

# print(f"kullanıcı name: {p1.name} ,yılı: {p1.year} , )
# p1.intro()
# print(p1.calcularage())
#############################################################################
# class Circle:
#     pi=3.14
#     def __init__(self, yarıcap=1): #yarıcap otomatik tanımlanan bir değeri
#         self.yarıcap=yarıcap

#     #method
#     def daire_cevre(self):
#         return 2*self.pi*self.yarıcap

#     def daire_alan(self):
#         return self.pi*self.yarıcap**2


# c1=Circle() # parametre verilmediğinde otomatik tanımlanan bir değeri atanır.
# c2=Circle(5)

# print(c1.daire_cevre(), c1.daire_alan())
# print(f"cevre { c1.daire_cevre()}, alan {c1.daire_alan()}")
##############################################################################
# KALITIM
class Person():
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        print ('person created')
    
    def who_i_am(self):
        print('i am person')

class Student(Person):
    def __init__(self, fname, lname, number): #Person clasının init metodunu ezer. bunu aşmak için;
        Person.__init__(self, fname, lname)  #person clasının içindeki methodu cağırız.
        self.number=number  #numberı sadece student te tanımladık ve 
        print('student created') #sadece student(person) olduğundan yani
                                # person(student) olmadığından paremetre personda geçerli değil.
p1=Person('ali','turan')
s1=Student('ali','turan',357)

print(p1.fname,p1.lname)
s1.who_i_am()
print(s1.number)

######################################################################
#OBJELER ÜZERİNDE ÖZEL  METODLAR
#def  __abc__():  şeklinde olur yani
class Deneme(): 
    def __init__(self,isim): #yazmanın özel metodu bu class içinde str nin nasıl yazılcağını belirler
        self.isim=isim
        
    # def __str__(self):
    #     return self.isim

a=Deneme('mehmet')   
print(f"deneme:{a}")
print(str(a))
print(a.isim)

##############################################################################

