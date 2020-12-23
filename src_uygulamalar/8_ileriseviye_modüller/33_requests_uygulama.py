import requests
import json

api_url="https://api.exchangeratesapi.io/latest?base="

bozulan_doviz=input('bozulan döviz türü: ')#büyük harf gir
alınan_doviz=input('alınan döviz türü: ')#büyük harf gir
miktar=int(input(f"ne kadar {bozulan_doviz} bozdurmak istiyor sunuz: "))

result=requests.get(api_url + bozulan_doviz) 

result=json.loads(result.text) #textini almazsak sadece almanın başarılı olduğunu gösterir,biz textinin dictinary olmasını istiyoruz.

print("1 {} {} {}".format(bozulan_doviz,result['rates'][alınan_doviz],alınan_doviz))
print('toplam: {} {} alacaksınız.'.format(miktar*result['rates'][alınan_doviz],alınan_doviz))



