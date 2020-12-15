import glob
import os
import table_ocr.demo.main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import pyautogui
import shutil
from cv2 import cv2
import random
import sys
# sys.path.append('/home/seluser/python/utils')
sys.path.append('/Users/Hai/github/python/utils')
from util import login
import pickle

def extract():
    # get latest downloaded file from downloads 
    list_of_files = glob.glob('/Users/Hai/Downloads/*.jpg') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)

    # extract tables from image 
    sizeTable = table_ocr.demo.main.extractTable(latest_file)

    print(sizeTable)

    return sizeTable

host = "https://cottagecore-outfits.myshopify.com"

class Shopify:
# open Shopify admin All Product view 
    def __init__(self, url, username, pw):
        self.driver = login(self, url, username, pw)

    def openProductInNewTab(self, url):
        self.driver.execute_script("window.open('','_blank');")
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(url)
        sleep(4)
    
    def selectTablePicture(self, instance):
        # contains list of image thumbnails 
        sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[1])
        container = self.driver.find_elements_by_xpath("//div[@class=\"Polaris-DropZone__Container_13mbo\"]/div/div[position()=2]/*")
        print(container)
        print(instance.driver.find_elements_by_xpath("//div[@class=\"Polaris-DropZone__Container_13mbo\"]"))
        
        # grap second last div and open it 
        tablePicture = container[-2]
        tablePicture = tablePicture.find_element_by_xpath('.//button')
        instance.driver.execute_script("""
            arguments[0].click()
        """, tablePicture)
        sleep(3)
        

    def addHtmlTable(self):
        self.selectTablePicture()
        # download the picture 
        self.clickButton('Download')
        self.clickButton('Close')

        # ---- EXTRACT TABLE FROM IMAGE --- 
        table = extract()

        # ---- INSERT INTO TEXT AREA ----- 
        textarea = self.driver.find_element_by_xpath('.//iframe[@id=\"product-description_ifr\"]')
        self.driver.switch_to.frame(textarea)
        p = self.driver.find_element_by_xpath('//p')

        # Add HTML Table 
        text = self.driver.execute_script("""
            // var desc = document.getElementById('product-description')
            var text = "<p>"+ arguments[1].innerHTML + "</p>" + "<p><strong>Size Chart: </strong></p><br>" + arguments[0]
            return text
        """, table, p)

        self.driver.switch_to.window(self.driver.window_handles[1])

        self.driver.execute_script(""" 
        var button = document.querySelector("[aria-describedby='PolarisTooltipContent15']");
        button.click()
        """)
        sleep(2)

        self.driver.find_element_by_id('product-description').send_keys(Keys.COMMAND + 'a')
        self.driver.find_element_by_id('product-description').send_keys(text)
        sleep(2)
        self.driver.find_element_by_id('product-description').click()
        sleep(2)

    def checkForTable(self): 
        textarea = self.driver.find_element_by_xpath('.//iframe[@id=\"product-description_ifr\"]')
        print('textarea', textarea)
        self.driver.switch_to.frame(textarea)
        #check if table exist

        try:
            self.driver.find_element_by_xpath('//table')
            print('table', self.driver.find_element_by_xpath('//table') )
            # if it exists delete the picture 
            return True
        except NoSuchElementException:
            return False


    # argument: 'Download' , 'Close', 'Save' or 'Delete' 
    def clickButton(self, action):
        # download the picture 
        button = self.driver.find_element_by_xpath("//button[@aria-label='"+action+"']")
        self.driver.execute_script("""
            arguments[0].click()
        """, button)
        print(action)
        sleep(2)

    def executeProduct(self, url, action):
        # open a new TAB 
        self.openProductInNewTab(url)            

        # Add HTML Table or delete second picture 
        action(self)

        # Save the Product 
        self.driver.execute_script(""" 
        var button = document.querySelector("[aria-label='Save']");
        button.click()
        """)
        sleep(6)

        self.driver.close()

        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)


    def addTables(self): 
        productList = self.driver.find_element_by_xpath("//div[@class=\"Polaris-Page__Content_xd1mk\"]")
        productList = productList.find_elements_by_xpath(".//ul[@class=\"v0Su5 _3jLY9\"]/li")

        print(productList)

        # for all Products do the following 
        for product in productList:

            href = product.find_element_by_xpath(".//div[@testid=\"ProductTitles\"]/span/a").get_attribute('href')
            self.executeProduct(href, self.addHtmlTable)

    def specificTable(self, name, action):
        product = self.driver.find_element_by_xpath("//a[@aria-label='"+name+"']")
        print(product.get_attribute('href'))
        # href = product.find_element_by_xpath(".//div[@testid=\"ProductTitles\"]/span/a").get_attribute('href')
        url = product.get_attribute('href')
        self.executeProduct(url, action)

    def deleteTables(self, instance):
        # Run through all products 
        # Check if html table exists  
        if self.checkForTable(): 
            # if it exists, delete the size table picture 
            self.selectTablePicture(instance)
            self.clickButton('Delete')
            sleep(3)
            self.driver.find_element_by_xpath('//span[contains(text(), "Delete media")]').click()
        return



shopify = Shopify('https://cottagecore-outfits.myshopify.com/admin/products?selectedView=all', 'cottagecoreoutfit@gmail.com', 'Wassermann2001')
sleep(2)
shopify.specificTable('Academia Girl Dress', shopify.deleteTables)
