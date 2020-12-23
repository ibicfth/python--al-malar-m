import pandas as pd    

data=pd.read_csv("12_pandas/nba.csv")
print(data)
print(data.columns)

## örneğin player kolonunda yazan oyuncu isimlerini büyük harfeçevirmek için,
data["Player"]=data["Player"].str.upper()

## herhangi bir kolonda karakter aratıp yeni bir kolon ekleyip o kolonda yazdırmak için;
data["arama"]=data["Player"].str.find("A") #player kolonunda a aratıp bulduğu sonucların index numarasını arama kolununda yazar.
print(data)

##arağımız kelimeyi için satırları True yapan contains methodu
data2=data["Player"].str.contains('JONHSON')
print(data2)

##JOHNON ları bulup  yazdırmak içinse;
data = data[data["Player"].str.contains('JOHNSON')]  

## herhenhi bir karakteri başka karakter ile değiştirmek için
data=data["Date"].str.replace(" ","--")

## oyuncu isimleri eğer sadece 2 kelimeden oluşuyorsa bunları yeni oluşturulan satırda yazma;
data[["First","Last"]]=data["Player"].loc[data["Player"].str.split().str.len()==2].str.split(expand=True)

print(data) ##baştan 5 kaydı getirir.

