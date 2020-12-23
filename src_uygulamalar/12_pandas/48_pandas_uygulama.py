import pandas as pd 

##soru1
df=pd.read_csv("12_pandas/imdb.csv")
result=df.info 

##soru2
result=df.columns
result=df.head()

## soru3
result=df.columns
result=df.head(10)

##soru3
result=df.columns
result=df.tail()

##soru5
result=df.columns
result=df.tail(10)

#soru6
result=df["Title"]


##soru7
result=df["Title"].head()

##soru8
result=df[["Title","Rating"]].head()

##soru9
result=df[["Title","Rating"]].head(7)

##soru10
result=df[5:10][["Title","Rating"]]

##soru11
result=df[(df["Rating"]> 8.0)][["Title","Rating"]].head(50)
##or
result=df.query("Rating > 8.0")[["Title","Rating"]].head(50)

##soru12
result=df.query("Year > 2014 & Year<=2015")[["Title","Year"]]

##soru13
result=df.columns
result=df["Votes"]
result=df["Votes"].max() ##1791916
result=df["Votes"].min()  ##61 
result=df.query("Votes>950000 | (Rating>=8.0 & Rating<=9.0)")[["Title","Rating","Votes"]]
print(result)
