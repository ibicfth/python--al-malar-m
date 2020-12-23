import re  # arama krtiterleri ile ilgili  

str='Python kursu:python programlama rehberiniz | 490 saat'

result=re.findall('python',str)  # büyük küçük dikkat et, str de python u arar ve liste yapar.

result=re.split(' ',str)  # str deki ifadeleri boşluklardan böler, listede gösterir

result=re.sub(' ','-',str) # str içindeki boslukları - ile değştirir.

###boşluk belirtmek için ' ' yerine '\s' diyebilirz.

result=re.search('python',str) # arama yapar ve kaçıncı index ten kaçıncı indexe kadar olduğu belirten match objesi oluşturur.
## ilk bulduğu ifade için yapar sadece sonrakilere bakmaz
#oluşan match objesinin  hangi indexle hangi inedex arasında olduğunu span ile buluruz
result=result.span() 

####findall  [] köşeli parantez içine yazılan bütün karakterleri arar.
result=re.findall('[stk]',str)

#belli bir aralıktakini aratmak için - kullanırız.[ - ]
result=re.findall('[a-k]',str)
result=re.findall('[0-4]',str)

## yalnız [0-49] 0 dan 49 a kadar aramaz 0 dan 4 e kadar arar 9'u da haricen arar .
result=re.findall('[0-49]',str)

result=re.findall('[^abc]',str) # ^ ifadesi hariç anlamındadır. abc dışındaki karakterleri arar.

result=re.findall('[^0-9]',str) # 0 dan 9 kadar rakam haricindeki karakterleri arar.

'''
.  = tek nokta tek karakterleri aratır.
.. = çift karakterleri aratır.
 örnek  .. =>a  : iki karakter olmadığına bişey bulamaz
            ab  : ab sonucunu döndürür.
            abc : arama yaptığında sonuc ab döndürür. (ikişer ikişer gider)
            abcd:  arama yaptığında sonuc abcd döndürür. (ikişer ikişer gider)
            

'''
result=re.findall('ab','abc')
result=re.findall('ab',str)


''' 
^ karakteri ile başlıyanı en başı getirir. yukardaki ile karıştırma bunda [] kullanılmaz
^a a ile başlıyormu dmek
'''
result=re.findall('^P',str)

''' 
$  karakteri ile bitiyorsa  getirir. 
a$ a ile biterse liste olarak döndürür.
'''

result=re.findall('t$',str)
result=re.findall('saat$',str)

'''
x* => x ten 0 yada çok kere
        sa*t  = a dan o yada çok kere olanları arar ve a dan sonra t gelecek. saaaaaaat olabilir mesela

x+ => x ten en az 1 ve çok kere 
        sa+t = a dan en az bir yada çok kere olanları döndürür.

x? => x ten sadece 0 yada 1 kere , daha fazla olursa bulamaz.
        sa?t = budurumda bulamaz çünkü saat 'te 2 tane a var.0yada 1 kere olabilri sadece
        
'''

result=re.findall('sa*t',str)
result=re.findall('sa+t',str)
result=re.findall('sa?t',str)

'''
| ifadesi yada anlamındadır.
a|b = a yada b yi arar
'''

result=re.findall('a|b',str)


'''
() grublama yaparken kullanılır.
(a|b|c)xz  => demek axz yada bxz yada cxz olabilir.

'''

'''
özel karakter aramak için  \ kullanılır ve bundan sonraki yazanlar normal karakter olarak değerlendirirlir
\$a => $a karakterini arar sadece a yı aramaz artık $ yi karakter sayar ve $a yı arar.

'''

'''
\A  = verilen bi ifade  baştamı diye aratır.
        \Athe => the ifadesin ile mi başlıyor aratır.

\Z = sonra mi die bakar.
        \Zmi? => ifade mi? ile bitiyor bulup geitrir.

\b = belirtilen karakter kelimenin başındamı sonunda mı bakar.

\B =belirtilen karakter kelimenin başında sonunda değil mi die bakar

\d = [0-9] ile aynı anlamda yani 0 dan 9 a arama yapar.

\D =[^0-9] ile aynıdır yani 0 ve 9 arasına olmayan rkam olmayan karakterleri arar.

\s = boşluk karakterlerini arar
\S = boşluk karakterleri dışındakileri arar.
\w = alfabetik akrakterleri arar.
\W = alfabetik olmayan karakterleri arar.


daha fazlasını python RegEx die aratıp bulabilirz.
'''


print(result)

