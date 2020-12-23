import random
value=random.randint(0,100)
print(value)

hak=5
puan=100
can=1
sayac=0

while can<=5:
    can+=1
    sayac+=1
    tahmin=int(input('lütfen tahmininizi giriniz: '))
    
    if tahmin==value:
        print(f'tebrikler bildiniz. puanınız {puan-(sayac-1)*20}')
        break
    
    elif tahmin<value:
        print('lütfen daha yüksek tahminde bulunun: ')
        
    else :
        print('lütfen daha düşük tahminde bulunun: ')

    if can==6:
        print('maalesef hakkınız kalmadı lütfen tekrar deneyin')



