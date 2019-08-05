from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()
    def login(self):
        bot =self.bot
        bot.get('https://twitter.com/login')
        sleep(5)
        user = bot.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
        password = bot.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
        user.clear()
        password.clear()
        user.send_keys(self.username)
        password.send_keys(self.password)

        sleep(4)
        log =bot.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
        log.click()
        sleep(6)

    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+ hashtag +'&src=typed')
        sleep(4)
        for i in range(1,4):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(2)
            tweets = bot.find_elements_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div[2]/div/div/div/div/div[2]/div/section/div/div/div/div[9]/div/div/article')
          
                           

ed = TwitterBot('noor.alam.619@gmail.com','superman1234')
ed.login()
ed.like_tweet('food')
