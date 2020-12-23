html_doc='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Web Sayfam</title>
</head>
<body>
 <h1 id='header'>
        Python Kursu
    </h1>
    
    <div class='grup_1'>
        <h2>
            programlama
        </h2>
        <ul>
            <li> Menu 1 </li>
            <li> Menu 2 </li>
            <li> Menu 3 </li>
        </ul>
    </div>

<div class='grup_2'>
        <h2>
            modüller
        </h2>
        <ul>
            <li> Menu 1 </li>
            <li> Menu 2 </li>
            <li> Menu 3 </li>
        </ul>
    </div>
div class='grup_3'>
        <h2>
            sınıflar
        </h2>
        <ul>
            <li> Menu 1 </li>
            <li> Menu 2 </li>
            <li> Menu 3 </li>
        </ul>
    </div>
    <img src="kivircik.jpg" alt="">




</body>
</html>

''' # bile bile html_doc içindeki bazı etiketlerin hizalarını bozduk ama aşağıdaki kodlar düzgünce getirecek.
from bs4 import BeautifulSoup

soup=BeautifulSoup(html_doc,'html.parser') ##nasıl bi denetleme parser ı kullanacağını belirtiyoruz.(html.parser  bu xml.parser da oalbilirdi.)

result=soup.prettify() ## bozduğumuz etiketlerin düzgün halini getirir.

result=soup.title ## title bilgisinin gelmesi için title çağırdık.

result=soup.head  ## head etiketini çağırdık

result=soup.body  # body etiketini çağırdık

result=soup.title.name  ## title etiketinin sadece etiket adını yani title getirir.

result=soup.title.string ## title etiketinin etiket olmadan sadece içeriğini gtirir.

result=soup.h1  # h1 getirir.

result=soup.h2  ## h2 den çok var(2 tane h2 etiketi var.) sadece ilkini getiri.

## bütün h2 etiketlerinigetirmek istiyorsak find_all methodu ile arama yapalım
result=soup.find_all('h2')  ## h2 etiketlerini dizi içinde geitrir


## ancak biz bu h2 etiketlerinden ikincini sadece istiyorsak index ile çağırırız
result=soup.find_all('h2')[1] # ikinci h2 etiketini geitirir.


#2 tane div etiketi var ve biz 2. divin ul etiketini çağıralım.
result=soup.find_all('div')[1].ul  ## ul etiketinin altında 3 tane li etiketi var
# bu 3 etiketi de hepsini yada indeks vererek istediğimiz çağırabiliriz.
result=soup.find_all('div')[1].ul.li # sadece ilki gelir
result=soup.find_all('div')[1].ul.find_all('li')[2] ##li etiketlerinin 3. sünü getirecek


#bir etiketin altındaki her etiketi getirmek için;
result=soup.div.findChildren()

##çok olan etiketlerden bir sonrakine geçmek için findnextsbling kullanılır
result=soup.find_all('h2') #sadece ilki gelir bir sonrakine
result=soup.h2.findNextSibling() #h2 den sonra gelen kardeş etiket ul etiketi onu getirir.
#bunu sona ekleye ekleye gideriz.
result=soup.div.findNextSibling().findNextSibling().findNextSibling()  ## gibi 

##yada bir sonraki etiketten bir öncekine geçmek için findprevioussibling kullanılır
result=soup.div.findNextSibling().findNextSibling().findPreviousSibling()


print(result)
