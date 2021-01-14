from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import pyautogui
import os
import shutil
from cv2 import cv2
import random
import pickle
from random import randint
import usersDB
import urllib.request
from datetime import date
import datetime

# from dotenv import load_dotenv

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--disable-dev-shm-usage')    

hashTags="#nfp #finest #babeswithcurves #babesofinstagram #babesofinstagram #fitnessmotivation #fitness #fitnessgirl #beautifulgirl #brunettegirl #brunette #beautifulbrunette #beauty #beautiful #gorgeous #pretty #hot #classy #elegant #stylish #brunette #girl #lady #makeup #fashion #potd #ootd #hairstyle #outfit #pose #bubbles #2021  #newyear #eyes #lips #black #looks #instagirl #sensual #stunning" 
slogans = [ "WEAR or TEAR?", "SHOP or FLOP?", "TAKE or TOSS?", "Rate this outfit from 1-10!", "YAY or NAY?"]
referall= "Click on link in Bio to shop this dress! <3"
comments = ["Amazing.", "So lovely <3", "I love this", "Wow <3", "this is awesome", "simply beautiful <3", "lovely post"]
slogan= "like or nah?"

highQualityPictures = {
    "https://www.instagram.com/p/CGrkkoZjV5h/": True,
    "https://www.instagram.com/p/CJV6u_mjg5W/": True,
    "https://www.instagram.com/p/CJN5f6zDDx-/": False
}


arr = hashTags.split() 
mySet = list(set(arr))


def hashTagSelector(hashtags):
    result= []
    for i in range(0,20):
        element = random.choice(hashtags)
        if element not in result:
            result.append(element)
            #print(result)
    return " ".join(result)
  

posts = {}
users = {}
        
class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Akzeptieren')]").click()
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]").click()
            except NoSuchElementException:
                pass
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Anmelden')]").click()
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Log In')]").click()
            except NoSuchElementException:
                pass
        try:
            self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                .send_keys(username)
            self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                .send_keys(pw)
            self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
                .click()
            # sleep(4) 
        except NoSuchElementException:
            pass

        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Jetzt nicht')]").click()
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            except NoSuchElementException:
                pass
        sleep(4)  
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Abbrechen')]").click()
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Cancel')]").click()
            except NoSuchElementException:
                pass    
        sleep(4)  

        #### First TIme USage #####

        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Jetzt nicht')]").click()
        except NoSuchElementException:
            try: 
                self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            except NoSuchElementException:
                pass
                      

    def getUser(self, username, action):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.execute_script("window.open('','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get('https://www.instagram.com/'+ username + '/')
        sleep(3)
        action()
        sleep(2)
        self.driver.close()
    
    def deFollow(self):
        self.driver.execute_script("""
            document.getElementsByClassName('vBF20 _1OSdk')[0].children[0].click()
        """)
        sleep(2) 
        print('defollowed User')
        self.driver.execute_script("""
            document.getElementsByClassName('mt3GC')[0].children[0].click()
        """)
        sleep(2)

    def deFollowUsers(self, seconds):
        following = usersDB.loadState('following.pickle')
        # run once at the end of a day
        # today = datetime.date.today()
        today = datetime.date.today()
        weekBefore = today - datetime.timedelta(days=2)
        print(weekBefore)
        try:
            print('access week ago', following[str(weekBefore)])
            for elem in following[str(weekBefore)]: 
                print('enter loop')
                sleep(seconds)
                self.getUser(elem, self.deFollow)
            following[str(weekBefore)].append('defollowed')
            usersDB.saveState(following, 'following.pickle')
            print('defollowed All users from day')
        except:
            print('one week has not passed yet')

my_bot = InstaBot('hot__brunettes', 'Wassermann2001') #not changing

my_bot.deFollowUsers(20)