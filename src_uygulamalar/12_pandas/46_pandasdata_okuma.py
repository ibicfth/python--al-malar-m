import pandas as pd 


df=pd.read_csv('12_pandas/indian_food.csv')
print(df)

df=pd.read_json('12_pandas/not.json',encoding="UTF-8")
print(df)

df=pd.read_excel('12_pandas/sample.xlsx') ## burda encoding hata veriyor. dosyayı olduğu gibi okuyor tr uyuymlu
print(df)

######## >>>>>>>>>>>>>>>>> satır sütun da ki verileri alma<<<<<<<<<<<<<<#############
from numpy.random import randn

df=pd.DataFrame(randn(3,3), index=["a","b","c"],columns=["column1","column2","column3"])
result=df
 ##sütun için
result=df["column1"]

result=type(df["column1"])

result=df[["column1","column2"]]


## loc >>> loc["row","column"] 
##sadece satır için loc["row"]
## sadece sütun için loc[":","column"]
##satır için 
result=df.loc["a"]  ## a satırının sütunlarda(column) bulunan bilgilerini  getirir
result=type(df.loc["a"])

result=df.loc[:,"column1"]

result=df.loc[:,["column1","column2"]]

## çok sayıda kolon olup belli aralıkta olanları getirmek için;
result=df.loc[:,"column1":"column3"] ##column1,column2,column3 gelir. bunu şöylede olur

result=df.loc[:,:"column3"]

### tek bir elemanı getirmek için
result=df.loc["a","column3"] 

## bu 3x3 lük randn ye sütun eklemek için;
df["column4"]=pd.Series(randn(3),["a","b","c"])

df["column5"]=df["column1"]+df["column3"]

##silme işlemi  satır=x=0  |||sütun=y=1 axis değeri için
print(df.drop("column5",axis=1)) # burda birde inplace parametresi vardır varsayılan değeri false yani;
## df nin kopyasını oluşturu değişiklikleri kopya üzerinde yapar. ama df yi değiştirmek istiyorsak true yaparız.

print(df.drop("column5",axis=1,inplace=True)) ##şimdi df nin 5. sütununu sildi orjinalde. 


print(result)
