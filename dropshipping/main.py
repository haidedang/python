from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

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
import pickle

# from dotenv import load_dotenv

chrome_options = Options()
shopifyImages = {}

i=0 

defaultObject= {
    "season": '',
    "neckline": '',
    "style": '',
    "patternType": '',
    "dressesLength": ''
}

page = 2 

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
        ## product Tab 
            # store title 
            title = product.find_element_by_xpath(".//div[@class=\"input-block product-main-tab__title-input\"]").get_attribute('value')

            # Set Collection 
            collection = product.find_element_by_xpath("//input[@id=\"ajaxCollections\"]")
            collection.send_keys('Cottagecore')
            sleep(2)
            collection.send_keys(Keys.ENTER)
            sleep(1)

            # paste content of fetchImagesFromWebsite
                
            # --DESCRIPTION ----
            product.find_element_by_xpath('.//span[contains(text(), "Description")]').click()
            sleep(2)

            # create Material Text 
            textarea = product.find_element_by_xpath('.//iframe[@class=\"tox-edit-area__iframe\"]')
            
            self.driver.switch_to.frame(textarea)
            text = self.driver.find_element_by_xpath('//p')
            print(text)

            # find materials 
            materials = text.find_elements_by_xpath('.//strong[contains(text(), "Material:")]')
            print(materials)

            try:
                season = text.find_element_by_xpath('.//strong[contains(text(), "Season:")]')
            except (NoSuchElementException, StaleElementReferenceException) :
                season = defaultObject["season"]
            try:
                neckline = text.find_element_by_xpath('.//strong[contains(text(), "Neckline:")]')
            except (NoSuchElementException, StaleElementReferenceException) :
                print('ERROR NO NECKLINE')
                neckline = defaultObject["neckline"]
            try:
                style = text.find_element_by_xpath('.//strong[contains(text(), "Style:")]')
            except (NoSuchElementException, StaleElementReferenceException) :
                style = defaultObject["style"]
            try:
                patternType = text.find_element_by_xpath('.//strong[contains(text(), "Pattern Type:")]')
            except (NoSuchElementException, StaleElementReferenceException) :
                patternType = defaultObject["patternType"]
            try:
                dressesLength = text.find_element_by_xpath('.//strong[contains(text(), "Dresses Length:")]')
            except (NoSuchElementException, StaleElementReferenceException) :
                dressesLength = defaultObject["dressesLength"]
            
            global i 
            if i==0:
                defaultObject["season"] = season
                defaultObject["neckline"] = neckline
                defaultObject["style"] = style
                defaultObject["patternType"] = patternType
                defaultObject["dressesLength"] = dressesLength

            textarea = self.driver.find_element_by_xpath('//body[@id=\"tinymce\"]')

            try:
                self.driver.execute_script("""
                    //create overall tag 
                    var overallTag = document.createElement('p')

                    var createTag = function (tag, strongText) {
                        var textNode = document.createTextNode(strongText.nextSibling.textContent)
                        var br = document.createElement("br");
                        // append to p tag 
                        tag.appendChild(strongText)
                        tag.appendChild(textNode)
                        tag.appendChild(br)
                        return tag 
                    }

                    // for each material do that the following 

                    arguments[0].forEach((material) => {
                        overallTag = createTag(overallTag, material)
                    })

                    overallTag = createTag(overallTag, arguments[3])
                    overallTag = createTag(overallTag, arguments[4])
                    overallTag = createTag(overallTag, arguments[5])
                    overallTag = createTag(overallTag, arguments[6])
                    overallTag = createTag(overallTag, arguments[7])
                
                    var element = arguments[2]
                    element.parentNode.removeChild(element)

                    arguments[1].appendChild(overallTag)
                                            
                    """, materials, textarea, text, season, neckline, style, patternType, dressesLength)
            except (NoSuchElementException, StaleElementReferenceException):
                pass

            textarea = self.driver.find_element_by_xpath('//body[@id=\"tinymce\"]').click()
            sleep(2)

            # switch back to window
            self.driver.switch_to.window(self.driver.window_handles[0])

            # ---VARIANTS -----

            product.find_element_by_xpath('.//span[contains(text(), "Variants")]').click()
            cost = product.find_element_by_xpath('.//div[@class=\"money-view\"]/div/span').text
            cost = cost[1:]
            price = round(float(cost) + 15) + 0.99
            fakePrice = 2* round(price) + 0.99
            print(price)

            # find input fields 
            tableBody = product.find_element_by_xpath('.//tbody')

            # get all tablerows 
            tableRows = tableBody.find_elements_by_xpath('.//tr')

            print(str(price))

            for row in range(1,len(tableRows)):
                inputValue = tableRows[row].find_element_by_xpath('.//div[@class=\"money-input variants-table__price\"]/div/div/div/input')
                inputValue.send_keys(Keys.COMMAND + 'a')
                inputValue.send_keys(str(price))
                inputValue.send_keys(Keys.TAB) 

                compareValue = tableRows[row].find_elements_by_css_selector("td")[9].find_element_by_css_selector('input')
                compareValue.send_keys(str(fakePrice))
                compareValue.send_keys(Keys.TAB)
            
            # IMAGES 

            # deselect image
            """ product.find_element_by_xpath('//span[contains(text(), "Images")]').click()
            sleep(2)
            product.find_element_by_xpath('.//div[@class=\"product-image__overlay\"]').click() """

            sleep(2)
            i += 1
            #Import to Store
            # product.find_element_by_xpath('.//button[@class=\"push-to-shop btn btn-primary btn-regular\"]').click()

    def runAllPages(self):
        global page
        while True:
            page += 1 
            number = str(page)
            try:
                self.driver.find_element_by_xpath("//button[@class='btn btn-basic btn-regular']/span/span[contains(text(), '"+number+"')]").click()
            except NoSuchElementException:
                print('No pages left')
                break
            sleep(4)
            self.fillProduct()
            sleep(2)


