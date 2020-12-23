from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:/Users/fatih/Desktop/python_temelleri/9_selenium/chromedriver.exe')
url='https://www.github.com/'

driver.get(url) #sayfayı açar
 
time.sleep(2) #2 saniye bekler
driver.maximize_window() #sayfayı tam ekran yapar
driver.save_screenshot('9_selenium/screenshot.png')

url='https://www.github.com/sadikturan'
driver.get(url)

print(driver.title) # sayfa başlığını yazar
driver.save_screenshot('9_selenium/screenshot.png')

time.sleep(2) #2saniye bekler
driver.back() # sayfayı geri alır, ileri almak için forward()
time.sleep(2)

driver.close() # kapatır.

