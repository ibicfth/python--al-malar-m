import pandas as pd 

# pandas_series=pd.Series()
# print(pandas_series)

#data veri tiplerinde pandas

numbers=[20,30,40,50]
pandas_series=pd.Series(numbers)
print(pandas_series)

letter=['a','b','c','d']  ##heterojen bir yapıdadır. 
pandas_series=pd.Series(letter)
print(pandas_series)

letter=['a','b','c',20]  ##heterojen bir yapıdadır. farklı türde veriler verilebilir 
pandas_series=pd.Series(letter)
print(pandas_series)

scalar=5
pandas_series=pd.Series(scalar)
print(pandas_series)


##yukardaki örnekelrin hepsinin indekslerini kendi isteiğimiz gibi verebiliriz!!
'''
indeksiz                                    indeksli
numbers=[20,30,40,50]                       numbers=[20,30,40,50]
pandas_series=pd.Series(numbers)            pandas_series=pd.Series(numbers,['a','b','c','d'])

diğerleirnede verileblir
'''

dict={'a':5,'b':4,'c':9,'d':5454}
pandas_series=pd.Series(dict)
print(pandas_series)


###numpy ile üretilen sayılarıda kullanılbilriz.
import numpy as np

dizi=np.random.randint(15,95,6)
pandas_series=pd.Series(dizi)
print(pandas_series)


###### elemanıları çağırırken ister 0. indeks ister kendi belirlediğimiz indeks sıralasına göre çağırabilirzi
numbers=[20,30,40,50]
pandas_series=pd.Series(numbers,['a','b','c','d']) ##numbers dizinin kenisinide buraya direk yazabiliriz.
print(pandas_series)
print(pandas_series[0])
print(pandas_series['a'])

## yada  birden fazla indeks i getirmek istiyorsak indeksleri dizi şeklinde veririz
print(pandas_series[['a','b']])


pandas_series.ndim #>> liste boyutunu
pandas_series.shape  ##>> kaça kaçlık dizi oldugunu söyler 3x5 yada (3,5) gibi
pandas_series.sum() #>> elemanları toplar

result=np.sqrt(pandas_series) ## pandas dizisinin elemanlarının karekökünü aldırma

result=pandas_series >= 50 #pandas dizisinin 50 den büyük elemanları için true yazıdrır
##true olan değerlerin hangi sayılarsa onları yazdırmak için
print(pandas_series[result]) #yada 

print(pandas_series[pandas_series >= 50]) # şeklinde yapılır

print(result)


################## DATA FRAME ################33
df=pd.DataFrame()  #kullanımı
print(df)

data=[['ahmet',50],['veli',70],['ceylan',60],['osman',75]]
df=pd.DataFrame(data,index=[1,2,3,4],columns=['name','grade'],dtype=float)
print(df)
##yada data şu keilde tanımlarsak sütun kolon kendi belirler 
data={'name':['ahmet','veli','ceylan','osman'],'grade':[50,70,60,75]}
df=pd.DataFrame(data)
print(df)
##yada
data=[
    {'name':'ali','grade':50},
    {'name':'veli','grade':70},
    {'name':'ceylan','grade':60},
    {'name':'osman','grade':75}

]
df=pd.DataFrame(data)
print(df)

s1=pd.Series([11,32,53,74,95])
s2=pd.Series([23,65,28,90,22])

data={'oranges':s1,'apples':s2}
df=pd.DataFrame(data)  ## verilen listeyi sütun (key), ve satır (value) oluşturur.

print(df)

