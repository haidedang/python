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
import counter
import pickle
from random import randint
import pandas as pd
import usersDB

# from dotenv import load_dotenv

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--disable-dev-shm-usage')      

 

def moveFile(folder, dest):
    folderPath = os.getcwd()+ '/Instagram/' + folder
    print(folderPath)
    for filename in os.listdir(folderPath):
        img = cv2.imread(os.path.join(folderPath,filename))
        if img is not None:
            print(filename)
            # dest = /posting or /finished
            shutil.move(os.path.join(folderPath,filename), os.getcwd() + '/Instagram/' + dest)
            print(os.path.join(folderPath,filename), os.getcwd() + '/Instagram/' + dest)
            break

def sloganGenerator():
    # load the counter 
    obj = counter.loadState('counter.pickle')

    print(slogans[obj.counterSlogan])  
    instaCaption = slogans[obj.counterSlogan]

    obj.counterSlogan += 1

    counter.saveState(obj)

    return instaCaption


hashTags = "#cottagecore #cottagecoreaesthetic #witchy #mushroom #botanicalillustration #tarotcards #cottage #katharsis #cabincore #aesthetic #flowers #forest #forestlover #ceramics #meadow #nature #lemontree #fruitbasket #naturewitch #moodboard #moodboardaesthetic #naturelovers #retro #vintageaesthetic #retroaesthetic #fairycore #cottagecoreaesthetic #farmcore #grandmacore #countryside #arthoe #plantcore #angelcore #softcore #forestcore #lovecore #forestnymph #softgirl #morikei #warmcore #fairycore #fairycoreaesthetic #faeriecore #honeycore #warmaesthetic #cloudaesthetic #aestheticallypleasing #myaesthetic #cottagecore #cottagecoreaesthetic #cottagecorefashion #cottagecorestyle #vintagedresses #fairyfashion #princessdress #princessdresses #praerigirl #morikei #morigirl #farmcoreaesthetic #farmcore"
essentialHashTags= "#cottagecore #cottagecoreaesthetic #cottage #aesthetic #moodboardaesthetic #vintageaesthetic #cottagecore #cottagecoreaesthetic #cottagecorefashion #cottagecorestyle #vintagedresses #fairyfashion #princessdress #princessdresses #praerigirl #morikei #morigirl #farmcoreaesthetic #farmcore"
slogans = [ "WEAR or TEAR?", "SHOP or FLOP?", "TAKE or TOSS?", "Rate this outfit from 1-10!", "YAY or NAY?"]
comments = ["Amazing.", "So lovely <3", "I love this", "Wow <3" ]

prev_user_list = []

users = usersDB.loadState()
print('users', users)

arr = hashTags.split() 
mySet = list(set(arr))

#print(random.choice(mySet))

essentialHashTags = list(set(essentialHashTags.split()))
print(essentialHashTags)
def hashTagSelector(hashtags):
    result= []
    for i in range(0,20):
        element = random.choice(hashtags)
        if element not in result:
            result.append(element)
            #print(result)
    return " ".join(result)
  

