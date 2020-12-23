# y='hello word' # ilk 'o' ya geldiğinde program durur.
# for x in y:
#     if x=='o':
#         break

#     print(x)

# y='hello word' #  'o'larda program o döngüyü atlar
# for x in y:     # sonraki döngüye geçer.
#     if x=='o':
#         continue

#     print(x)
######################
# x=0           # x=2 oldugunda program durur.
# while x<10:
    
#     if x==2:
#        break
#     print(x)
#     x +=1
# ######################################
# x=0             # x=2 olduğunda 2 yi yazdırmaz döndürmez
# while x<10:     # sonraki çevrimden devam eder.
#     x +=1
#     if x==2:
#         continue
#     print(x)

###########################################
sonuc=0
x=0             # sadece çift sayıları toplayan program
while x<100:     
    x +=1
    if x%2==1:
         continue
    sonuc +=x
print(sonuc)
############################################### 