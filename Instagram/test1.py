from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import pyautogui
import os
import shutil
from cv2 import cv2
import random
import sys
# sys.path.append('/home/seluser/python/utils')
sys.path.append('/Users/Hai/github/python/utils')
from util import login

# from dotenv import load_dotenv

chrome_options = Options()
shopifyImages = {}

class Oberlo:
    def __init__(self, url, username, pw):
        self.driver = login(self, url, username, pw)

    def fillProduct(self):
        # change title 
        #products = self.driver.find_elements_by_css_selector("div.import-products")

        

        # Find all products from page 
        products = self.driver.find_element_by_xpath("//div[@class=\"import-products\"]")
        productList = products.find_elements_by_xpath("//div[@class=\"panel import-product\"]")
        
        # loop through each product and edit every product 
        for product in productList: 

            product.find_element_by_xpath('//span[contains(text(), "Description")]').click()
            sleep(2)

            # create Material Text 
            textarea = product.find_element_by_xpath('//iframe[@class=\"tox-edit-area__iframe\"]')
            
            self.driver.switch_to.frame(textarea)
            text = self.driver.find_element_by_xpath('//p')
            print(text)

            # find materials 
            materials = text.find_elements_by_xpath('.//strong[contains(text(), "Material:")]')
            print(materials)
            # create a overall p tag 

            # delete old p tag from body 
           
            # create HTML elements for these 

            textarea = self.driver.find_element_by_xpath('//body[@id=\"tinymce\"]')

            self.driver.execute_script("""
                //create overall tag 
                var p = document.createElement('p')

                // for each material do that the following 

                arguments[0].forEach((material) => {
                    // create a Material Tag 
                    var materialTag = document.createElement("STRONG")
                    var materialText= document.createTextNode("Material: ")
                    materialTag.appendChild(materialText)

                    var textNode = document.createTextNode(material.nextSibling.textContent)
                    var br = document.createElement("br");
                    // append to p tag 
                    p.appendChild(material)
                    p.appendChild(textNode)
                    p.appendChild(br)
                })

                var element = arguments[2]
                element.parentNode.removeChild(element)

                arguments[1].appendChild(p)

                                        
                """, materials, textarea, text)

            # delete old p tag from body 


            # append new p tag to body 

            textarea = self.driver.find_element_by_xpath('//body[@id=\"tinymce\"]').click()

            break




oberlo = Oberlo('app.oberlo.com', 'cottagecoreoutfit@gmail.com', 'Wassermann2001')
sleep(4)
oberlo.fillProduct()
        
        

# create Material Text  - DEPRECEATED
            textarea = product.find_element_by_xpath('//iframe[@class=\"tox-edit-area__iframe\"]')
            
            self.driver.switch_to.frame(textarea)
            text = self.driver.find_element_by_xpath('//p')
            print(text)

            text.find_element_by_xpath('//strong[contains(text(), "Material:")]')
            material = self.driver.execute_script("""
                return arguments[0].nextSibling.textContent
            """, text)
            print(material)

            self.driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, text)

            
            textarea = self.driver.find_element_by_xpath('//body[@id=\"tinymce\"]')
            self.driver.execute_script("""
            var textField = document.createElement("p")
            var material = document.createElement("STRONG")
            var materialText= document.createTextNode("Material: ")
            material.appendChild(materialText)
            var textNode = document.createTextNode(arguments[1])
            textField.appendChild(material)
            textField.appendChild(textNode)   
            arguments[0].appendChild(textField)
            """, textarea, material)

            sleep(2)
