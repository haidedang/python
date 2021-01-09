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
success = {}
products = {}

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
    
    def selectTablePicture(self):
        # contains list of image thumbnails 
        sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[1])
        container = self.driver.find_elements_by_xpath("//div[@class=\"Polaris-DropZone__Container_13mbo\"]/div/div[position()=2]/*")
        print(container)        
        # grap second last div and open it 
        tablePicture = container[-2]
        tablePicture = tablePicture.find_element_by_xpath('.//button')
        self.driver.execute_script("""
            arguments[0].click()
        """, tablePicture)
        sleep(3) 

    def addHtmlTable(self, url):
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

        # switch from fram back to windows 
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

    def archiveTable(self,url):
        if self.checkForTable():
            print('table exists')
        else:
            # Archive Product
            print('nothing')
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.find_element_by_xpath('//span[contains(text(), "Archive product")]').click()
            sleep(2)
            self.driver.find_element_by_xpath('//button[@class="Polaris-Button_r99lw Polaris-Button--newDesignLanguage_1rik8 Polaris-Button--primary_7k9zs"]/span/span[contains(text(), "Archive product" )]').click()
            sleep(4)

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
        action(url)

        # Save the Product 
        try:
            self.driver.execute_script(""" 
            var button = document.querySelector("[aria-label='Save']");
            button.click()
            """)
            sleep(6)
        except:
            pass

        self.driver.close()

        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)

    def getAllProducts(self):
        productList = self.driver.find_element_by_xpath("//div[@class=\"Polaris-Page__Content_xd1mk\"]")
        productList = productList.find_elements_by_xpath(".//ul[@class=\"v0Su5 _3jLY9\"]/li")
        return productList
       
    def addTables(self):
        # select all entries with active status  
        self.driver.find_element_by_xpath("//a[@id='archived']").click()
        sleep(2)

        productList = self.getAllProducts()

        while True:
            # for all Products do the following 
            for product in productList:

                href = product.find_element_by_xpath(".//div[@testid=\"ProductTitles\"]/span/a").get_attribute('href')
                self.executeProduct(href, self.addHtmlTable)
            sleep(4)
            self.driver.find_element_by_xpath('//button[@aria-label="Next"]').click()
            sleep(4)

    def changeVendors(self):
        self.driver.find_element_by_xpath("//a[@id='all']").click()
        sleep(2)
        self.driver.execute_script("""
            Array.from(document.querySelectorAll('span[class="Polaris-Button__Text_yj3uv"]')).find(el => el.textContent === 'Product vendor').click();
        """)
        sleep(2)
        self.driver.find_element_by_xpath("//span[@class='Polaris-Choice__Label_2vd36' and contains(text(), 'Cottagecore Outfits')]").click()
        sleep(4)
        productList = self.getAllProducts()
        for product in productList:
                href = product.find_element_by_xpath(".//div[@testid=\"ProductTitles\"]/span/a").get_attribute('href')
                self.executeProduct(href, self.changeVendor)

    def changeVendor(self, url):
        inputField = self.driver.find_element_by_xpath("//input[@value='Cottagecore Outfits']")
        inputField.send_keys(Keys.COMMAND + "a")
        inputField.send_keys("Cottagely")
        inputField.send_keys(Keys.RETURN)

    def archiveTables(self):
        self.driver.find_element_by_xpath("//a[@id='active']").click()
        sleep(2)

        productList = self.getAllProducts()
        # for all Products do the following 
        for product in productList:
            href = product.find_element_by_xpath(".//div[@testid=\"ProductTitles\"]/span/a").get_attribute('href')
            self.executeProduct(href, self.archiveTable)
            
    def specificTable(self, name, action):
        product = self.driver.find_element_by_xpath("//a[@aria-label='"+name+"']")
        print(product.get_attribute('href'))
        # href = product.find_element_by_xpath(".//div[@testid=\"ProductTitles\"]/span/a").get_attribute('href')
        url = product.get_attribute('href')
        self.executeProduct(url, action)

    def deleteTables(self,url):
        # Run through all products 
        # Check if html table exists  
        if self.checkForTable(): 
            # if it exists, delete the size table picture 
            self.selectTablePicture()
            self.clickButton('Delete media')
            sleep(3)
            success[url]= True
            self.driver.find_element_by_xpath('//span[contains(text(), "Delete media")]').click()
        else:
            success[url]= False
                
    def deleteAllTablePictures(self):
        productList = self.getAllProducts()
        for product in productList:
            href = product.find_element_by_xpath(".//div[@testid=\"ProductTitles\"]/span/a").get_attribute('href')
            self.executeProduct(href, self.deleteTables)

    def changePrices(self):
        self.driver.find_element_by_xpath("//a[@id='active']").click()
        sleep(2)
        self.driver.find_element_by_xpath('//button[@aria-label="Next"]').click()
        sleep(4)
        while True:
            productList = self.getAllProducts()
            for product in productList:
                    href = product.find_element_by_xpath(".//div[@testid=\"ProductTitles\"]/span/a").get_attribute('href')
                    self.executeProduct(href, self.changePrice)
            sleep(4)
            self.driver.find_element_by_xpath('//button[@aria-label="Next"]').click()
            sleep(4)
    
    def changePrice(self, url):
        cost = self.driver.find_element_by_xpath('//input[@id="PolarisTextField2"]').get_attribute('value')
        price = round(float(cost) + 0.1*float(cost)) + 0.99
        print(price)
        positionDiv = self.driver.find_elements_by_xpath("//div[@class='_2MM1C']/div/div[contains(text(),'Price')]")
        position = self.driver.execute_script("""
            var i = 2;
            while( (arguments[0] = arguments[0].previousSibling) != null ) 
            i++;
            return i
        """, positionDiv)
        position = str(position)
        print('price at position', position)

        rows = self.driver.find_elements_by_xpath("//ul[@class='_3K9fP']/*")
        sleep(3)
        for row in rows:
            inputValue= row.find_element_by_xpath('.//div[contains(text(),"€")]/following-sibling::input')
            #inputValue = inputDiv.find_element_by_xpath('.//input')
            cost = inputValue.get_attribute('value')
            print ('old price', cost)
            price = round(float(cost) + 0.1*float(cost)) + 0.99
            print('new price', price)
            inputValue.send_keys(Keys.COMMAND + 'a')
            inputValue.send_keys(str(price))
            inputValue.send_keys(Keys.TAB) 

    def scrapePrices(self, orderID):
        #self.driver.find_element_by_xpath("//span[contains(text(), 'Orders')").click()
        sleep(2)
        i= 0
        while True:
            i +=1
            try:
                stringID = '#' + str(orderID)
                order = self.driver.execute_script("""
                    array = document.body.getElementsByTagName('span')
                    let found 
                    for (let i = 0 ; i< array.length ; i++){ if(array[i].innerText == arguments[0]){found = array[i]; break;} }
                    return found
                """, stringID)
                price = self.driver.execute_script("""
                    return arguments[0].parentElement.parentNode.parentNode.children[5].textContent
                """, order)
                price = price[1:]
                print(price)
                products[orderID]= {}
                products[orderID]["price"] = int(price)
                # put all prices to orderID 
                orderID += 1
            except: 
                break
        print(products)
        print('end of loop')
        
        
        
    def getCosts(self, orderID, endID):
        self.driver.get("https://gifutoshoppu.myshopify.com/admin/apps/printify/app?hmac=22495163e145f33151d798c34428a19dfb894a14179182704577958143809a92&locale=en-DE&new_design_language=true&session=84529564184272628efded0bf9c22c1621ef3d1292a58fea0cbc4a60c4fb4d2e&shop=gifutoshoppu.myshopify.com&timestamp=1610132063")
        sleep(4)
        iFrame = self.driver.execute_script("""
            return document.getElementsByTagName('iframe')[0]
        """)
        print(iFrame)
        self.driver.switch_to.frame(iFrame)
        order = "Orders"
        link = self.driver.execute_script("""
            array = document.body.getElementsByClassName('secondary')
            let found 
            for (let i = 0 ; i< array.length ; i++){ 
                if(array[i].innerText == 'Orders'){
                    found = array[i]; 
                    break;} 
                }
            return found.href
        """, order)
        self.driver.get(link)
        difference= endID-orderID
        sleep(3)
        i= 0
        while i< difference:
            self.driver.switch_to.window(self.driver.window_handles[0])
            stringID = '#' + str(orderID)
            try:
                print('processing product', stringID)
                orderLink = self.driver.execute_script("""
                    array = document.body.getElementsByTagName('div')
                    let found 
                    for (let i = 0 ; i< array.length ; i++){ if(array[i].innerText.substr(0,5) == arguments[0]){found = array[i]; break;} }
                    return found.parentElement.href
                """, stringID)
            except:
                print('stringID not found')
                orderID += 1
                continue
            self.openProductInNewTab(orderLink)
            totalCosts = self.driver.execute_script("""
                let totalCosts = document.body.getElementsByClassName('order__billing__entry order__billing__total')[0].children[1].innerText.substr(4)
                return totalCosts
            """)
            print(totalCosts)
            products[orderID] = {}
            products[orderID]["costs"] = float(totalCosts)
            # put all prices to orderID 
            orderID += 1
            i += 1
            self.driver.close()
        print(products)

# shopify = Shopify('https://cottagecore-outfits.myshopify.com/admin/products?selectedView=all', 'cottagecoreoutfit@gmail.com', 'Wassermann2001')
shopify = Shopify('https://gifutoshoppu.myshopify.com/admin/apps/printify/app?hmac=c009496353aa6388ce1cab62d5eb70da46ab89e86c5ddc202b47b4affbef1a75&locale=en-DE&new_design_language=true&session=53dd6d00afe02c54e29da83a37ecdb162dbd715f6b879b7df7f763b820d222c3&shop=gifutoshoppu.myshopify.com&timestamp=1610152491',"cottagely.shop@gmail.com","Wassermann2001")
sleep(2)
# shopify.specificTable('Academia Girl Dress', shopify.deleteTables)
# shopify.deleteAllTablePictures()

#shopify.specificTable('Angel Dream Dress', shopify.archiveTable)
shopify.getCosts(2530,2558)
#shopify.changeVendors()