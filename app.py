from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(executable_path = '/Users/tigranmuradyan/downloads/geckodriver')

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)

    def scroll_reload(self, hashtag):
        bot = self.bot
        search = bot.find_element_by_class_name('r-1swcuj1')
        search.send_keys(hashtag)
        search.send_keys(Keys.RETURN)
        time.sleep(3)
        for i in range(1,5):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(5)
        bot.execute_script('window.scrollTo(document.body.scrollHeight, 0)')


tigran = TwitterBot('usr', 'pwd')
tigran.login()
tigran.scroll_reload('webdevelopment')