from selenium import webdriver
from time import sleep
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(PATH)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]").click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()
        sleep(4)  
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(4)  
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(4)  
        
    def get_page(self) : 
        """ self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]")\
            .send_keys('aestheticcottagecore')
        sleep(4)
        self.driver.find_element_by_xpath("//a[@href=\"/aestheticcottagecore/\"]")\
            .click()
        sleep(4) """
        

    def get_post(self): 
        """ self.driver.find_element_by_xpath("//a[@href=\"/p/CHIv8KYJSlt/\"]")\
            .click()
        sleep(4) """
        self.driver.get("https://instagram.com/p/CG-at29gC_O/")
        sleep(4)
    
   
    def fetchComments(self): 
        old = 0
        count = [2,3,4]
        try:
            while self.driver.find_element_by_xpath("//span[@aria-label=\"Load more comments\"]"): 
                self.driver.find_element_by_xpath("//span[@aria-label=\"Load more comments\"]")\
                    .click()
                sleep(random.choice(count))
                """ count = links.length
                if old == count:
                    raise Exception("looping activated")
                else:
                    old = count  """
        except: 
            links =  self.driver.find_elements_by_tag_name("a")
            result = []
            for link in links:
                result.append(link.text)
                
                """ if '' in link.text:
                    links.remove(link)
                elif '#':
                    links.remove(link)
                else:
                    
                    print(link.text) """
            del links[-10:]
            result = list(filter(None, result))
            print("resultarray", result)
            print("length", len(result))
            """ for link in links:
                print(link.text)
                print("resultarray", result)
                print("length", len(result))
            
            print("resultarray", result)
            print("length", len(result)) """


        
my_bot = InstaBot('haidedang', 'Haidang91')

my_bot.get_post()
my_bot.fetchComments()
