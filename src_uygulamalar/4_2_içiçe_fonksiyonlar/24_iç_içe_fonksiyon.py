# def fatih(name):
#   print(f'hesap numaranız: {name} olarak tanımlandı.')

# fatih(1111)

# naim=fatih #artık naim  fonksiyon özelliği gösterir.
            
# ENCAPSULATİON

# def outer(num1):
#     print('dış fonksiyon')
#     def inner_increment(num1):
#         print('iç fonksiyon')
#         return num1 + 1
#     num2=inner_increment(num1) ## burda inner_increment() fonksiyonu çağrılmazsa outer sadece ('dış fonksiyonu')
#     print(num1,num2)            # çıktı olarak verir.Ayrıca iç içe fonksiyonu sadece içteki
# ##                                #fonksiyon çalıştırabilir.

# outer(10)


# #########################################
# ## içiçe fonksiyon ile faktoriyel hesaplama

# def factoriyel(number):
#     def inner_factroriyel(number):
#         if number<=1:
#             return 1
#         else:
#             return number*inner_factroriyel(number-1)
#     return inner_factroriyel(number)


# print(factoriyel(4))

# #################################################
# ## FONKSİYONDAN FONKSİYON DÖNDÜRME

# ##us alma ###########################
# def usalma(number):
#     def us_kuvveti(power):
#         return number**power
#     return us_kuvveti

# x=usalma(2) #buradan bize returnus_kuvveti yani us_kuvveti fonksiyonu döner.
# y=x(3)
# print(y)

# ###################################
# ## us alma gibi benzer bi uygulama 
# ## giriş yetkisi verme:

# def yetki_sorgulama(page):
#     def inner(rol):
#         if rol=='admin':
#             return'{0} rolü {1} sayfasına giriş hakkına sahiptir.'.format(rol,page)
#         else :
#             return'{0} rolü {1} sayfasına giriş hakkına sahip değildir.'.format(rol,page)
#     return inner

# x=yetki_sorgulama('sayfa yönetimi')
# y=x(input('rol giriniz: '))
# print(y)

# #############################################
# ###seçtiğimiz işleme göre inner fonksiyonunu çağıran program:
# def islemsec(islemadi):
    
#     def toplama(*args):
#         toplam=0
#         for i in args:
#             toplam += i
#         return toplam

    
#     def carpma(*args):
#         carpım=1
#         for i in args:
#             carpım *=i
#         return carpım
    
#     if islemadi=='toplama': ## verilen işlem adına göre carpma yada toplama fonksiyonlarını getirir.
#         return toplama      ## burada inner methodları(carpma ve toplama methodlarıdır)
#     else:
#         return carpma

# x=islemsec('toplama') # toplama yada çarpma fonksiyonlarını getirir.
# y=x(1,2,3,4)
# print(y)


####################################################################
## FONKSİYONLARI BAŞKA FONKSİYONLARA PARAMETRE OLARAK GÖNDERME

# def toplama(a,b):
#     return (a+b)

# def cikarma(a,b):
#     return (a-b)

# def carpma(a,b):
#     return (a*b)

# def bölme(a,b):
#     return (a/b)

# def islem(f1,f2,f3,f4,islem_sec):
#     if islem_sec=="toplama":
#         print(f1(2,3))
    
#     elif islem_sec=="cikarma":
#         print(f2(101,1))

#     elif islem_sec=="carpma":
#         print(f3(2,24))

#     elif islem_sec=="bölme":
#         print(f4(33,3))

#     else:
#         print('işlem girme hatası')

# islem(toplama,cikarma,carpma,bölme,'bölme')


#####################################################33
## DECORATOR FONKSİYONLARI
 

# def my_decorator(func):
#     def wrapper():
#          print('fonsiyondan önceki işlemler')
#          func() ##decorator(sayHello) olarak fonksiyonu çağırdığımızda burda sayHello() fonsiyonuna dönüşüyor.
#          print('fonksiyondan sonraki işlemler')

#     return wrapper

# def sayHello():
#     print('hello')

# x=my_decorator(sayHello) #>>x=wrapper()oldu. #bunu sayHello() fonsiyonunu üstüne @my_decorator yazarakta yapabiliriz.

# x()       

######################## yukardakini alternatifi
# def my_decorator(func):
#     def wrapper():
#          print('fonsiyondan önceki işlemler')
#          func() ##decorator(sayHello) olarak fonksiyonu çağırdığımızda burda sayHello() fonsiyonuna dönüşüyor.
#          print('fonksiyondan sonraki işlemler')

#     return wrapper

# @my_decorator   ##bu sayHello() fonksiyonunun sayHello söz dizimini my_decorator e parametre olarak yollar.
# def sayHello():
#     print('hello')

# sayHello()  ## yani sayHello() fonksiyonunu my_decorator un parametresi yapar.

##  ?? PEKİ YA sayHello() fonksiyonuna parametre vermek istersek, o zaman my_decoratorün 
## inner ı olan wrapper() a da o parametreyi tanımlamalıyız. tabiki func() a da tanımlamalıyız.
##yani:

# def my_decorator(func):
#     def wrapper(name):
#          print('fonsiyondan önceki işlemler')
#          func(name) ##decorator(sayHello) olarak fonksiyonu çağırdığımızda burda sayHello() fonsiyonuna dönüşüyor.
#          print('fonksiyondan sonraki işlemler')

#     return wrapper

# @my_decorator
# def sayHello(name):
#     print('hello',name)

# sayHello('ali')

# ###############################################
# ## örnek
# import math
# import time
# def hesaplat(func):
#     def getir(*args,**kwargs):
#         print('fonksiyondan önceki işlem')
#         start=time.time()
#         time.sleep(1)
#         func(*args,**kwargs)
#         finish=time.time()
#         print('fonksiyondan sonraki işlem')
#         print('sectiğiniz '+ func.__name__ +' '+ str(finish-start)+' sürede çalıştırıldı.')
#                          fonksiyonun adını yazar
#     return getir 

# @hesaplat
# def üsal(a,b):
#     print(math.pow(a,b))

# @hesaplat
# def factoriyelal(sum):
#     print(math.factorial(sum))
    
# üsal(2,9)
# factoriyelal(6)

