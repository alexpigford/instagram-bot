# dependencies for the bot
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# time.sleep() allows time for the page to load. without it the bot is too fast and can't find elements that are not loaded yet
import time

class InstagramBot():
    def __init__(self, username, password, bio):

# ------------------------------------------------------------------------------- #
# this is a hack - this is the location of my chromedriver locally. you will need to change this path
# chromedriver version must match chrome version
# https://chromedriver.chromium.org/downloads
# there are other ways to use chromedriver, like .install()
        self.browser = webdriver.Chrome('../../Downloads/chromedriver')
# ------------------------------------------------------------------------------- #
        self.username = username
        self.password = password
        self.bio = bio

    def signInAndClickAccount(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        time.sleep(3)

        usernameInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(3)

        notNow = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
        notNow.click()

        time.sleep(3)

        clickProfile = self.browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a")
        clickProfile.click()

        time.sleep(3)

    def editAccount(self):
        self.browser.get('https://www.instagram.com/' + self.username)

        time.sleep(5)

# the edit profile button would not work by copying the xpath. used class name instead
        clickEdit = self.browser.find_element_by_xpath("//button[@class='sqdOP  L3NKy _4pI4F   _8A5w5    ']")
        clickEdit.click()

        time.sleep(5)

        findBioTextArea = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[4]/div/textarea")
        findBioTextArea.clear()
        findBioTextArea.send_keys(self.bio)

        time.sleep(5)

        clickSubmit = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[10]/div/div/button[1]")
        clickSubmit.click()

        time.sleep(5)

        self.browser.get('https://www.instagram.com/' + self.username)

bot = InstagramBot('USERNAME', 'PASSWORD', 'I just used Python and Selenium to change this bio!')
bot.signInAndClickAccount()
bot.editAccount()
print('bot finished')
