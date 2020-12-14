from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import os

# from dotenv import load_dotenv

print('HI')

chrome_options = Options()
mobile_emulation = { "deviceName": "iPhone X" }
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        

class InstaBot:
    def __init__(self, username, pw):
        # self.driver = webdriver.Chrome(PATH, options=chrome_options)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)

       
        screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
           
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        pyautogui.displayMousePosition()

        # pyautogui.write("/Users/Hai/github/python/Instagram/images/0.png") 
        # pyautogui.press('enter')

        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Next')]").click()
        sleep(4)
        self.driver.find_element_by_xpath("//textarea[@autocomplete=\"off\"]")\
            .send_keys("Am i not a cute motherfucker? #Pro #Sexy #Followme")
        self.driver.find_element_by_xpath("//button[contains(text(), 'Teilen')]").click()
        sleep(2)
        print("success")
my_bot = InstaBot('johamovement', 'mpi91nv')

