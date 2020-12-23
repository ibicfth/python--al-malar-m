sayı=int(input('sayı giriniz: '))

# result=(sayı>0) and (sayı<100) #true yada false üretir
# print(result)
# print(f'girdiğiniz sayı 0 ve 100 arasında mıdır: {result}')

# result=(sayı>0) and (sayı % 2 == 0)
# print(f'girdiğiniz sayı pozitif ve çift mıdır: {result}')

# email='fth.ibic@gmail.com'
# parola=1234

# kemail=input('email giriniz: ')
# kparola=int(input('parola giriniz: '))

# sonuc=(kemail == email) and (kparola == parola)
# print(f'girdiğiniz parola ve email  doğru mudur: {sonuc}')


# sayı1=int(input('sayı giriniz: '))
# sayı2=int(input('sayı giriniz: '))
# sayı3=int(input('sayı giriniz: '))

# sonuc1=(sayı1 > (sayı2 and sayı3))
# sonuc2=(sayı2 > (sayı1 and sayı3))
# sonuc3=(sayı3 > (sayı2 and sayı1))

# print(f'sayı1 en büyük sayımıdır {sonuc1} \n sayı2 en büyük sayımıdır {sonuc2} \n sayı3 en büyük sayımıdır {sonuc3}')

# vize1=int(input('vize1 giriniz: '))
# vize2=int(input('vize2 giriniz: '))
# final1=int(input('final1 giriniz: '))

# ortalama=(((vize1+vize2)/2)*0.6 +final1*0.4)
# sonuc=(ortalama >= 50) and (final1>=70)

# print(f'dersten geçme durumunuz: {sonuc}')

ad=input('adınızı giriniz: ')
kilo=float(input('kilonuzu giriniz: '))
boy=float(input('boyunuzu giriniz (metre olarak): '))

formül=(kilo/(boy**2))

zayıf=(0 <= formül) and (formül<= 18.4)
normal=(18.5 <= formül) and (formül <= 24.9)
fazla_kilolu=(25 <= formül) and (formül <= 29.9)
sisman=(30 <= formül) and (formül <= 34.9)


# print(f'zayıf olma durumunuz: {zayıf}')
# print(f'normal olma durumunuz: {normal}')
# print(f'fazla kilolu olma durumunuz: {fazla_kilolu}')
# print(f'şişman obez olma durumunuz: {sisman}')

if zayıf ==True:
    print(f'sayın {ad} kilo değerlendirmeniz zayıf olarak hesapanmıştır. {formül} ')

elif normal==True:
    print(f'sayın {ad} kilo değerlendirmeniz normal olarak hesapanmıştır. {formül} ')

elif fazla_kilolu==True:
    print(f'sayın {ad} kilo değerlendirmeniz fazla kilolu olarak hesapanmıştır. {formül} ')

else:
    print(f'sayın {ad} kilo değerlendirmeniz şişman olarak hesapanmıştır. {formül} ')

