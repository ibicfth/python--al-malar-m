# istenilen miktarda parayı bakiyeden yetmezse ekhesaptan çeken program

fatihhesap={
    'ad':'fatih ibic',
    'hesapno':'1234697',
    'bakiye':3000,
    'ekhesap':2000,
}

alihesap={
    'ad':'ali kamıs',
    'hesapno':'1234697',
    'bakiye':2000,
    'ekhesap':1000,
}

def paracek(hesap, miktar):
    print(f"hoşgeldiniz sayın {hesap['ad']} ")

    if (hesap['bakiye']>=miktar):
        hesap['bakiye'] -= miktar
        print(f"paranızı alabilirsiniz.")
    else:
        toplam = hesap['bakiye'] + hesap['ekhesap']

        if (toplam>=miktar):
            ekhesapkullanimi=input('ek hesap kullanılsın mı: (e/h)')

            if ekhesapkullanimi=='e':
                ekhesapcekim = miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekhesap'] -= ekhesapcekim
                print('paranızı çekebilirisiniz')
            else:
                print(f"{hesap['hesapno']} lu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüz bakiyeniz yetersiz')


#uygulama kodu
paracek(alihesap, 2000)


