from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import os
import shutil
from cv2 import cv2

# from dotenv import load_dotenv

chrome_options = Options()
mobile_emulation = { "deviceName": "iPhone X" }
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

def moveFile(folder, dest):
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            print(filename)
            # dest = /posting or /finished
            shutil.move(os.path.join(folder,filename), os.getcwd()+ '/' + dest)
            break
        
class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Akzeptieren')]").click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]").click()
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Anmelden')]").click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Log In')]").click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()
        sleep(4)  
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Jetzt nicht')]").click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
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

        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Jetzt nicht')]").click()
        except NoSuchElementException:
            try: 
                self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            except NoSuchElementException:
                pass
          
        self.driver.find_element_by_xpath("//div[@data-testid=\"new-post-button\"]")\
           .click()
        sleep(4)

        #move first file of folder images to posting folder
        moveFile('images','posting')
        
        # pick selenium folder
        pyautogui.moveTo(60, 160)
        sleep(2)
        pyautogui.click()

        # pyautogui.displayMousePosition()

        # select posting folder
        #pyautogui.moveTo(200, 105)
        pyautogui.moveTo(217, 154)
        sleep(2)
        pyautogui.doubleClick()

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

        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Next')]").click()
        sleep(4)
        self.driver.find_element_by_xpath("//textarea[@autocomplete=\"off\"]")\
            .send_keys("Am i not a cute motherfucker? #Pro #Sexy #Followme")
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Teilen')]").click()
        except NoSuchElementException:
            try: 
                self.driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()
            except NoSuchElementException:
                pass
        sleep(2)
    
        moveFile('posting','finished')
        print("success")

    


my_bot = InstaBot('johamovement', 'mpi91nv')

""" for i in range(378,792):
    shutil.move(os.path.join('images',f"{i}.png"), '/Users/Hai/Desktop/notProcessed') """

""" moveFile('images','posting')
sleep(2)
moveFile('posting', 'finished') """

            


