import pandas as pd  

data=pd.read_csv("12_pandas/data_youtube.csv")
df=pd.DataFrame(data)
###1
result=df.head(10)

###2
result=df[5:10].head()

###3
result=df.columns
result=len(df.columns)

###4
#df=df.drop[["xxx"],axis=1]
result=df

###5
result=df["likes"].mean()

result=df["dislikes"].mean()

##6
result=df[["likes","dislikes"]].head(50)

###7
result=df[df["views"]==df["views"].max()][["views","title"]]

###8
result=df[df["views"]==df["views"].min()][["views","title"]]

###9
result=df.sort_values("views",ascending=False).head(10)[["views","title"]]

###10
result=df.groupby("category_id").mean().sort_values("likes")["likes"]

###11
result=df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]

###12
result=df["category_id"].value_counts()

###13
df["title_character"]=df["title"].apply(len)

###14
df["tag_count"]=df["tags"].apply(lambda x: len(x.split("|")))
##yada;
def tag_counts(tags):
    return len(tags.split("|"))
 
df["tag_count"]=df["tags"].apply(tag_counts)

###15

def begeniOrani(dataset):
    likes_list=list(dataset["likes"]) ##likesleri liste yapar.
    dislikes_list=list(dataset["dislikes"])
    liste=list(zip(likes_list,dislikes_list))
    oran=[]
    for like, dislike in liste:
        if like + dislike ==0:
            oran.append(0)
        else:
            oran.append(like/(dislike+like))
    return oran
df["kalite"]=begeniOrani(df)

print(df[["title","likes","dislikes","kalite"]].sort_values("kalite",ascending=False))