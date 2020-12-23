## normalde oluşturdurğumuz dict  listesi eğer string olarak verilirse json ile dict hale getirilir.

person={"name":"ali","langauges":["python","c#"]} ## dict haldeki liste

person='{"name":"ali","langauges":["python","c#"]}' ## string bir ifade '' içine yazılmış

### stringi dict yapmak için json modülü kullaılır.

import json

# person='{"name":"ali","langauges":["python","c#"]}'

# result=json.loads(person)  #dosyadan alırken loads değil load kullanılır.
# print(result) # artık dictinary list oldu.

###########################################################
## dosyalardaki metinler string dir
## şimdi person.json  dosyasından bilgileri alıp yazdıralım.

# with open('person.json') as f:
#     data=json.load(f)  ## strin bilgiyi dictinary list yaptık [loads objeden,, load dosyadan alırken]
#     print(data)
#     print(data['name'])


################################################################
## şimdide dictinary bilgiyi string yapalım

# person={"name":"ali","angauges":["python","c#"]}
# result=json.dumps(person)  # dictinary listi string yapar dumps 
# print(result)

##NOT: burada dumps s'li olanı kullandık çünkü dosyaya kaydetme yapmıyoruz
## sadece dosyaya kaydedilebilir hale getirmek istiyoruz aşağıdaki örnekte ise
## dosyaya kaydedeceğimizden dump metodunu kullanıypruz s'siz olanı !!!!

#################################################################
## şimdide dictinary bilgiyi string yapıp dosya içine yazdıralım.

person={"name":"ali","langauges":["python","c#"]}  ## dictinary list
with open("person.json","w") as f:
    json.dump(person, f)
