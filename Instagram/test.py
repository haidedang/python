from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import os

# from dotenv import load_dotenv

print('HI')
""" print (os.path.dirname(__file__))

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

PATH = os.getenv("MAC_CHROMEDRIVER")
print("Path",PATH)
 """


#driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',

                         # desired_capabilities = chrome_options.to_capabilities())

# driver = webdriver.Chrome(PATH, options=chrome_options)

"""Sets chrome options for Selenium.
Chrome options for headless browser is enabled.
"""
chrome_options = Options()
""" chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_prefs = {}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2} """


mobile_emulation = { "deviceName": "iPhone X" }
#chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        

class InstaBot:
    def __init__(self, username, pw):
        # self.driver = webdriver.Chrome(PATH, options=chrome_options)
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

        """  inputs = self.driver.find_elements_by_css_selector("input")
            print(inputs)
            element = inputs[-1]
            attrs = self.driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
            print(attrs) """
        
        """ print(os.getcwd()+"/images/0.png")
        print('input value:', element.get_attribute('value'))
        element.send_keys(os.getcwd()+"/images/0.png")
        inputs = self.driver.find_elements_by_css_selector("input")
        element = inputs[-1]
        print('input value:', element.get_attribute('value')) """
        
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Jetzt nicht')]").click()
        except NoSuchElementException:
            try: 
                self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            except NoSuchElementException:
                pass

        """ test = self.driver.execute_script('let forms = document.getElementsByTagName("form"); return forms')
        print(len(test)) 
        
        self.driver.execute_script(f'let forms = document.getElementsByTagName("form"); forms[{len(test) - 1}].submit(); ')
        sleep(4) """
        
     
        self.driver.find_element_by_xpath("//div[@data-testid=\"new-post-button\"]")\
           .click()
        sleep(4)
        
        # pick selenium folder
        pyautogui.moveTo(60, 160)
        sleep(2)
        pyautogui.click()

        # select images folder
        pyautogui.moveTo(200, 105)
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
       
        # pyautogui.write("/Users/Hai/github/python/Instagram/images/0.png") 
        # pyautogui.press('enter')

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
        print("success")
my_bot = InstaBot('johamovement', 'mpi91nv')

