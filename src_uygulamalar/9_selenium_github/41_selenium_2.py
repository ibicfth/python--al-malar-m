from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys ##enter,space tuşuna bastırmak için kullanılır
driver=webdriver.Chrome(executable_path='C:/Users/fatih/Desktop/python_temelleri/9_selenium/chromedriver.exe')

url='http://github.com'
driver.get(url) #driver url adresini getirir.

serchInput=driver.find_element_by_name("q") ##etiket altındaki name özelliğine(key) göre bulur 
##YUKARDAKİ KODU ŞU ŞEKİLDEDE YAPABİLİRİZ.
#serchInput=driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]")
# burada parantez içini chrome xpath copy oluşturdan aldık

time.sleep(2) 
serchInput.send_keys("python") ##send_keys ile searchinput(arama kutucusu) içine python nu yazdırır.
time.sleep(2)

serchInput.send_keys(Keys.ENTER)  ##send_keys ile searcinput arama kutucuğuna enter bilgisi gönderiyoruz.
time.sleep(3)


result=driver.find_elements_by_css_selector(".v-align-middle") ##css kodları ile driver verilen etiketler altındaki yeri bulur
## v-align-middle  bu a classının ismi <a class='v-align-middle'
for element in result:
    print(element.text)  ##bulunananların textlerini yazdırır.

driver.close()