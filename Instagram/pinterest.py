from selenium import webdriver
from time import sleep
import urllib.request
from selenium.webdriver.chrome.options import Options
#from duplicateRemover import DuplicateRemover
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"
SCROLL_PAUSE_TIME = 2
chrome_options = Options()
chrome_options.add_argument('--disable-dev-shm-usage')   

class PinterestScraper:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.pinterest.de/search/pins/?q=cottagecore%20dress&rs=typed&term_meta[]=cottagecore%7Ctyped&term_meta[]=dress%7Ctyped")
        sleep(4)
    
    def download_images(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        print(last_height)
        downloadedImages = []
        n=0
        store = {}
        while True:
            images = self.driver.find_elements_by_css_selector('img')
            sleep(2)
            for image in images:
                try:
                    src = image.get_attribute('src')
                    try:
                        store[src]
                        print('Exists already', n)
                        continue   
                    except:
                        downloadedImages.append(src)
                        store[src]=n+1
                        n+=1
                except:
                    print('no image there')
                    sleep(2)
                    pass
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height 
        i=0
        for image in downloadedImages:
            #print(f"C:\\Users\\lee Stone\\Desktop\\dev\\Python\\Instagram\\images\\{i}.jpg")
            urllib.request.urlretrieve(image, os.getcwd()+ f"/images/{i}.png")
            i+=1

        # location = r"C:\Users\lee Stone\Desktop\dev\Python\Instagram\images"
#print(os.getcwd())

pinterest = PinterestScraper()
pinterest.download_images()

# img = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div/a/div/div/div[1]/img")
# src = img.get_attribute('src')


# urllib.urlretrieve(src, "dress.png")
