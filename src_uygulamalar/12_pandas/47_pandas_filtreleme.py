import pandas as pd  
import numpy as np

data=np.random.randint(10,100,75).reshape(15,5)
df=pd.DataFrame(data,columns=["column1","column2","column3","column4","column5"])
result=df

##başka bi yerden okuma yaptığımızda çok sayıda kolon ve sütun olabilir sütun ve kolonları görmek için;

result=df.columns #kolonları getirir sadece
result=len(df.columns) ## kolonların saysını getirir.

## satırlar için
## head methodu varsayılan değeri=5 tanımlıdır
result=df.head()  #5 satırın verisini getirir

result=df.head(10) #10 parametre getirir.

##en sondan almak için
result=df.tail() ##varsayılan değeri 5 tir
result=df.tail(10)


result=df["column1"].head() ## column1 in ilk 5 verisini getirri.
result=df[["column1","column3"]].head()

result=df[5:15][["column1","column3"]].head() ## kolon1 ve kolon2 nin  5 ten 15 satırlarının 5 verisini getirir. 

result=df > 50 #50 den büyük kayıtlar için True getirir. bunların hangileri olduğunu yazdırmak için
result=df[df >50] ## 50 den büyük olup true olan değerleri getir.

## sadece tek bir kolondakilerin 50  den büyük olanlarını bulmak için
result=df["column1"] > 50

##bunları getirmek isteğimizde sadece kolon1 değil kolon 1 de 50 den büyük olan satırların kolon1,kolon2,kolon3,kolon4,kolon5 hepsini getirir.
##yani kolon1 in 5. satırı 50 den büyükse 5. satırın kolon1,kolon2,kolon3,kolon4,kolon5 daki bilgilerini getrir.
result=df[df["column1"]>50]  ## biz sadece kolon 1 in 50 den büyük olan değerlerini getirmek istiyorsak;

result=df[df["column1"]>50]["column1"] #yani gelenlerin arasından sadece kolon1 i listelettiriyoruz.


## daha fazla şart eklemek içim  "&"==>> "ve" anlamında

result=df[(df["column1"]>50) & (df["column2"]<=70)]  ##kolon 1 ve kolon2 şartları sağlanan bütün kolonları getirir
#sadece kolon1 ve kolon2 nin gelmesi için
result=df[(df["column1"]>50) & (df["column2"]<=70)][["column1","column2"]]

## daha fazla şart eklemek içim  "|"==>> "or" anlamında
result=df[(df["column1"]>50) | (df["column2"]<=70)]

##TÜM BUNLARI query("") methodu ile yapabiliriz.

result=df.query("column1 >50 & column2 <=70")

result=df.query("column1 >50 & column2 <=70")[["column1","column2"]]

print(result)




