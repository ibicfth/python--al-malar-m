import pandas as pd   

data=pd.read_csv("12_pandas/nba.csv")

##1
df=pd.DataFrame(data)
print(df.head(10))

##2
result1=len(df) ## satır uzunluğu
print(result1)
#yada
result2=len(df["Player"])
print(result2)
##farklı
result=df.size ## toplam eleman

##3
result=df["Age"].mean()

##4
result=df["Age"].max()

##5
result=df.query("Age.max()")["Player"]
result=df.query("Age.max()").loc["Player"]
result=df[df["Age"]==df["Age"].max()]["Player"]

##6
result=df.query("Age >=20 & Age<=26")[["Player","Team","Age"]].sort_values("Age",ascending=False)

##7
result=df[df["Player"]=="Jimmy Butler"]["Team"]

##8
result=df.groupby("Team").mean()["Age"]

##9
result=len(df.groupby("Team"))
result=df["Team"].nunique()

##10
result=df["Team"].value_counts() ## team gruplarının kümelerinde kaçar eleman var olduğunu

##11
result=df[df["Player"].str.contains("and")] #yada

 ##buna alternatif olarak;

def bul(Player):
    if "and" in Player.lower():
         return True
    return False

result=df[df["Player"].apply(bul)] ##apply methodunun içine sınıf referansı verebiliyoruz.
print(result)