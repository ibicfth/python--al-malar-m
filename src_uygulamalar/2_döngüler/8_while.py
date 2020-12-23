
# x=1                   çalışmaz çünkü sayaç doğru yerde değil ve
# while x <= 100:       program if içine giremiyor. sayacı if döngüsünün
#     if x %2 ==0:      dışında yaz.sayac if e değil while a ait.
#         print(x)
#         x=x+1
# print('bitti..')
##############################################################
# x=1                   #üsttekini doğrusu
# while x <= 100:
#     if x %2 ==0:
#         print(x)
#     x=x+1


# print('bitti..')
###############################################################
# x=1                   sayac doğru yerde çalışır.
# while x <= 100:
#     if x %2 ==0:
#         print(x)
#     x=x+1 


# print('bitti..')

###########################################################

# # x=1                     sayac doğru yerde calısır.
# while x <= 100:
#     if x %2 ==0:
#         print(x)
#     x=x+1
# print('bitti..')

#UYGULAMA
#####################################
# sayilar=[1,3,5,7,9,12,19,21] #for kullanmadan while ile sayilar 
                                #dizisini ekrana yazdırma
# ekran=[]
# x=0
# while x <=(len(sayilar)-1):
#     ekran.append(sayilar[x])
#     x +=1

# print(ekran)
########################################################

# #while kullanarak verilen iki değer arasindaki tek sayiları yazidrma.
# ilk=int(input('ilk değeri giriniz: '))
# son=int(input('son değeri giriniz: '))

# x=ilk
# while x<=son:
#     while x%2 !=0:
#         print(x)
#         x +=1  # burada sadece tek olduğunda sayac sayar
#     x+=1  #burada çiftlerde sayac saymaya devam eder.
###############################################################
## while şart doğru olduğu müddetçe for döngüsü gibi döner
# x=5
# while x<= 10:
#     while x>0 and x<10:
#         print('iç while')
#         print(x)
#         x +=1
#     print('dış while')
#     print(x)
#     x +=1
###########################################################
# 1-100 arasındaki sayıları azalan olarak
# x=100
# while x>=0:
#     print(x)
#     x = x-1

##############################################################
# kullanıcıdan alınan 5 degeri kücükten büyüge siralar.
# a=[]
# x=1
# while x<=5:
#      b=int(input(f'{x} . değeri giriniz: '))
#      a.append(b)
#      x+=1
    
# a.sort()
# print(a)
######################################################
# ürün sayısına göre dizi oluşturup name ve price dictionary yapma
ürünsay=int(input('ürün sayısını giriniz: '))
x=1
ürünler=[]
while x<=ürünsay:
    b={'name':input('ürün adı giriniz: '),'price':int(input('fiyat giriniz: '))}
    ürünler.append(b)
    x += 1

print(ürünler)
#########################################################