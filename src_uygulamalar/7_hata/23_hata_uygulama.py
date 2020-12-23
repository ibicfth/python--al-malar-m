liste=["1","2","5a","10b","abc","10","50"]

####liste içindeki sayısal degerleri bulunuz
sayısaldegerler=[]
for x in liste:
    try:
        a=int(x)
    except Exception:
        continue
    else:  #hata vermediğinde çalışan kısım.
        sayısaldegerler.append(x)
    
print(sayısaldegerler)

#yada
for x in liste:
    try:
        a=int(x)
        print(a)
    except Exception:
        continue

######################################################
### q girilmedikce girilen sayıların integer olup olmadığına bakan program

while True:
    a=input('veri giriniz: ')
    if a == 'q' or a== 'Q':
       break
       
    try:
        b=float(a)
        print(f"girdiğiniz sayı integer {a}")
    except Exception as ex:
        print(f'girdiginiz deger integer değil hata:{ex}')




###########################################################
### girilen parola içinde türkçe karakter hatası bulunuz.

parola=input('parola giriniz: ')
            
def karakterSorgulama(k):
    import re
    if re.search("[ıİçÇöÖüÜŞş]",k):
      raise Exception('türkçe karakter kullanamazsınız!')    
    else:
        print('geçerli parola')


try:
    karakterSorgulama(parola)

except Exception as ex:
    print(f"hata: {ex}")


######################################################


