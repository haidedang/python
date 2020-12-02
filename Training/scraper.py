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
        store = {}
        i = 0 
        tracker=[]

        try:
            while self.driver.find_element_by_xpath("//span[@aria-label=\"Load more comments\"]"): 
                self.driver.find_element_by_xpath("//span[@aria-label=\"Load more comments\"]")\
                    .click()
                sleep(2)
                links =  self.driver.find_elements_by_tag_name("a")
                for element in links:
                    if element.text == '':
                        continue
                    try:
                        store[element.text]
                        tracker.append(True)
                        i = i +1 
                        difference =  len(tracker) - store[list(store)[-1]] 
                        if difference > 200:
                            print('infinite loop')
                            print(store)
                            print (tracker)
                            print (store[list(store)[-1]])
                            print (len(tracker))
                            endresult = list(store.keys())
                            return endresult
                        continue
                    except:
                        tracker.append(False)
                        store[element.text] = i + 1 
                        i = i + 1 
        except: 
            print('done')
            print(store)
            print (tracker)
            print (store[list(store)[-1]])
            print (len(tracker))
            return list(store.keys())

    def cleanComments(self, comments):
        for comment in list(comments):
            if comment[0] == '#':
                comments.remove(comment)
            if comment[0].isupper():
                comments.remove(comment)
            if len(comment)<=2:
                comments.remove(comment)
        return comments    
        
my_bot = InstaBot('haidedang', 'Haidang91')

my_bot.get_post()
comments = my_bot.fetchComments()
cleanComments = my_bot.cleanComments(comments)

print(cleanComments)
print(len(cleanComments))