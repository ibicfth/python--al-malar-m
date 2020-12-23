import matplotlib.pyplot as plt   
import numpy as np

# x=[1,2,3,4]

# plt.plot(x) ## sadece tek bir eksen verilirse  y eksenine yazar.
# plt.show()

#################
# x=[1,2,3,4]
# y=[1,4,9,16]

# plt.plot(x,y)
# plt.show()

################
## axis komutu x ve ye ekseninin minimum ve maksimum limitlerini belirler
# x=[1,2,3,4]
# y=[1,4,9,16]

# plt.plot(x,y)
# plt.axis([0,6,0,20]) ## x ekseni 0 dan 6 ya kadar, y ekseni 0 dan 20 e kadar
# plt.show()
###############
## grafiğe ve eksenlere değer verme;
# x=[1,2,3,4]
# y=[1,4,9,16]

# plt.plot(x,y)
# plt.axis([0,6,0,20]) 

# plt.title("Grafiğin Başlığı Yazılır")
# plt.xlabel("X ekseni etiketi yazılır")
# plt.ylabel("Y ekseni etiketi yazılır")
# plt.show()

##################33
## renk ve kalınlım verme 
# x=[1,2,3,4]
# y=[1,4,9,16]

# plt.plot(x,y,color="orange",linewidth="5")
# plt.show()

#########################
## çizgi ayarlar formatı>>> [marker][line][color] şeklindedir

# x=[1,2,3,4]
# y=[1,4,9,16]

# plt.plot(x,y,"--g") ## burda marker yok, line şekli: --   ,color: green(g)
# plt.show()

# #########################
# x=[1,2,3,4]
# y=[1,4,9,16]

# plt.plot(x,y,"o--g") ## burda marker  x ve y keşişim noktasını gösterir, line şekli: --   ,color: green(g)
# plt.show()

############################
# x=np.linspace(0,2,100)

# plt.plot(x,x,label="linear",color="yellow")
# plt.plot(x,x**2,label="quadratic",color="red")
# plt.plot(x,x**3,label="cubic",color="black")

# plt.xlabel("x label")
# plt.ylabel("y label")


# plt.legend()  ###çizgi isimlerini(label) veririr.
# plt.show()

#####################
##sayı dorğultusundaki her bir bölge axes alanıdır.
##subplots methodu ile bir axes alanında kaç çizim yaptırmak istediğimizi belirleriz

# x=np.linspace(0,2,100)
# fig, axs=plt.subplots(2) # bir axes bölgesinde iki çizim yapacağız

# axs[0].plot(x,x,label="yavhe",color="blue") ## axes alanında yaptırmak istediğimiz iki çizimden birincisi
# axs[0].set_title("1. grafik")

# axs[1].plot(x,x**3,label="nededin",color="orange")## axes alanında yaptırmak istediğimiz iki çizimden ikincisi
# axs[1].set_title("2. grafik")

# plt.legend()

# plt.tight_layout() ##alt ve üsteki grafik başlıklarının üst üste gelmemesi için

# plt.show()

##############################
# x=np.linspace(0,2,100)
# fig,axs=plt.subplots(2,2) ## 2 ye 2 lik toplamda 4 graifk oluşturur.

# axs[0,0].plot(x,x,color="blue")
# axs[0,1].plot(x,x**2,color="black")
# axs[1,1].plot(x,x**3,color="red")
# axs[1,0].plot(x,x**4,color="yellow")

# plt.show()

#################################
## BÜYÜK VERİLERDEN GRAFİK OLUŞTURMAK İÇİN ###
import pandas as pd   

df=pd.read_csv("12_pandas/nba.csv")
df=df.groupby("Team").mean()
df.head().plot(subplots=True) ## team groublamasında mean ile gelen kaçtane kümecik varsa axes te okadar çizim yapması için sayıyı bilmediğimizden true veririz. 
plt.legend() ## çizgi isismlerini yazdırır.
plt.show()