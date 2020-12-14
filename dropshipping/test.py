from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import os
import shutil
from cv2 import cv2
import random

# from dotenv import load_dotenv

chrome_options = Options()

class Oberlo:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.aliexpress.com/item/32828068983.html?af=465576&utm_campaign=465576&aff_platform=portals-tool&utm_medium=cpa&dp=e22588da7fcb727f8e1840af32db72dd&cv=47843&mall_affr=pr3&sk=_ePNSNV&aff_trace_key=0b32650d9a1e45a4b172e4bb0011b417-1607799413780-07511-_ePNSNV&terminal_id=0d66cd9ad3944dab8bf7f7624df6ee46&tmLog=new_Detail&utm_source=admitad&utm_content=47843")
        sleep(2)
        SCROLL_PAUSE_TIME = 1
        i = 0
        last_height = 0
        new_height = self.driver.execute_script("return document.body.scrollHeight")
        print(new_height)
        while True:
            last_height += 300
            self.driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
            sleep(SCROLL_PAUSE_TIME)
            if last_height == new_height:
                break
            i += 1
            if i == 7:
                break
            print(i)
        sleep(4)
        
        self.driver.find_element_by_xpath('//span[contains(text(),"SPECIFICATIONS")]').click()
        specifications = self.driver.find_element_by_xpath('//div[@class=\"product-specs\"]')
        element= specifications.find_element_by_xpath('.//span[contains(text(),"Material")]')
        print(element.get_attribute('class'))
        material = self.driver.execute_script("return arguments[0].nextSibling", element).text
        print(material)

        # create Material Text 
        textarea = self.driver.find_element_by_xpath('//body[@class=\"mce-content-body\"]/p')
        self.driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, textarea)

        textarea = self.driver.find_element_by_xpath('//body[@class=\"mce-content-body\"]')
        self.driver.execute_script("""
        textField = document.createElement("p")
        material = document.createElement("STRONG")
        materialText= document.createTextNode("Material")
        material.appendChild(materialText)
        textNode = document.createTextNode(material)
        textField.appendChild(material)
        textField.appendChild(textNode)
        arguments[0].appendChild(textField)
        """, textarea)
        






oberlo = Oberlo()

        
        

