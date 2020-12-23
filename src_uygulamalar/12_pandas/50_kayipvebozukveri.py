import pandas as pd   
import numpy as np

# personeller={
#     'çalışan':["ahmet yılmaz","can ertürk","hasan korkmaz","cenk saymaz","ali turan","rıza ertürk","mustafa can"],
#     'departman':["insan kaynakları","bilgi işlem","muhasebe","insan kaynakları","bilgi işlem","muhasebe","bilgi işlem"],
#     'yaş':[30,25,45,50,23,34,42],
#     'semt':["kadıköy","tuzla","maltepe","tuzla","maltepe","tuzla","kadıköy"],
#     'maaş':[5000,3000,4000,3500,2750,6500,4500]

# }

data=np.random.randint(10,110,15).reshape(5,3)
df=pd.DataFrame(data, index=["a","c","e","f","h"], columns=["column1","column2","column3"])

df=df.reindex(["a","b","c","d","e","f","g","h"])

result=df

##silme işlemlerini hatırlayalım
result=df.drop("column1",axis=1) #column1 i siler axis belirtmek lazım
## ancak satır silmek istedipimizde;
result=df.drop("a",axis=0) ##a satırını siler

##eğer boş olan elemanları görmek tespit etmek istersek isnull methodunu kullanırız.
result=df.isnull()  ##boş olan(NaN) yerleri True gösterir.


##tek bir kolon için sorgulama yapmak içinse;
result=df["column1"].isnull()

##tek bir kolonun NaN olan satırlara göre ;bütün o satırın kolonlarını getirmek için.
result=df["column3"].isnull() ##column3 ün null olan satırlarının diğer bütün kolonlarınıda getirir.
##true olanların seçip yazdırmak içinse;
result=df[df["column1"].isnull()]["column1"]

##null olmayan alanrı getirmek içinse;
result=df[df["column1"].notnull()]["column1"]
##eğer NaN ların değilde veri olan elemanların yerini görmek istiyorsak notnull mehtodunu kullanırız.
result=df.notnull()

##nullların toplamı için
result=df.isnull().sum()  #hangi kolonda kaç tane NaN olduğunu sayar
##tek bir kolon içinse
result=df["column1"].isnull().sum()


##yeni bir kolon eklemek için;
newColumn=[np.nan,40,np.nan,65,np.nan,13,np.nan,47]
df["column4"]=newColumn


##dropna methodu ile satır veya sütunda nan varsa o satır veya sütunu siler >>varsayılan değeri axis=o dır satırı siler
result=df.dropna()  ##axis=0  satıların herhangi bir kolon değerinde null varsa o satırı siler

result=df.dropna(axis=1) ## sütünların her hangi birtanesinde null değeri varsa o sütunu siler
## df içindeki her kolonda nan olduğundan boş liste getirir.

## biz sadece bir tane NaN gelidiğinde o satır yada sütunun silinmesini istemiyorsak how methodunu kullanırız
result=df.dropna(how="any")  ## bir tane nan gelmesi durumunda satırı siler
result=df.dropna(how="all")  ## bütün satır nan ise o satırı siler

result=df.dropna(how="any",axis=1) ## kolonda herhangi bir nan varsa o kolono siler 
result=df.dropna(how="all",axis=1) ## kolondaki bütün elemanlar nan ise o kolonu siler

##>>bu how bütün kolon yada satırlarda arama yapar biz sadece bir kolon yada satırda yada istediklerimizde arama yaptırmak için;
##bunun için subset methodunu kullanıp hangi kolon yada satırda how kullanmak istersek belirtebiliiz
result=df.dropna(subset=["column3","column1"], how="any") ##kolon3 ve kolon1 de how uygulanır diğer kolonları getirir.
#yani kolon1 ve kolon3 te nan varsa o satırları siler. diğer satırlar kalır


##eğer istediğimiz kadar veri olmayan satır ve kolonu silmek istersek thresh methodunu kullnırız
result=df.dropna(thresh=4) ##axis=0 varsayılan , satırlarda 4 veri olan yani 4 kolonda veri olanı silmez daha az olanı siler.

result=df.dropna(thresh=3,axis=1) ##kolonda en az 3 veri olmayanı siler

### NaN alanlara bişey yazdırmak için fillna;
result=df.fillna(value="no input") ## null olanları bul ve no input yaz

result=df.fillna(value=1) ##null lara 1 yazdırır

## kolonlardaki toplamları getirmek için.
result=df.sum()

##dataframe deki bütün elemanları toplamak için;
result=df.sum().sum()
result=df.size  #toplam eleman sayısını

##null olan kolonların toplamı
result=df.isnull().sum()

##null olan kolonların toplamının toplamı
result=df.isnull().sum().sum

##null olan satırların toplamı
result=df.isnull().sum(axis=1)

##null olan satırların toplamının toplamı
result=df.isnull().sum(axis=1).sum()

##  küçük bi uygulama
## toplam eleman sayısından null sayısını çıkartıp adet bulup 
## df içeriğinin toplamını eleman sayısına bölüp ortalama hesaplattrıalım ve bu ortlamaları
## df te null olan yerlere yazdıralım
def ortalama(df):
    toplam=df.sum().sum()  ## elemanların toplamı
    adet=df.size - df.isnull().sum().sum() #null olmayan eleman sayısı
    return toplam / adet 

result=df.fillna(value=ortalama(df)) ## ortalama sınıfdan gelen ortalamaları null olan yerlere yazdırma


print(df)
print(result)
