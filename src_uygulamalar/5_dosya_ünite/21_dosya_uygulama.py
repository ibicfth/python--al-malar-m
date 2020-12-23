# UYGULAMA ##
def notbul(satir):
    satir = satir[:-1]
    liste = satir.split(':') # satırı : ikiye böler.yani satır iki elemanlı olur. isim ve notlar
    ogrenci_adi=liste[0]
    notlar=liste[1].split(',')

    
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])

    ortalama=(not1+not2+not3)/3

    if ortalama>=90 and ortalama<=100:
        harf='AA'
    elif ortalama>=85 and ortalama<=89:
        harf='BA'
    elif ortalama>=75 and ortalama<=84:
        harf='BB'
    elif ortalama>=65 and ortalama<=74:
        harf='CB'
    elif ortalama>=55 and ortalama<=64:
        harf='CC'
    else:
        harf='ff'

    return ogrenci_adi+' '+'ortalama: '+harf+"\n"



def ortalamalari_oku():
    with open('sinav_kayitlari.txt', 'r', encoding='utf-8') as file:
        for satir in file:
            print(notbul(satir))
            
            
def not_gir():
    ad=input('öğrenci adı: ')
    soyad=input('öğrenci soyadı: ')
    not1=input('öğrencinin 1.notu: ')
    not2=input('öğrencinin 2.notu: ')
    not3=input('öğrencinin 3.notu: ')

    with open('sinav_kayitlari.txt', 'a', encoding='utf-8') as file:
        file.write(ad+' '+soyad+' : '+not1+','+not2+','+not3+'\n')

def notlari_kayıtet():
    with open('sinav_kayitlari.txt', 'r', encoding='utf-8') as file:
        liste=[]
        for i in file:
            liste.append(notbul(i))

        with open("sonuclarim.txt",'w',encoding='utf-8') as file2:
            for i in liste:
                file2.write(i)


while True:
    islem=input('1- notları oku \n2- notları gir \n3- notları kayıt et \n4- çıkış \n')

    if islem=='1':
        ortalamalari_oku()
    elif islem=='2':
        not_gir()
    elif islem=='3':
        notlari_kayıtet()
    else:
        break