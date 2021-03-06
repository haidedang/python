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
import usersDB
import images
# from dotenv import load_dotenv

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--disable-dev-shm-usage')      
mobile_emulation = { "deviceName": "iPhone X" }
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
 

""" def moveFile(folder, dest):
    folderPath = os.getcwd()+ '/Instagram/' + folder
    print(folderPath)
    for filename in os.listdir(folderPath):
        img = cv2.imread(os.path.join(folderPath,filename))
        if img is not None:
            print(filename)
            # dest = /posting or /finished
            shutil.move(os.path.join(folderPath,filename), os.getcwd() + '/Instagram/' + dest)
            print(os.path.join(folderPath,filename), os.getcwd() + '/Instagram/' + dest)
            break """

def moveFile(folder, dest):
    folderPath = os.getcwd()+ '/' + folder
    print(folderPath)
    for filename in os.listdir(folderPath):
        img = cv2.imread(os.path.join(folderPath,filename))
        if img is not None:
            print(filename)
            # dest = /posting or /finished
            shutil.move(os.path.join(folderPath,filename), os.getcwd() + '/' + dest)
            print(os.path.join(folderPath,filename), os.getcwd() + '/' + dest)
            break

def sloganGenerator():
    # load the counter 
    obj = counter.loadState('counter.pickle')
    print(slogans[obj.counterSlogan])  
    instaCaption = slogans[obj.counterSlogan]
    obj.counterSlogan += 1
    counter.saveState(obj)
    return instaCaption


hashTags="#cottagecore #cottagecoreaesthetic #witchy #mushroom #botanicalillustration #tarotcards #cottage #katharsis #cabincore #aesthetic #flowers #forest #forestlover #ceramics #meadow #nature #lemontree #fruitbasket #naturewitch #moodboard #moodboardaesthetic #naturelovers #retro #vintageaesthetic #retroaesthetic #fairycore #cottagecoreaesthetic #farmcore #grandmacore #countryside #arthoe #plantcore #angelcore #softcore #forestcore #lovecore #forestnymph #softgirl #morikei #warmcore #fairycore #fairycoreaesthetic #faeriecore #honeycore #warmaesthetic #cloudaesthetic #aestheticallypleasing #myaesthetic #cottagecore #cottagecoreaesthetic #cottagecorefashion #cottagecorestyle #vintagedresses #fairyfashion #princessdress #princessdresses #praerigirl #morikei #morigirl #farmcoreaesthetic #farmcore" 
topHashTags = "#vintageaesthetic #grandmacore #arthoe #cottagecore #retro #warmaesthetic #cottagecorestyle #praerigirl #farmcoreaesthetic #ceramics #honeycore #botanicalillustration #vintagedresses #aestheticallypleasing #angelcore #softcore"
slogans = [ "WEAR or TEAR?", "SHOP or FLOP?", "TAKE or TOSS?", "Rate this outfit from 1-10!", "YAY or NAY?"]
referall= "Click on link in Bio to shop this dress! <3"
comments = ["Amazing.", "So lovely <3", "I love this", "Wow <3" ]


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
    
        #move first file of folder images to posting folder
        #moveFile('images','posting')
        pictureList = images.loadState()
        folderPath = os.getcwd()+ '/0images' 
        while True:
            myList = list(pictureList.keys())
            random.shuffle(myList)
            # print('list of keys', myList)
            fileName = random.choice(myList)
            print('randomFileName', fileName)
            if(pictureList[fileName]==True):
                print('picture has already been posted')
                continue
            print('old name ', fileName)
            newFileName= '0'+fileName
            print('new Name', newFileName)
            os.rename(os.path.join(folderPath,fileName), os.path.join(folderPath,newFileName))
            # posting it 
            if newFileName[0] == "0":
                print('pyautogui processing')
                self.post()
            else:
                continue
            # rename back for autogui since always selecting first element
            print('renaming back')
            os.rename(os.path.join(folderPath,newFileName), os.path.join(folderPath,fileName))
            print(fileName)
            pictureList[fileName] = True   
            images.saveState(pictureList) 
            print('selecting picture and setting to True', fileName, pictureList[fileName])
            # picture has been posted and save back -> exit loop
            break

        self.driver.find_element_by_xpath("//button[contains(text(), 'Next')]").click()
        sleep(4)
        
        self.driver.find_element_by_xpath("//textarea[@autocomplete=\"off\"]")\
            .send_keys(sloganGenerator() + "\n" + "\n" + referall + "\n" + "\n" + hashTagSelector(mySet))
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Teilen')]").click()
        except NoSuchElementException:
            try: 
                self.driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()
            except NoSuchElementException:
                pass
        sleep(4)
        # moveFile('posting','finished')
        print("success")   
        sleep(4)
       # self.driver.close() 
    
    def post(self):
        try:  
            self.driver.find_element_by_xpath("//div[@data-testid=\"new-post-button\"]")\
            .click()
        except NoSuchElementException:
            pass
        sleep(4)

        pyautogui.FAILSAFE= False

        # pyautogui.displayMousePosition()

        # show file extensions
        pyautogui.moveTo(1056, 772)
        sleep(2)
        pyautogui.click()
        pyautogui.moveTo(1039, 805)
        sleep(2)
        pyautogui.click()

        #select Instagram folder 
       # pyautogui.moveTo(200, 105)
        pyautogui.moveTo(65, 161)
        sleep(2)
        pyautogui.click()
        sleep(2)

        #
        # (214,106)

        #select posting folder , delay to the bottom because of pycache
        """ pyautogui.moveTo(217, 155)
        sleep(2)
        pyautogui.doubleClick()
        sleep(2) """

        #select File 
        pyautogui.moveTo(200, 105)
        sleep(2)
        pyautogui.doubleClick()

        #select File 
        pyautogui.moveTo(200, 105)
        sleep(2)
        pyautogui.click()

        #open File
        pyautogui.moveTo(1084, 826)
        sleep(2)
        pyautogui.click()

        sleep(8)
      
my_bot = InstaBot('cottagecorefashion', 'wassermann2001') #not changing
#my_bot.followUsers()

