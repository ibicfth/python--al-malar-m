import os

sonuc=dir(os)
sonuc=os.name # işletim sisteminin adını söyler nt=windows
sonuc=os.getcwd() #28_os klasörünün uzantısını söyler etkin dizini söyler yani

#os.mkdir("newdirector") # yeni bir klasör(dosya değil klasör) oluşturur aynı dizin altında
### buraya kadar olan kısmın dizini adresi: C:\Users\fatih\desktop\python_temelleri değiştirmek için

#os.name("newdirector","lastdirector") # klasör adını değiştirir

#os.rm("lastdirector") #kalsörü siler

# os.chdir('c:\\') # c nin altına geldik dizini değiştirdik . şimdi dosya eklersek c nin altına ekler

# os.getcwd('..') # bir üst dizine geçer.
# os.getcwd('../..') # iki kere yaptırmış oluruz ve iki üst dizine geçer.

#os.makedirs("newdirector/yeniklasör") # newdirector ün içinde yeniklasör adlı klasöroluşturduk

### herhangi birdizindeki dosyaları listelemek için;
sonuc=os.listdir() # mevcut idizindeki klasörleri listeler

##istediğmiz bi dosyadaki klasörü listelemek için;
#sonuc=os.listdir('c:\\') # c dizini altındaki dosyaları listeler

 ##>>>>>  listeleme yapılırken filtreleme yapmak için
for dosya in os.listdir():
    if dosya.endswith('.py'):
     print(dosya)
    

sonuc=os.stat('newdirector')  # dosyanın oluşturma,boyut,son değişiklik gbi özelliklerini getiri.
sonuc=os.stat('newdirector').st_size # dosyanın büyüklüğünü  byte olarak verir.

sonuc=os.stat('newdirector').st_ctime  # dosyanın oluşturulma tarihini sanşye cinsinden verir
## eğer bunu gün yıl ay formatından yazdırmak istiyorsak fromtimestamp methodun çağırmalıyız
import datetime  #fromtimestamp datetime modülünün  methodu
sonuc=datetime.datetime.fromtimestamp(os.stat('newdirector').st_ctime)  #oluşturulma tarihi
sonuc=datetime.datetime.fromtimestamp(os.stat('newdirector').st_atime)  #son erişim tarihi
sonuc=datetime.datetime.fromtimestamp(os.stat('newdirector').st_mtime)  #son değitirme tarihi


#os.system('notepad.exe') # system dosya açar çalışltırır.

########### path dosya isminideğiştiri.ancak daha çok uzantısını değiştirir.
sonuc=os.path.abspath("28_os.py")  # dosyanın tam konumunu verir.dosya isminden konumu verir
sonuc=os.path.dirname("C:/Users/fatih/desktop/python_temelleri/28_os.py") #dosya konumundan dizini verir.tam konumdan bir önceki dizine kadar olanı gösterir. C:\Users\fatih\desktop\python_temelleri

###>>>> bir dosyanın sadece ismini biliyorsan nerde olduğunu yani dizinini yukarıdaki iki methodu birleştirerek buluruz.

sonuc=os.path.dirname(os.path.abspath("28_os.py")) 

# bir konumda dosyanın olup olmadığına bakmak için;
sonuc=os.path.exists("C:/Users/fatih/desktop/python_temelleri/28_os.py")  #true yada false döndürür.

### dosya mı klasör mü olduğunu sorgulamak için isdir kullanılır.klasör=1>true, dosya=0>false dır
sonuc=os.path.isdir("C:/Users/fatih/desktop/python_temelleri/28_os.py") #dosya oldugundan false gelir


print(sonuc)
