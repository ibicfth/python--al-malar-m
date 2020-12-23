# isim=input('isminizi giriniz: ')
# yas=float(input('yaşınızı giriniz: '))
# egitimm_durumu=input('eğitim durumunuz: ')

# hak=yas>=18 and (egitimm_durumu=='lise'  or egitimm_durumu=='üniversite')

# if hak:
#     print(f'sayın {isim} ehliyet alma hakkınız vardır.')
# else:
#      print(f'sayın {isim} ehliyet alma hakkına sahip değilsiniz.')

# yazili1=float(input('yazılı1 giriniz: '))
# yazili2=float(input('yazılı2 giriniz: '))
# sözlü1=float(input('sözlü giriniz: '))
# ort=(yazili1+yazili2+sözlü1)/3

# if 85<= ort and ort <=100:
#     print(f'not ortalamanız {ort} ve geçme notunuz: {5}')
# elif 70<= ort and ort <=84:
#      print(f'not ortalamanız {ort} ve geçme notunuz: {4}') 
# # elif 55<= ort and ort <=69:
#      print(f'not ortalamanız {ort} ve geçme notunuz: {3}')       
# elif 45<= ort and ort <=54:
#      print(f'not ortalamanız {ort} ve geçme notunuz: {2}')
# elif 25<= ort and ort <=44:
#      print(f'not ortalamanız {ort} ve geçme notunuz: {1}')
# else  :
#      print(f'not ortalamanız {ort} ve geçme notunuz: {0}')

import datetime
# suan=datetime.datetime.now()
# tarih=input('aracınızın trafiğe çıkış tarihini 2020/12/30 formatında giriniz: ')

# tarih=tarih.split('/') # bir dizi haline getirir.

# trafik_cıkıs=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
## kendimiz tarih verdik
# trafik_durumu=suan-trafik_cıkıs
# print(trafik_durumu)

# gün=trafik_durumu.days

# if gün<=365:
#     print(f'1. servis aralığındasınız ')
# elif gün>365 and gün<=365**2:
#     print(f'2. servis aralığındasınız ')
# elif gün>365**2 and gün<=365**3:
#     print(f'3. servis aralığındasınız ')   
# else :
#     print(f'tarihi yanlış girdiniz ')