# hashTagSelector(mySet)
        
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
            sleep(4) 
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

    def postPicture(self):
        try:  
            self.driver.find_element_by_xpath("//div[@data-testid=\"new-post-button\"]")\
            .click()
        except NoSuchElementException:
            pass
        sleep(4)

        pyautogui.FAILSAFE= False

        #move first file of folder images to posting folder
        moveFile('images','posting')
        
        #select Instagram folder 
        pyautogui.moveTo(200, 105)
        sleep(2)
        pyautogui.doubleClick()
        sleep(2)

        #select posting folder , delay to the bottom because of pycache
        pyautogui.moveTo(217, 185)
        sleep(2)
        pyautogui.doubleClick()
        sleep(2)

        # show file extensions
        pyautogui.moveTo(1056, 772)
        sleep(2)
        pyautogui.click()
        pyautogui.moveTo(1039, 805)
        sleep(2)
        pyautogui.click()
        
        #select File 
        pyautogui.moveTo(200, 105)
        sleep(2)
        pyautogui.click()

        #open File
        pyautogui.moveTo(1084, 826)
        sleep(2)
        pyautogui.click()

        sleep(8)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Next')]").click()
        sleep(4)
        
        self.driver.find_element_by_xpath("//textarea[@autocomplete=\"off\"]")\
            .send_keys(sloganGenerator() + "\n" + "\n" + hashTagSelector(mySet))
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Teilen')]").click()
        except NoSuchElementException:
            try: 
                self.driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()
            except NoSuchElementException:
                pass
        sleep(4)
    
        moveFile('posting','finished')
        print("success")    

    def followUsers(self): 
        i=0 
        for hashtag in essentialHashTags:
            hashtag = hashtag[1:]
            print(hashtag)
            self.driver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
            sleep(5)
            first_thumbnail = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
            first_thumbnail.click()
            sleep(2)

            """  try: """
            # click liked by users button
            section = self.driver.find_element_by_xpath("//section[@class='EDfFK ygqzn']")
            section.find_element_by_xpath(".//button").click()

            last_height = 0
            
            while True:
                # save usernames in object 
                #  usernames = self.driver.find_elements_by_xpath('//div[@class="_1XyCr"]/div[position()=2]/div/div/*')
                # sleep(3)
                # print(usernames)
                sleep(1)
                global users
                users = self.driver.execute_script("""
                obj = {}
                var list =  document.querySelector('._1XyCr div:nth-child(2) div div').children
                for (i = 0; i < list.length; i++) {
                    var title =  list[i].querySelector('div:nth-child(2) div div span a').getAttribute('title')
                    if (arguments[0][title] == undefined ){
                        arguments[0][title] = false
                    }   
                }
                return arguments[0]
                """, users)
                print(users)
                last_height = last_height + 1000
                container = self.driver.find_element_by_xpath('//div[@class="_1XyCr"]/div[position()=2]/div')
                self.driver.execute_script("arguments[1].scrollTo(0, arguments[0]);", last_height, container)
                sleep(1)
                new_height = self.driver.execute_script("return arguments[0].scrollHeight", container)
                i +=1
                if i==15:
                    break
                if new_height == last_height:
                    break
            
            for k, v in users.items():
                if users[k]== True:
                    print('user has already been commented')
                    continue
                print(k)
                self.driver.switch_to.window(self.driver.window_handles[0])
                sleep(7)
                self.driver.execute_script("window.open('','_blank');")
                sleep(2)
                self.driver.switch_to.window(self.driver.window_handles[1])
                sleep(2)
                self.driver.get("https://instagram.com/" + k + '/')
                sleep(2)
                try:
                    self.driver.find_element_by_xpath('//article[@class="ySN3v"]/div/div/div/div/a/div').click()
                    sleep(2)
                except NoSuchElementException:
                    print(NoSuchElementException)
                    pass
                
                try:
                    #like picture 
                    self.driver.execute_script("""
                        document.querySelector('svg[aria-label="Like"]').parentNode.click()
                    """)
                    # write a comment 
                except:
                    pass
                try:
                    self.driver.find_element_by_xpath('//textarea[@class="Ypffh"]').click()
                except NoSuchElementException:
                    print(NoSuchElementException)
                    pass
                sleep(2)
                try:
                    self.driver.find_element_by_xpath('//form[@class="X7cDz"]/textarea').send_keys(random.choice(comments))
                    sleep(2)
                    self.driver.find_element_by_xpath('//form[@class="X7cDz"]/textarea').send_keys(Keys.RETURN)
                    sleep(4)
                    print('commented and liked sucessfully')
                    users[k] = True
                    usersDB.saveState(users)
                except NoSuchElementException: 
                    print(NoSuchElementException)
                    pass
                self.driver.close()
            break
      
my_bot = InstaBot('cottagecorefashion', 'Wassermann2001') #not changing
my_bot.followUsers()

