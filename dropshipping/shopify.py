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

    def addTables(self): 
        productList = self.driver.find_element_by_xpath("//div[@class=\"Polaris-Page__Content_xd1mk\"]")
        productList = productList.find_elements_by_xpath(".//ul[@class=\"v0Su5 _3jLY9\"]/li")

        print(productList)

        # for all Products do the following 
        for product in productList:

            href = product.find_element_by_xpath(".//div[@testid=\"ProductTitles\"]/span/a").get_attribute('href')
            # open a new TAB 
            self.driver.execute_script("window.open('','_blank');")
            sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.driver.get(href)

            sleep(4)

            # contains list of image thumbnails 
            container = self.driver.find_elements_by_xpath("//div[@class=\"Polaris-DropZone__Container_13mbo\"]/div/div[position()=2]/*")
            print(container)
            # grap second last div 
            tablePicture = container[-2]
            tablePicture = tablePicture.find_element_by_xpath('.//button')
            self.driver.execute_script("""
                arguments[0].click()
            """, tablePicture)

            sleep(3) 

            downloadButton = self.driver.find_element_by_xpath("//button[@aria-label=\"Download\"]")
            self.driver.execute_script("""
                arguments[0].click()
            """, downloadButton)

            print('downloaded')

            sleep(2)

            closeButton = self.driver.find_element_by_xpath("//button[@aria-label=\"Close\"]")
            self.driver.execute_script("""
                arguments[0].click()
            """, closeButton)
            print('closed')
            sleep(2)

            # ---- EXTRACT TABLE FROM IMAGE --- 
            table = extract()

            #table = "<table><tr><td><p>Size(CM).</p></td><td><p>Length.</p></td><td><p>Bust</p></td><td><p>waist</p></td><td><p>Shoulder</p></td></tr><tr><td><p>S.</p></td><td><p>19.</p></td><td><p>86.</p></td><td><p>68.</p></td><td><p>37</p></td></tr><tr><td><p>M.</p></td><td><p>120.</p></td><td><p>90.</p></td><td><p>72</p></td><td><p>38.</p></td></tr><tr><td><p>L</p></td><td><p>2</p></td><td><p>94.</p></td><td><p>76.</p></td><td><p>39.</p></td></tr><tr><td><p>XL</p></td><td><p>22</p></td><td><p>98.</p></td><td><p>80.</p></td><td><p>40.</p></td></tr></table>"

            # ---- INSERT INTO TEXT AREA ----- 
            
           
            textarea = self.driver.find_element_by_xpath('.//iframe[@id=\"product-description_ifr\"]')
            
            self.driver.switch_to.frame(textarea)
            p = self.driver.find_element_by_xpath('//p')

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

            self.driver.execute_script(""" 
            var button = document.querySelector("[aria-label='Save']");
            button.click()
            """)
            sleep(6)

            self.driver.close()

            self.driver.switch_to.window(self.driver.window_handles[0])
            sleep(2)
            
shopify = Shopify('https://cottagecore-outfits.myshopify.com/admin/products?selectedView=all', 'cottagecoreoutfit@gmail.com', 'Wassermann2001')
sleep(2)
shopify.addTables()

extract()