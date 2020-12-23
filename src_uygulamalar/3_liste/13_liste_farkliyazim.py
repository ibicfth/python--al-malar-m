# numbers=[]
# for x in range(10):
#   numbers.appen(x)    
# print(numbers)

#AYNISINI ALTTAKİ YAPAR

# numbers=[x for x in range(10)]  #dizi içinde for tanımlama
# print(numbers)
##################################################
# numbers=[x**2 for x in range(10)]  #10 kadar olan sayıların karesini alır.
# print(numbers)

###################################
# 10 kadar olan sayılardan 3 e bölünebilenlerin karesini alır
# numbers=[x**2 for x in range(10) if x%3==0]
# print(numbers)
#####################################
# x in her değeri icin ye 0'dan 3 e kadar döner
# yani 3 e 3'lük matris olusturur.
#
#  result=[]
# for x in range(3):
#     for y in range(3):
#         result.append((x,y))
# print(result)

# # AYNI SONUC YAPAN 
# numbers=[(x,y) for x in range(3) for y in range(3)]
# print(numbers)
######################################################