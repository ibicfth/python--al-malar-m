#import datetime  # bütün classlar gelir
from datetime import datetime #sadece datetime classını import edebiliriz
# from datetime import date  # sadece date clasını import edebiliriz


#sonuc=dir(datetime) # modül içindeki klasları cağırır.

simdi=datetime.now() # now ın içinde yıl ay gün  saat saniye ve salise vardır. sadece birini çağırmak için
#simdi=datetime.now().year  #yada;
sonuc=simdi.year

sonuc=datetime.ctime(simdi) #simdi'yi biçimli yazar:  Mon Oct 19 19:54:11 2020  şeklinde
## aynı şekilde kenimizde foırmat belirleyebiliriz.
sonuc=datetime.strftime(simdi,'%Y') # sadece simdi() nin yıL bilgisini verir. büyük küçükdikkat
## '%X' saat, '%B':ay  bunları googlede datetime python die aratıp bulabiliriz.

t='21 nisan 2019' #string ifadeden ay gün yılı metdot bilip çekemez. bunu bölüp çekebiliriz
gun, ay, yıl=t.split(' ')
print(gun)
print(ay)
print(yıl)

## yada;
t='21 June 2019 hour 10:12:30' #burası ing olmak zorunda;
sonuc=datetime.strptime(t, '%d %B %Y hour %H:%M:%S') ##t stringini çözümler.
sonuc=sonuc.year

birthday=datetime(1991,10,7,5,5,5)
sonuc=datetime.timestamp(birthday) # bütün tarihi saniye cinsinden gelir.
sonuc=datetime.fromtimestamp(sonuc) #yukardaki saniyeyi tekrar tarihe çevirir.

#uyarı pcler için milat 1970 tir. yani;
sonuc=datetime.fromtimestamp(0) #0. saniyeyi tarihe çevirdiğinde;  1970-01-01 03:00:00 gelir

##tarihler arasında çıkarma yapma için
sonuc=simdi-birthday #yani timedelta objesi oluşturur. (10598 days, 15:10:24.352082)

##UYARI: ileri tarihi hesaplamak için timedelta clasının çalışması lazım
from datetime import timedelta

sonuc=simdi + timedelta(days=10) #simdi'deki tarihe 10 gün eklemiş oluruz.
sonuc=simdi + timedelta(days=10,minutes=40)

##yada azaltma yapmak için
sonuc=simdi - timedelta(days=10,minutes=40)

print(sonuc) 




