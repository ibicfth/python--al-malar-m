sayi=int(input('sayı giriniz: '))
isdurum= True


if sayi==1:
    isdurum=False

for x in range(2,sayi):

    if ((sayi % x)==0):
        isdurum=False
        break
    
#print (dizi)
if isdurum:
    print('sayı asal sayıdır.')
    
else:
    print('sayı asal sayı değildir.')


    