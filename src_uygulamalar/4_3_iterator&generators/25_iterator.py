##not: iter() metodu sadece iter'i destekleyen class larda çalışır ve liste class'ları destekler.
## iter ile oluşturulan obje next methodu  ile çağrılır.
liste=[1,2,3,4,5]
x=iter(liste)

print(next(x)) #listenin sadece bi çevrimde 0. indexini getirir.ve sonraki indexte bekler
#listenin sonraki elemanı için tekrar next() methodu ile çağırmamız gerekli.
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# listede 5 eleman var. next methodu 5. elemanı yazdıktan sonra tekrar çağrılırsa hata verir.
#print(next(x)) # 6. eleman olmadığından hata verir.


#gelelim for döngüsünün  çlaışma mantığına
liste2=['a','b','c','d']
x=iter(liste2)
while True:
    try:  ## break olmadığı müddetçe tekrar döner.
        
        print(next(x))
    except StopIteration: # başka eleman kalmadığında next hata verir ve except kısmında break komutuyla döngüden çıkılır.
        break
##########################################################
## kendimiz belirlediğimiz iki sayı arasındaki sayılardan dizi yapma:
class listeOlustur:
    def __init__(self,first,last):
        self.first=first
        self.last=last

    def __iter__(self):
        return self

    def __next__(self):
        if self.first<=self.last:
            x=self.first
            self.first+=1
            return x
        
        else:
            raise StopIteration

liste=listeOlustur(15,35)
print(liste) ##sadece adres verir.
for x in liste:
     print(x)
