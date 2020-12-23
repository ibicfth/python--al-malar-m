while True:
    try: 
        x=int(input('x: değeri giriniz: '))
        y=int(input('y: değeri giriniz: '))
        print(x/y)
    except Exception as a:   #>>>>> deger yanlış olduğu müddetce while tekrardan deger ister.
        print(f'yanlıs deger girdiniz.hata: {a}')

    else:  # degerler doğru girildiinde program print i yazdırır ve döngüden çıkar
        break

    finally:         #>>>>>>>>>> hem except hemde else durumunda çalışır. 
        print('finally her durumda çalışır')


########################################################

# KENDİMİZ HATA OLUŞTURUP İSTENMEYEN DURUMLARI ÖNLEME

# paralo için istemediğimiz durumları belirledik ve hata mesajları oluşturduk.
#while döngüsüylke hata kullanıcıdan aldırdığımız parolayı doğru olana kadar programı çevirdik.

def passwordCkeck(psw):
    import re
    if len(psw)<7:
        raise Exception('parola en az 7 karakter olmalıdır.')

    elif not re.search("[a-z]",psw):
        raise Exception('parola küçük harf içermelidir.')

    elif not re.search("[A-Z]",psw):
        raise Exception('parola büyük harf içermelidir.')

    elif not re.search("[0-9]",psw):
        raise Exception('parola rakam içermelidir')

    elif not re.search("[$_@]",psw):
        raise Exception('parola alfa numeric karakter içermelidir')

   


while True:
    password=input('parola giriniz: ')
    try:
        passwordCkeck(password)   # try passwordCheckten gelen raise olursa hata algılar ve except: 'te gönderir.

    except Exception as ex:
        print(ex)

    else:
        print('uygun parola girdiniz')
        break

    finally:
        print('bura her durumda çalışır.')


##################################################################################
