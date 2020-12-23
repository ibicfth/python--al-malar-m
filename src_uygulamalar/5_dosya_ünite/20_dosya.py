# #file=open('newfile.txt','w')
# file=open('newfile.txt','w',encoding='utf-8') #utf-8 bir çok karakteri türkçe karakter yazmayı mümkün kılar.
# #file=open('c:/users/fatih/desktop/newfile.txt','w')

# file.write('fatih ibiç')
# file.close()


# file=open('newfile.txt','a',encoding='utf-8')
# file.write(' fatih ibiç')
# file.close()

# file=open('newfile2.txt','x',encoding='utf-8') # sadece ilk oluşturulduğunda çalışır 
#                                               ikinci defada o dosya konumda olduğundan hata verir.                                                

####################################################3

#dosya okuma : 1 for döngüsü ile
# file=open('5_dosya_ünite/newfile2.txt','r',encoding='utf-8')

# for i in file:
#     print(i,end='') 
# file.close()

#dosya okuma : 2 read()  fonksiyonu ile
# file=open('newfile2.txt','r',encoding='utf-8')
# content=file.read()
# print(content)
# # file.close()

# ##not:dosya içeriğini bi kere okuyup yazdırdıktan sonra dosyayı kapatmadan tekrar okuma
# ## yaptırmak istersek birşey okuyup yazamaz çünkü imleç sonda kalmış olur.
# ## dosyayı kapatma işlemi yada yeniden okuma işlemi yaptırmak lazım.


# ############## readline herseferinde bir satır okur her satır için tekrar çalıştırılmalı. ########
file=open('5_dosya_ünite/newfile2.txt','r',encoding='utf-8')
print(file.readline(),end="") #end="" print 1 satır atlayarak yazar bunu yapmasını istemediğizden bu kullanımı yazarız
print(file.readline(),end="")


# # ################# readlines() bütün satırları okur ve her bir satırı liste elemanı yapar###
# file=open('5_dosya_ünite/newfile2.txt','r',encoding='utf-8')
# a=file.readlines()
# print(a)
# ###################dosya kapama############

# file=open('newfile2.txt','r',encoding='utf-8')
# content=file.read()
# print(content)


# file.close()

# ####başka yol
# with open('newfile2.txt','r',encoding='utf-8') as file:
#     content=file.read()
#     print(content)

# #bu kod (with) dosya işlemi bitince otomatik kapatır.


# ###############################
# with open('newfile2.txt','r',encoding='utf-8') as file:
#     content=file.read()
#     print(content) #imlec sonda dosyayı okudu.

#     print(file.tell()) #imlecin konumunu sçyler

#      content2=file.read() 
#     print(content2) #imlec sonda olduğundan bişey yazdıramaz.

# ####################################
# with open('newfile2.txt','r',encoding='utf-8') as file:
#     content=file.read()
#     print(content) #imlec sonda dosyayı okudu.
#     file.seek(0) #imleci istediğimiz byte (her karakter bi byte dır)

#     print(file.tell()) #imlecin konumunu sçyler

#     content2=file.read() 
#     print(content2) #imlec seek komutuyla başa aldığımızdan content ile aynı cevabı verir.


################################## güncelleme yapma r+ >>>hem okuma hem yazma yapar ####################

# with open('newfile2.txt','r+',encoding='utf-8') as file:
#     print(file.read())
    
# with open('newfile2.txt','r+',encoding='utf-8') as file:
#     file.write('deneme')
#     file.seek(0)
#     print(file.read())


########################## append modu ###################
########### apend modunda imlec otomatik sonda olur #####

# with open('newfile2.txt','a',encoding='utf-8') as file:
#     file.write("\nyunus emre figen 24 sakarya üniversitesi")
    
#     #print(file.read()) #>>>>>>>>> not yazdırma modunda okuma yapılmaz ,tekrar dosya açmak lazım okuma modunda

# with open('newfile2.txt','r',encoding='utf-8') as file:
#     print(file.read())

######################## sayfa başında güncelleme ###########

# with open('newfile2.txt','r+',encoding='utf-8') as file:
#     content=file.read()
#     content='sadık turan\n'+ content
#     file.seek(0)
#     file.write(content)
#     file.seek(0)

#     print(file.read())

######################## sayfa ortasında güncelleme ###########
# with open('newfile2.txt','r+',encoding='utf-8') as file:
#     liste=file.readlines()
#     print(liste)
#     liste.insert(1,'ali korkmaz')
#     print(liste)
# ancak bu ali korkmazı sadece liste ye ekler dosyaya eklemez dosyaya eklemek için:(aşağıda)

# with open('newfile2.txt','r+',encoding='utf-8') as file:
#     liste=file.readlines()
#     liste.insert(1,'ali korkmaz\n')
#     file.seek(0)
#     for i in liste:   #for döngüsünü yazmak istemezsek writelines() methodunu kullanabilriiz.
#         file.write(i)
#     file.seek(0)
#     print(file.read())


# with open('newfile2.txt','r+',encoding='utf-8') as file:
#     liste=file.readlines()
#     liste.insert(1,'ali korkmaz\n')
#     file.seek(0)
#     file.writelines(liste)   #for döngüsünü yazmak istemezsek writelines() methodunu kullanabilriiz.         file.write(i)     file.seek(0)
#     file.seek(0)
#     print(file.read())



