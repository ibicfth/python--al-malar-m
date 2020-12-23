# names=['ali','veli','deli']
# for x in names:
#      print(f"my names is {x}")
    

# tuple=(1,2,3)

# for x in tuple:
#     print(x)

# tuple=[(1,2),(3,4),(5,6)]

# # for item in tuple:
# #     print(item)

# for x,y in tuple:
#     print(x,y)

# name={'k1':1,'k2':2,'k3':3}
# for item in name:    ## sadece key değerleri gelir.
#      print(item)

# for x in name.items():  ## hem key hemde value değerleri gelir.
#      print(x)

# for x,y in name.items():   ## hem key hem value değerleri gelir.
#      print(x,y)

# UYGULAMA

sayilar=[1,3,5,7,9,12,19,21]
kat=[]
# for x in sayilar:  3 ün katını bulup kat dizisine ekler.
#     if x % 3==0:
#         kat.append(x)

# print(kat)
####################################################################
# toplam=0              ## sayilar dizisindeki elemanların toplamı
# for x in sayilar:
#     toplam +=x

# print(toplam)
##################################################

# kare=[]            ## tek sayıların karesini alır.
# for x in sayilar:
#     if x % 2 !=0:
#         kare.append(x**2)

# print(kare)
###################################################

# sehirlerden hangisi en fazla 5 karakterlidir.
sehirler=['kocaeli','istanbul','ankara','izmir','rize']

# istenen=[]
# for x in sehirler:
#     if len(x)<=5:
#         istenen.append(x)

# print(istenen)
###########################################################

# #ürün fiyatlarını toplar.
# urunler=[
#     {'name':'samsung s6','price':'3000'},
#     {'name':'samsung s7','price':'4000'},
#     {'name':'samsung s8','price':'5000'},
#     {'name':'samsung s9','price':'6000'},
#     {'name':'samsung s10','price':'7000'},
# ]

# toplam=[]
# sonuc=0
# for x in urunler:
#     toplam.append(int(x['price']))
# 
# for y in toplam:
#     sonuc += y
# print(sonuc)
    
# ###############################################

# # fiyatı en fazla 5000 olan ürünleri gösterir.
# istenen=[]
# for x in urunler:
#     if int(x['price'])<=5000:
#         istenen.append(x)


# print(istenen)

# ##############################################
