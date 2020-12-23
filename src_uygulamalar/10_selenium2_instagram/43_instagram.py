from instagramUserInfo import username,password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Instagram:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome(executable_path='C:/Users/fatih/Desktop/python_temelleri/10_selenium2_instagram/chromedriver.exe')
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
       
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)

        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(3)

    def followers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        dialog=self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followersCount=len(dialog.find_elements_by_css_selector("li"))
        print(f"first count: {followersCount}")

        action=webdriver.ActionChains(self.browser)
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount=len(dialog.find_elements_by_css_selector("li"))

            if followersCount < newCount:
                followersCount = newCount
                print(f"second count: {newCount}")
                time.sleep(2)
            
            else:
                
                break


        followers=dialog.find_elements_by_css_selector("li")

        for user in followers:
            links=user.find_element_by_css_selector("a").get_attribute("href")
            print(links)





instagram=Instagram(username,password)
instagram.signIn()
instagram.followers()




