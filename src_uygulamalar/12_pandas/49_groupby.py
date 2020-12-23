import pandas as pd   

# personeller={
#     "çalışan":["ahmet yılmaz","can ertürk","hasan korkmaz","cenk saymaz","ali turan","rıza ertürk","mustafa can"],
#     "departman":["insan kaynakları","bilgi işlem","muhasebe","insan kaynakları","bilgi işlem","muhasebe","bilgi işlem"],
#     "yaş":[30,25,45,50,23,34,42],
#     "semt":["kadıköy","tuzla","maltepe","tuzla","kadıköy","tuzla","maltepe"],
#     "maaş":[5000,3000,4000,3500,2750,6500,4500]

# } 
### çift tırnak olunca  tablo oluşturulur ama column isimleri gelmez


personeller={
    'çalışan':["ahmet yılmaz","can ertürk","hasan korkmaz","cenk saymaz","ali turan","rıza ertürk","mustafa can"],
    'departman':["insan kaynakları","bilgi işlem","muhasebe","insan kaynakları","bilgi işlem","muhasebe","bilgi işlem"],
    'yaş':[30,25,45,50,23,34,42],
    'semt':["kadıköy","tuzla","maltepe","tuzla","maltepe","tuzla","kadıköy"],
    'maaş':[5000,3000,4000,3500,2750,6500,4500]

}
df=pd.DataFrame(personeller)
result=df["maaş"].sum() ## maaş kolonunu toplar
result=df.groupby("departman") # deparmanı gruplandırdır
result=df.groupby("departman").groups ## hangi elemanlar hangi indekste bu grupta olduğunu gösterir
result=df.groupby(["departman","semt"]).groups

print(result)

semtler=df.groupby("semt")
for x, y in semtler:  
    print(x) ## x >> semtteki elemanların hangisine göre gruplama yapıldıysa onun adı 
    print(y) ## y >> grublama yapılan elemanları küme küme tablosunu getirir.

#bunu semtler die ayrı obje tanımladan da yapabiliriz.
for x, y in df.groupby("semt"):  
    print(x) ## x >> semtteki elemanların hangisine göre gruplama yapıldıysa onun adı 
    print(y) ## y >> grublama yapılan elemanları küme küme tablosunu getirir.


for x, y in df.groupby("departman"):  
    print(x) ## x >> semtteki elemanların hangisine göre gruplama yapıldıysa onun adı 
    print(y) ## y >> grublama yapılan elemanları küme küme tablosunu getirir.

#### bu druplamadan sonra sadece oluşan kümelenmelerden bir tanesinin getirirlmesini istiyorsak;
result=df.groupby("semt").get_group("kadıköy") ##semt i grublar ve kadıköy grubunu getirir.


## 
result=df.groupby("departman").sum() ## departmanda toplanacak bişey yok ama departmanı gruplar ve;
##bu grubların yaş ve maaş olarak toplamlarını gösterir. yani yani yaş ve maaşları deparmana göre gruplamış oldu.

result=df.groupby("departman").mean() ##ortalamaları

##deparmanın sadece grubladıktan sonra o grubların sadece maaş yada yas larının tekini getirmek için;
result=df.groupby("departman")["maaş"].mean()

result=df.groupby("semt")["yaş"].mean() #semtlere göre yaş ortalamaları

result=df.groupby("semt")["çalışan"].count() #semtlere göre çalışanların sayıları

result=df.groupby("departman")["maaş"].max()
result=df.groupby("departman")["maaş"].min()

result=df.groupby("departman")["maaş"].min()["muhasebe"] #deparmana göre maaşların min olanları bulur ve muhasebe departmanının min maaşını getirir.


## GROUPBY DA NUMPY KULLANIMI
### pandasta groublama yapabiliyorken numpy ile yapmak istememizin sebebi;
## numpy da birden fazla şarta göre gruplama yaptırabilmemizdir.

import numpy as np
result=df.groupby("departman").agg(np.mean)  ## depramtnı maaş ve yaşa göre ortalaması

result=df.groupby("departman")["maaş"].agg([np.sum,np.mean,np.max,np.min])
##departmanı grublandırıp maaşlarının toplamını,ortalamasını,max,min yazdırırız.

##yada bu hesaplamaları departmanın sadece bir elemanına göre yapmak istersek;
result=df.groupby("departman")["maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["muhasebe"]



print(result)
