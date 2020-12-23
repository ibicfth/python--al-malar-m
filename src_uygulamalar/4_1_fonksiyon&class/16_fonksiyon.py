# istenen kelimeyi istenen adette yazma.

# def yaz(kelime, kackez):
#     x=1
#     while (x <= kackez):
#         print(kelime)
#         x+=1

# yaz('nasilsin', 9)

#yada

# def yazdir(kelime, adet):
#     print(kelime*adet)

# yazdir('nasilsin\n', 9)

#################################################### 
# gönderilen parametreleri liste içerisine atma
#def listeyecevir(*params):
#     liste=[]
#     for param in params:
#         liste.append(param)
#     return liste

# sonuc=listeyecevir(10,20,'adam',75,'kardes')
# print(sonuc)
####################################################
# ARADAKİ ASAL SAYILARI BULMA
# sayı1=int(input('1.sayıyı giriniz: '))
# sayı2=int(input('2.sayıyı giriniz: '))

# def asalbul(sayı1, sayı2):
#     for aradakisayilar in range(sayı1, sayı2+1): # sayı2 yide alması için +1 dedik
#         if aradakisayilar>1:
#             for i in range(1, aradakisayilar):
#                 if (aradakisayilar% i)==0):
#                     break

#             else:
#                 print(aradakisayilar)

# #uygulaması
# asalbul(sayı1,sayı2)

#####################################################
#The program that lists the divisors of a number
#kendisine gönderilen sayinin tam bölenlerini liste haline getiren
sayi=int(input('sayı giriniz: '))

def tambölenler(sayi):
    liste=[]
    for x in range(1,sayi+1):
        if (sayi % x==0):
            liste.append(x)
    return liste

#
# uygulama cagirma
a=tambölenler(sayi)
print(a)