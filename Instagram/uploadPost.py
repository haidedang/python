from selenium import webdriver
from time import sleep
import os 
from selenium.common.exceptions import NoSuchElementException
import pyautogui

PATH = "C:\Program Files (x86)\chromedriver.exe"

mobile_emulation = { "deviceName": "iPhone X" }

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

#driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',

                         # desired_capabilities = chrome_options.to_capabilities())

# driver = webdriver.Chrome(PATH, options=chrome_options)


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(PATH, options=chrome_options)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Akzeptieren')]").click()
        except NoSuchElementException:
            pass
        self.driver.find_element_by_xpath("//button[contains(text(), 'Anmelden')]").click()
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
            pass
        sleep(4)  
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Abbrechen')]").click()
        except NoSuchElementException:
            pass    
        sleep(4)  
        self.driver.find_element_by_xpath("//input[@type=\"file\"]")\
            .send_keys(os.getcwd()+"\images\photo.jpg")
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Jetzt nicht')]").click()
        sleep(4)  
        self.driver.find_element_by_xpath("//div[@data-testid=\"new-post-button\"]")\
            .click()
        sleep(4)
        pyautogui.write(r'C:\Users\lee Stone\Desktop\dev\Python\Instagram\images\photo.jpg') 
        pyautogui.press('enter')
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Weiter')]").click()
        sleep(4)
        self.driver.find_element_by_xpath("//textarea[@autocomplete=\"off\"]")\
            .send_keys("Am i not a cute motherfucker? #Pro #Sexy #Followme")
        self.driver.find_element_by_xpath("//button[contains(text(), 'Teilen')]").click()
        sleep(2)

# my_bot = InstaBot('johamovement', 'mpi91nv')

