## amacımızın sadece belli bir hesaplama yaptırıp ekrana yazdırmak bellekteyer işgal etmesini
## istemiyorsak generator kullanırız.
##generator bir iterator gibi dir ,çağırmak için next() methodu çağırmalıyız 
# yada for ile oluşturulan iteratoru=generatorü yazdırmalıyız.

def us():  ## burada result listesi bellekte yer tutar.
    result = []
    for x in range(5):
        result.append(x**3)
    return result

print(us())

###################

def üsal():
    for x in range(5):
        yield x**3      ### yield return ile aynı görevi yapar ama ayrıca bellekte yer tutmadan
#                            #iterator oluşmasını sağlar.
for i in üsal():
    print (i)

################## generator yapmaya alternatif
liste1=[i**3 for  i in range(5)] # bu liste tanımlar ama liste bellekte yer tutar.köşeli parantezden dolayı
print(liste1)
#bunu şu şekilde yazarsak generator liste oluşur;
liste2=(i**3 for i in range(5))

#bunu yazdırmak içinse next() yada for ile yazdırırız.
for i in liste2:
    print (i)

