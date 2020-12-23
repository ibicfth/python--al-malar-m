import pandas as pd  


customers={
    'customerid':[1,2,3,4],
    'firstname':["ahmet","ali","hasan","canan"],
    'lastname':["yılmaz","korkmaz","çelik","toprak"]
}

orders={
    'orderid':[10,11,12,12],
    'customerid':[1,2,16,17],
    'orderdate':["2018","2019","2020","2021"]

}

df_customers=pd.DataFrame(customers)
df_orders=pd.DataFrame(orders)
print(df_customers)
print(df_orders)

result=pd.merge(df_customers,df_orders,how="inner")  ##ortak kolon custormerid ye göre


result=pd.merge(df_customers,df_orders,how="left")  ## soldakiler + keşişim


result=pd.merge(df_customers,df_orders,how="right") ## keşişim + sağ

result=pd.merge(df_customers,df_orders,how="outer") ## birleşim hepsini alır

print(result)

##### birleştirme concat methodu ############

customersA={
    'customerid':[1,2,3,4],
    'firstname':["ahmet1","ali1","hasan1","canan1"],
    'lastname':["yılmaz","korkmaz","çelik","toprak"]
}

customersB={
    'customerid':[1,2,3,4],
    'firstname':["ahmet2","ali2","hasan2","canan2"],
    'lastname':["yılmaz","korkmaz","çelik","toprak"]
}

df_customersA=pd.DataFrame(customersA)
df_customersB=pd.DataFrame(customersB)

result=pd.concat([df_customersA,df_customersB])  ##axis=0 varsayılan satır olarak ekler

result=pd.concat([df_customersA,df_customersB],axis=1) ## sütün yani kolon ekler

print(result)


## bazı özel dateframe methodları

data={
    'column1':[1,2,3,4],
    'column2':[15,70,96,12],
    'column3':["abc","ajl","fgt","erv"]

}

df=pd.DataFrame(data)
def kareal(x):
    return x*x

result=df["column1"].value_counts() ## kolon1 deki elemanlardan kaçar tane var aynı olanlardan gösterri

result=df["column1"].apply(kareal) ##apply ın içine fonksiyon adı verebiliyoruz
#burada kolon1 i kareal fonksiyonuna yolladık

result=df.sort_values("column2",ascending=True) ##kolon2 yi küçükten büyüğe sıralar
result=df.sort_values("column2",ascending=False)##kolon2 yi büyükten küçüğe doğru sıralar.
print(result)

print(list(range(100)))
## kolonları satır sütün ve veri olarak ayarlamak için pivot table

data={
    'ay':["ocak","şubat","mart","ocak","şubat","mart","ocak","şubat","mart"],
    'kategori':["elektronik","elektronik","elektronik","oyuncak","oyuncak","oyuncak","kitap","kitap","kitap"],
    'gelir':[0, 1, 2, 3, 4, 5, 6, 7, 8]
}

df=pd.DataFrame(data)
df=df.pivot_table(index="kategori", columns="ay", values="gelir")
print(df)
#print(len(df["ay"]),len(df["kategori"],len(df["gelir"])))
