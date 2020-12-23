import requests
import json

result=requests.get("https://jsonplaceholder.typicode.com/todos")

print(result)
print(result.text)
print(type(result)) ## türü string olduğundan herhangi bi key in value değerini getirmek için json modulü kullanmak zorundayız.



result=json.loads(result.text) # dosyadan çevirseydik load derdik. bilgiler şimdi dictinary oldu key value yapabiliriz.
print(result[0]['title'])

print(result) # listenin hepsini getirir ama okunurluğu karmaşık olur

### for ile index index getirelim (eleman eleman)
for i in result:
    print(i)

### for ile her gelen elemanın sadece bir key valusunu getirmek için;
for i in result:
    print(i['title'])

### for ile her gelen elemanlarda filtreme yaptıktan sonra filtreden geçenlerin key valusunu getirmek için;
for i in result:
    if i['userId']==9:
        print(i['id'])  ##userId'si 9 olanların id key'ine karşılık gelen value larını getirirç
        