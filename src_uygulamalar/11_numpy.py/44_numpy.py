import numpy as np

## 1
result=np.array([10,15,30,45,60])
print(type(result))

##2

result=np.arange(5,15,1)

##3
result=np.arange(5,100,5)

##4
result=np.zeros(10)

##5
result=np.ones(10)

##6
result=np.linspace(0,100,5) ##0 ile 100 ü 5 eşitparçaya böler

##7
result=np.random.randint(10,30,5)

##8
result=np.random.randint(-1,1,10)

##9
dizi=np.random.randint(10,50,15)
matris=dizi.reshape(3,5)  ##3x5 matris

##10
toplam=matris.sum(axis=1)  ##satırların toplamı
print(toplam)

toplam=matris.sum(axis=0) ##sütunların toplamı
print(toplam)

##11
enbüyük=matris.max()
print(enbüyük)

enkücük=matris.min()
print(enkücük)

ortlama=matris.mean()  ##ortalama verir
print(ortlama)

##12
index=matris.argmax()
print(index)

##13
dizi=np.arange(10,20)
result=dizi[:3]  #ilk 3 elemanı

##14
result=dizi[::-1]

##15
ilksatir=matris[0]
print(ilksatir)

##16
kl=matris[1,2]  ## matrisin 2. satır 3.sütundaki elemanı
print(kl)
print(matris)

##17
ilkeleman=matris[0:3,0]  ##matrisin 0 dan 3 e kadar olan satırının her birinin ilk elemanını, 
print(ilkeleman)

##18
kare=matris**2
print(kare)
    
##19
numpyy=np.random.randint(-50,50,15)
matris2=numpyy.reshape(3,5)
print(matris2)
cift=matris2[matris2 % 2 ==0]  ##matrisin çift olanları turu olur ve sonra matrisden true olan indeksleri getirir.
sonuc=cift[cift>0] ##çiftler matrisinin elemanılarının 0 dan büyüyk olanlar true olur ve true olan indekxleri sonuc matris yapar

print(sonuc)