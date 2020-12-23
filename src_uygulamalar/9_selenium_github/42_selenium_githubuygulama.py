from githubUserInfo import username,password  ##kendimiz githubUserInfo.py dosyasını modül oluşturduk
from selenium import webdriver
import time


class Github:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome(executable_path='C:/Users/fatih/Desktop/python_temelleri/9_selenium_github/chromedriver.exe')
        self.username=username
        self.password=password
        self.followers=[]
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[12]").click()

    def getFollowers(self):
        self.browser.get(f"https://github.com/sadikturan?tab=followers")
        time.sleep(2)

        item=self.browser.find_elements_by_css_selector(".d-table.table-fixed") ##takipçi sayfası

        for i in item:
            self.followers.append(i.find_element_by_css_selector(".link-gray").text) #css de (.) konarak yazılır. #takipçi isimlerini getirir.

        while True:
            links=self.browser.find_element_by_class_name("pagination").find_elements_by_tag_name("a")
## diğer sayfalardaki kullanıcılarıda eklemek için next yaptırıp yazdıralım.
            if len(links)==1:
                if links[0].text=='Next':
                    links[0].click()
                    time.sleep(1)
                    item=self.browser.find_elements_by_css_selector(".d-table.table-fixed") ##takipçi sayfası

                    for i in item:
                        self.followers.append(i.find_element_by_css_selector(".link-gray").text) #css de (.) konarak yazılır. #takipçi isimlerini getirir.
                else:
                    break
            else:
                for link in links:
                    if link.text=='Next':
                        link.click()
                        time.sleep(1)
                        item=self.browser.find_elements_by_css_selector(".d-table.table-fixed") ##takipçi sayfası

                        for i in item:
                            self.followers.append(i.find_element_by_css_selector(".link-gray").text)
                    else:
                        continue
                    

github=Github(username,password)
github.signIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)