def fetchImagesFromWebsite():
    # check wether product is from Perfect Stranger 
    supplier = product.find_element_by_xpath("//span[@class=\"supplier-info__name\"]").text
    print('supplier')
    if supplier == "Perfect Stranger Official Store (AliExpress)":
        
        # store textarea in variable 

        # click on the Link to supplier 
        href = product.find_element_by_xpath(".//a[contains(text(), 'View original product')]").get_attribute('href')
        print(href)
        sleep(2)

        #open new tab 
        # self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
        self.driver.execute_script("window.open('','_blank');")
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])

        # click on the Link to supplier 
        self.driver.get(href)
        sleep(2)
        
        #open new tab   
        self.driver.find_element_by_xpath("//a[@class=\"product-info__product-link\"]").click()
        sleep(4)

        self.driver.switch_to.window(self.driver.window_handles[2])
        sleep(3)
        #url = self.driver.execute_script("""return window.location.href""")
        #print('success', url)

        #self.driver.get(url)
        #sleep(2)

        ##  images

        #save all url images to array   /product-description/img 
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
        imageDiv = self.driver.find_element_by_xpath('//div[@class=\"product-overview\"]')
        images = imageDiv.find_elements_by_xpath(".//img")
        imageSrc = []
        for image in images:
            src = image.get_attribute('src')
            imageSrc.append(src)
        
        shopifyImages[title] = imageSrc

        # Step 2
        with open('shopify.images', 'wb') as shopify_images_file:
            # Step 3
            pickle.dump(shopifyImages, shopify_images_file)

        print('storing images for product')
        print(shopifyImages)

        #get the Material 

        self.driver.find_element_by_xpath('//span[contains(text(),"SPECIFICATIONS")]').click()
        specifications = self.driver.find_element_by_xpath('//div[@class=\"product-specs\"]')
        element= specifications.find_element_by_xpath('.//span[contains(text(),"Material")]')
        print(element.get_attribute('class'))
        material = self.driver.execute_script("return arguments[0].nextSibling", element).text
        print(material)

        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(3)

oberlo = Oberlo('https://app.oberlo.com/import', 'cottagecoreoutfit@gmail.com', 'Wassermann2001')
sleep(4)
#oberlo.fillProduct()
oberlo.runAllPages()