

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
    #latest_file = '/Users/Hai/Downloads/sizeTable1.jpg'
    sizeTable = table_ocr.demo.main.extractTable(latest_file)

    print(sizeTable)

    return sizeTable

host = "https://cottagecore-outfits.myshopify.com"

class Shopify:
# open Shopify admin All Product view 
    def __init__(self, url, username, pw):
        self.driver = login(self, url, username, pw)

    def addTables(self): 
        productList = self.driver.find_element_by_xpath("//div[@class=\"Polaris-Page__Content_xd1mk\"]")
        productList = productList.find_elements_by_xpath(".//ul[@class=\"v0Su5 _3jLY9\"]/li")

        print(productList)

        # for all Products do the following 
        for product in productList:
        
            href = product.find_element_by_xpath(".//div[@testid=\"ProductTitles\"]/span/a").get_attribute('href')
            sleep(4)

            # open a new TAB 
            self.driver.execute_script("window.open('','_blank');")
            sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.driver.get(href)

            sleep(4)

            # ---- EXTRACT TABLE FROM IMAGE --- 
            table = extract()            

            # ---- INSERT INTO TEXT AREA ----- 
            
            self.driver.execute_script(""" 
            var button = document.querySelector("[aria-describedby='PolarisTooltipContent15']");
            button.click()
            """)
            sleep(2)

            text = self.driver.execute_script("""
                var desc = document.getElementById('product-description')
                var text ="<p><strong>Size Chart: </strong></p><br>" + arguments[0]
                return text
            """, table)

            self.driver.find_element_by_id('product-description').send_keys(text)

            sleep(2)
            self.driver.find_element_by_id('product-description').click()

            sleep(2)

            self.driver.execute_script(""" 
            var button = document.querySelector("[aria-describedby='PolarisTooltipContent17']");
            button.click()
            """)
            sleep(2)

            self.driver.execute_script(""" 
            var button = document.querySelector("[aria-label='Save']");
            button.click()
            """)
            sleep(6)

            self.driver.close()

            self.driver.switch_to.window(self.driver.window_handles[0])

            sleep(2)
            
            break


shopify = Shopify('https://cottagecore-outfits.myshopify.com/admin/products?selectedView=all', 'cottagecoreoutfit@gmail.com', 'Wassermann2001')
sleep(2)
shopify.addTables()




