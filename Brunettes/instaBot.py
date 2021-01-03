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
import pickle
from random import randint
import usersDB
from bs4 import BeautifulSoup
import requests


# from dotenv import load_dotenv

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--disable-dev-shm-usage')      


posts = {}
users = {}
        
class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Akzeptieren')]").click()
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]").click()
            except NoSuchElementException:
                pass
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Anmelden')]").click()
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Log In')]").click()
            except NoSuchElementException:
                pass
        try:
            self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                .send_keys(username)
            self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                .send_keys(pw)
            self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
                .click()
            # sleep(4) 
        except NoSuchElementException:
            pass

        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Jetzt nicht')]").click()
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            except NoSuchElementException:
                pass
        sleep(4)  
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Abbrechen')]").click()
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Cancel')]").click()
            except NoSuchElementException:
                pass    
        sleep(4)  

        #### First TIme USage #####

        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Jetzt nicht')]").click()
        except NoSuchElementException:
            try: 
                self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            except NoSuchElementException:
                pass

    def postPicture(self):
        try:  
            self.driver.find_element_by_xpath("//div[@data-testid=\"new-post-button\"]")\
            .click()
        except NoSuchElementException:
            pass
        sleep(4)

        pyautogui.FAILSAFE= False

        #move first file of folder images to posting folder
        moveFile('images','posting')
        
        #select Instagram folder 
        pyautogui.moveTo(200, 105)
        sleep(2)
        pyautogui.doubleClick()
        sleep(2)

        #select posting folder , delay to the bottom because of pycache
        pyautogui.moveTo(217, 185)
        sleep(2)
        pyautogui.doubleClick()
        sleep(2)

        # show file extensions
        pyautogui.moveTo(1056, 772)
        sleep(2)
        pyautogui.click()
        pyautogui.moveTo(1039, 805)
        sleep(2)
        pyautogui.click()
        
        #select File 
        pyautogui.moveTo(200, 105)
        sleep(2)
        pyautogui.click()

        #open File
        pyautogui.moveTo(1084, 826)
        sleep(2)
        pyautogui.click()

        sleep(8)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Next')]").click()
        sleep(4)
        
        self.driver.find_element_by_xpath("//textarea[@autocomplete=\"off\"]")\
            .send_keys(sloganGenerator() + "\n" + "\n" + hashTagSelector(mySet))
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Teilen')]").click()
        except NoSuchElementException:
            try: 
                self.driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()
            except NoSuchElementException:
                pass
        sleep(4)
    
        moveFile('posting','finished')
        print("success")    

    def followUsers(self): 
        i=0 
        n=0
        while n<2:
            self.driver.switch_to.window(self.driver.window_handles[0])
            sleep(2)
            # load the hashtagDB 
            hashtags = hashTagDB.loadState()
            print("HASHTAGDB", hashtags)
            hashtag = random.choice(list(hashtags.keys()))
            # hashtag="princessdress"
            #  hashtag = hashtag[1:]
            print(hashtag)
            self.driver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
            sleep(5)
            first_thumbnail = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
            imageSrc = first_thumbnail.find_element_by_xpath('.//img').get_attribute('src')
            print(imageSrc)
            try: 
                if (hashtags[hashtag][imageSrc]):
                    # if image already has been assigned once or went through, skip it
                    print('image has already been scraped run through, skipp iteration')
                    continue
            except:
                print('starting insta bot execution')
                first_thumbnail.click()
                sleep(2)
                
                # click liked by users button
                section = self.driver.find_element_by_xpath("//section[@class='EDfFK ygqzn']")
                section.find_element_by_xpath(".//button").click()

                last_height = 0
                
                # save all usernames to run through
                pictureArr= []
                while True:
                    # save usernames in object 
                    #  usernames = self.driver.find_elements_by_xpath('//div[@class="_1XyCr"]/div[position()=2]/div/div/*')
                    # sleep(3)
                    # print(usernames)
                    sleep(3)
                    global users
                    userData = self.driver.execute_script("""
                    let obj 
                    let arr=[]
                    var list =  document.querySelector('._1XyCr div:nth-child(2) div div').children
                    for (i = 0; i < list.length; i++) {
                        var title =  list[i].querySelector('div:nth-child(2) div div span a').getAttribute('title')
                        if (arguments[0][title] == undefined ){
                            arguments[0][title] = false
                            arguments[1].push(title)
                        }   
                    }
                    obj = {
                        "users": arguments[0],
                        "userPictureList":arguments[1]
                    }
                    return obj
                    """, users, pictureArr)
                    users = userData["users"]
                    for elem in userData["userPictureList"]:
                        pictureArr.append(elem)
                    userData["userPictureList"]=pictureArr
                    print(userData["userPictureList"])
                    last_height = last_height + 1000
                    container = self.driver.find_element_by_xpath('//div[@class="_1XyCr"]/div[position()=2]/div')
                    self.driver.execute_script("arguments[1].scrollTo(0, arguments[0]);", last_height, container)
                    sleep(1)
                    new_height = self.driver.execute_script("return arguments[0].scrollHeight", container)
                    i +=1
                    if i==10:
                        i= 0
                        break
                    if new_height == last_height:
                        break
                # comment and like all these users
            
                for k in userData["userPictureList"]:
                    print('processing userList', len(userData["userPictureList"]))
                    if userData["users"][k]== "PRIVATE":
                        print('useraccount is private')
                        continue
                    if userData["users"][k]== True:
                        print('user has already been commented')
                        continue
                    print(k)
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    sleep(7)
                    self.driver.execute_script("window.open('','_blank');")
                    sleep(2)
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    sleep(2)
                    self.driver.get("https://instagram.com/" + k + '/')
                    sleep(2)
                    try:
                        self.driver.find_element_by_xpath('//article[@class="ySN3v"]/div/div/div/div/a/div').click()
                        sleep(2)
                    except NoSuchElementException:
                        print(NoSuchElementException)
                        pass
                    
                    try:
                        #like picture 
                        self.driver.execute_script("""
                            document.querySelector('svg[aria-label="Like"]').parentNode.click()
                        """)
                        # write a comment 
                    except:
                        pass
                    try:
                        self.driver.find_element_by_xpath('//textarea[@class="Ypffh"]').click()
                    except NoSuchElementException:
                        print("This account is private. Flagging as private")
                        userData["users"][k] = "PRIVATE"
                        usersDB.saveState(userData["users"])
                        pass
                    sleep(2)
                    try:
                        self.driver.find_element_by_xpath('//form[@class="X7cDz"]/textarea').send_keys(random.choice(comments))
                        sleep(2)
                        self.driver.find_element_by_xpath('//form[@class="X7cDz"]/textarea').send_keys(Keys.RETURN)
                        sleep(4)
                        print('commented and liked sucessfully')
                        userData["users"][k] = True
                        usersDB.saveState(userData["users"])
                    except NoSuchElementException: 
                        print(NoSuchElementException)
                        pass
                    self.driver.close()
                hashtags[hashtag][imageSrc] = True
                hashTagDB.saveState(hashtags)
                n+=1

    def getUser(self, username):
        self.driver.get('https://www.instagram.com/'+ username + '/')
        sleep(3)
    
    def getPost(self, link, action, obj):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.execute_script("window.open('','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(link)
        sleep(2)
      
        result = action(obj)
       
        self.driver.close()
        return result
        
    
    def getUserHandle(self):
        try:
            userProfile = self.driver.execute_script("""
                return document.getElementsByClassName('JYWcJ')[0].href
            """)
            users[userProfile] = {}
            print('saved user', users)
        except:
            print('no linked user')

    def getAllRows(self, posts):
        rows = self.driver.find_elements_by_xpath('//article[@class="ySN3v"]/div/div/*')
        posts = posts
        for row in rows: 
            pictures = row.find_elements_by_xpath('.//*')
            pictures = self.driver.execute_script("""
                return arguments[0].childNodes
            """, row)
            try:
                for picture in pictures:
                    link = picture.find_element_by_css_selector('a').get_attribute('href')
                    try:
                        if(posts[link]==False):
                            print('row already has been processed!')
                            break
                    except:
                        print('taking post into account')
                        posts[link] = False  
            except:
                print('no link found')
                continue
        return posts
        
    def saveAllPostLinks(self):
        
        last_height = 0
        end = 0 
        i=0
        while True:
            results = self.getAllRows(posts)
            last_height = last_height + 1500
            self.driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
            sleep(1)
            new_height = self.driver.execute_script("return document.documentElement.scrollHeight")
            if end == new_height:
                print('reached end of DIV')
                break
            else:
                end = new_height
            i +=1
            print(i)
            print('new Height', new_height)
            print('last_height', last_height)
            if i==600:
                i= 0
                break
        usersDB.saveState(results, 'users.pickle')
        
            # store links in post object 
    def scrape(self, username):
        #users = usersDB.loadState('userHQ.pickle')
        self.getUser(username)
        self.saveAllPostLinks()
    
    def extractAllUsers(self):
        posts = usersDB.loadState('users.pickle')
        links = list(posts.keys())
        for link in links:
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.getPost(link, self.getUserHandle)
            usersDB.saveState(users, 'babes.pickle')
            print('saved state to file')
        
    def getLikes (self, obj):
        try:
            likes = self.driver.find_element_by_xpath('//div[@class="Nm9Fw"]/button/span').text
        except:
            print('assuming video content')
            return 0
        print(likes)
        return int(likes.replace(',',''))

    def findQualityPicture(self):
        babes = usersDB.loadState('babes.pickle')
        babesArr = list(babes.keys())
        for babe in babesArr:
            # from the first page get all pictures and their likes 
            # result 
            result = self.getPost(babe, self.getAllRows, babes[babe])

            babes[babe]= result
            usersDB.saveState(babes, 'babes.pickle')
            print('final result', babes)
            # sort this array from highest to lowest 
            # for every babe, fetch all the likes first and append to the object. 
            

            # pick the first 3 picture and add to DB 

            # do this with all chicks in the list 

    def getLikesFromAll(self):
        babes = usersDB.loadState('babes.pickle')
        babeArr = list(babes.keys())
        posting = usersDB.loadState('postingBabes.pickle')
        for elem in list(posting.keys()):
                babeArr.remove(elem)
        for babe in babeArr:
            pictures= list(babes[babe].keys())
            for picture in pictures:
                    # get all likes 
                    likes = self.getPost(picture, self.getLikes, {})
                    babes[babe][picture]={"processed":False}
                    babes[babe][picture]["likes"] = likes 
                    usersDB.saveState(babes, 'babes.pickle')
                    print('saved babe in DB', babes[babe])
                          
    def commentAndLike(self):
        # users = usersDB.loadState('userHQ.pickle')
        randomList = [k for k,v in users.items() if v == False]
        print('length of userDB', len(randomList))
        random.shuffle(randomList)
        selected = []
        for k in range(0,50):
            selected.append(random.choice(randomList))
        print('random selected users', selected)
        for k in selected:
            print('processing userList', len(selected))
            if users[k]== "PRIVATE":
                print('useraccount is private')
                continue
            if users[k]== True:
                print('user has already been commented')
                continue
            print(k)
            self.driver.switch_to.window(self.driver.window_handles[0])
            sleep(7)
            self.driver.execute_script("window.open('','_blank');")
            sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            sleep(2)
            self.driver.get("https://instagram.com/" + k + '/')
            sleep(2)
            try:
                self.driver.find_element_by_xpath('//article[@class="ySN3v"]/div/div/div/div/a/div').click()
                sleep(2)
            except:
                print('error', 'weird stuff going on')
                pass
            try:
                #like picture 
                self.driver.execute_script("""
                    document.querySelector('svg[aria-label="Like"]').parentNode.click()
                """)
                # write a comment 
            except:
                pass
            try:
                self.driver.find_element_by_xpath('//textarea[@class="Ypffh"]').click()
            except NoSuchElementException:
                print("This account is private. Flagging as private")
                users[k] = "PRIVATE"
                usersDB.saveState(users, 'userHQ.pickle')
                pass
            sleep(2)
            try:
                self.driver.find_element_by_xpath('//form[@class="X7cDz"]/textarea').send_keys(random.choice(comments))
                sleep(2)
                self.driver.find_element_by_xpath('//form[@class="X7cDz"]/textarea').send_keys(Keys.RETURN)
                sleep(4)
                print('commented and liked sucessfully')
                users[k] = True
                usersDB.saveState(users, 'userHQ.pickle')
            except NoSuchElementException: 
                print(NoSuchElementException)
                pass
            self.driver.close()
        print([k for k,v in users.items() if v == True])
        print(selected)

driver = webdriver.Chrome(options=chrome_options)

def test():
    babes = usersDB.loadState('babes.pickle')
    babeArr = list(babes.keys())
    print(babeArr.index('https://www.instagram.com/juuleechkaa/'))
    print(babes[babeArr[31]])
    posting= {}
    print('POSTED', list(posting.keys()))
    print(len(list(posting.keys())))
    try:
        for babe in babeArr:
            pictures= list(babes[babe].keys())
            likesArr = []
            obj= {}
            posting[babe]={}
            for picture in pictures:
                    # get all likes 
                    likes = babes[babe][picture]["likes"]
                    likesArr.append(likes)
                    obj[likes] = picture 
            likesArr.sort(reverse=True)
            #print(likesArr)
            for i in range(3):
                babes[babe][obj[likesArr[i]]]["passed"]=True
                posting[babe][obj[likesArr[i]]]=False
                # print(babes[babe][obj[likesArr[i]]]["passed"])
                #print('babes sucessfully selected')
                #
    except:
        posting.pop(list(posting.keys())[-1], None)
        print(len(babeArr))
        print(list(posting.keys()))
        print(len(list(posting.keys())))
        usersDB.saveState(posting, 'postingBabes.pickle')
        # usersDB.saveState(posting, 'postingBabes.pickle')

def addPictureSrc():
    babes = usersDB.loadState('postingBabes.pickle')
    babeArr = list(babes.keys())
    posting = usersDB.loadState('posts.pickle')
    for elem in list(posting.keys()):
            babeArr.remove(elem)
    # babes = list(posting.keys())
    print('startValue', babes)
    for babe in babeArr: 
        posts =  list(babes[babe].keys())
        for post in posts:
            try:
                print(babes[babe][post]["src"])
                print('already downloaded')
                break
            except:
                babes[babe][post] = {}
                print('enter loop')
                driver.get(post)
                sleep(2)
                src= driver.execute_script("""
                    return document.getElementsByClassName("_97aPb ")[0].querySelector('img').src
                """)
                babes[babe][post]["posted"]= False
                babes[babe][post]["src"] = src
                # print(posting[babe])
                print(babes)
                # usersDB.saveState(posting,'posts.pickle') 
            

# my_bot = InstaBot('hot__brunettes', 'Wassermann2001') #not changing
#my_bot.scrape('___brunettes___')
# my_bot.scrape()
# my_bot.findQualityPicture()
# my_bot.getLikesFromAll()
# test()
addPictureSrc()
#print(usersDB.loadState('babes.pickle'))



