#YÖNTEM 1
#import math 

#value=dir(math) #modüldek, bütün methodların isimleri gelir
#value=help(math) #modüldeki bütün methodların nasıl kullanılacağı ve parametreleri
#value=help(math.factorial)# sadece factoriyelin yardmını açar
#print(value)  

##############################
#YÖNTEM 2

# from math import *   #bütün mfonksiyonları import ettiğimizden artık math.sqrt demeden direk sqrt() fonksiyonunu kullanabilriz

# value=sqrt(9)
# print(value)
##############################
#from math import sqrt,factorial  # sadece sqrt ve factoriali import ettik diğerleri kuallnılamaz.


################################
# RANDOM MODÜLÜ
#import random

# #value = random.random()  # 0.0 ve 1.0 arasında bir sayı üretir.

# value = random.uniform(1,10) # bir ile 10 arasında bir sayı üretir

# value = int(random.uniform(1,10)) #üretilen sayıların tam kısmını alır.yada
# value=random.randint(1,10) #1 ile 10 arasında tam değerleri alır

########################
# verilen diziden random eleman seçme
#liste=['ali','veli','deniz','yagmur']
# # value=liste[random.randint(0,len(liste)-1)] # ==value=random.choice(liste)

# value=random.choice(liste)

# random.shuffle(liste) # buda liste karıştırır,orjinal hali artık karışık hali olur.
# print(liste)

# sonuc=random.sample(liste, 2)  #listeden 2 tane herhangi veriyi alır.
# print(sonuc)

#print(value)

#############################


