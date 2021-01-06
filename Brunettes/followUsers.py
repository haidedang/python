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
import urllib.request
from datetime import date
import datetime

# from dotenv import load_dotenv

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--disable-dev-shm-usage')    

hashTags="#nfp #finest #babeswithcurves #babesofinstagram #babesofinstagram #fitnessmotivation #fitness #fitnessgirl #beautifulgirl #brunettegirl #brunette #beautifulbrunette #beauty #beautiful #gorgeous #pretty #hot #classy #elegant #stylish #brunette #girl #lady #makeup #fashion #potd #ootd #hairstyle #outfit #pose #bubbles #2021  #newyear #eyes #lips #black #looks #instagirl #sensual #stunning" 
slogans = [ "WEAR or TEAR?", "SHOP or FLOP?", "TAKE or TOSS?", "Rate this outfit from 1-10!", "YAY or NAY?"]
referall= "Click on link in Bio to shop this dress! <3"
comments = ["Amazing.", "So lovely <3", "I love this", "Wow <3", "this is awesome", "simply beautiful <3", "lovely post"]
slogan= "like or nah?"

highQualityPictures = {
    "https://www.instagram.com/p/CGrkkoZjV5h/": True,
    "https://www.instagram.com/p/CJV6u_mjg5W/": True,
    "https://www.instagram.com/p/CJN5f6zDDx-/": False
}


arr = hashTags.split() 
mySet = list(set(arr))


def hashTagSelector(hashtags):
    result= []
    for i in range(0,20):
        element = random.choice(hashtags)
        if element not in result:
            result.append(element)
            #print(result)
    return " ".join(result)
  
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
                      
    def commentAndLike(self, comment, follow):
        users = usersDB.loadState('userHQ.pickle')
        randomList = [k for k,v in users.items() if v == False]
        print('length of userDB', len(randomList))
        random.shuffle(randomList)
        selected = []
        for k in range(0,400):
            selected.append(random.choice(randomList))
        print('random selected users', selected)
        n = 0
        # x = number followers
        x = 0 
        for k in selected: 
            print('number of users liked, commented, and followed', n)
            if n < comment:
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
                    print('detect private or public profile')
                    firstPic = self.driver.find_element_by_xpath('//article[@class="ySN3v"]/div/div/div/div/a/div')
                    print('number of users followed', x)
                    if (x < follow):
                        print('following User')
                        followButton = self.driver.execute_script("""
                            return document.getElementsByClassName('BY3EC')[0].children[0] 
                        """)
                        followButton.click()
                        sleep(2)
                        self.followUser(k)
                        x += 1
                        # followUser
                    else:
                        print('limit followers reached')
                except:
                    print('account cannot be followed')
                    pass
                try:
                    self.driver.find_element_by_xpath('//article[@class="ySN3v"]/div/div/div/div/a/div').click()
                    sleep(2)
                except:
                    print('error', 'weird stuff going on')
                    pass
                self.likePicture()
                try:
                    self.driver.find_element_by_xpath('//textarea[@class="Ypffh"]').click()
                except NoSuchElementException:
                    print("This account is private. Flagging as private")
                    users[k] = "PRIVATE"
                    usersDB.saveState(users, 'userHQ.pickle')
                    pass
                sleep(2)
                """ try:
                    self.driver.find_element_by_xpath('//form[@class="X7cDz"]/textarea').send_keys(random.choice(comments))
                    sleep(2)
                    self.driver.find_element_by_xpath('//form[@class="X7cDz"]/textarea').send_keys(Keys.RETURN)
                    sleep(4)
                    print('commented and liked sucessfully')
                    users[k] = True
                    usersDB.saveState(users, 'userHQ.pickle')
                    n += 1
                except NoSuchElementException: 
                    print(NoSuchElementException)
                    pass """
                self.driver.close()
            else:
                print('limit of public comments reached. Exit')
                break
            print([k for k,v in users.items() if v == True])
            # print(selected)

    def followUser(self, user): 
        print('click Follow button of user')
    
        # load userList 
        following = usersDB.loadState('following.pickle')

        # following is false and empty object in first iteration
        today = datetime.date.today() 

        # check the object wether elements for this date exist 
        try:
            print('accessing date and show length', len(following[str(today)]))
            following[str(today)].append(user)
        except: 
            # if not existent, init empty array for that day
            print('first user of today. Init new array and save user')
            following[str(today)] = []
            following[str(today)].append(user)
        print('saving new followers...')
        usersDB.saveState(following, 'following.pickle')
    
    def likePicture(self):
        try:
            #like picture 
            self.driver.execute_script("""
                document.querySelector('svg[aria-label="Like"]').parentNode.click()
            """)
            # write a comment 
        except:
            pass

    def scrapeUsers(self):
        users = usersDB.loadState('userHQ.pickle')
        for link in highQualityPictures:
            # self.driver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
            if (highQualityPictures[link]):
                    # if image already has been assigned once or went through, skip it
                    print('image has already been scraped run through, skipp iteration')
                    continue
            self.driver.get(link)
            sleep(5)
            imageSrc = self.driver.find_element_by_xpath('//div[@class="KL4Bh"]/img').get_attribute('src')
            print(imageSrc)
        
            print('starting insta bot execution')
            #first_thumbnail.click()
            sleep(2)
            
            # click liked by users button
            section = self.driver.find_element_by_xpath("//section[@class='EDfFK ygqzn']")
            section.find_element_by_xpath(".//button").click()
            sleep(7)
            last_height = 0
            
            # save all usernames to run through
            pictureArr= []
            i= 0
            end = 0  
            while True:
                # save usernames in object 
                #  usernames = self.driver.find_elements_by_xpath('//div[@class="_1XyCr"]/div[position()=2]/div/div/*')
                # sleep(3)
                # print(usernames)
                sleep(1)
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
                print(len(list(users.keys())))
                last_height = last_height + 1000
                container = self.driver.find_element_by_xpath('//div[@class="_1XyCr"]/div[position()=2]/div')
                self.driver.execute_script("arguments[1].scrollTo(0, arguments[0]);", last_height, container)
                sleep(2)
                new_height = self.driver.execute_script("return arguments[0].scrollHeight", container)
                if end == new_height:
                    print('reached end of DIV')
                    break
                else:
                    end = new_height
                i +=1
                print(i)
                print('new Height', new_height)
                print('last_height', last_height)
                usersDB.saveState(users, 'userHQ.pickle')
                print('saved users to DB')
                if i==40000:
                    i= 0
                    break

            # comment and like all these users
            print('länge objekt', len(list(users.keys())))
            
            result = usersDB.loadState('userHQ.pickle')
            highQualityPictures[link]=True
            print('saved result', result)


my_bot = InstaBot('hot__brunettes', 'Wassermann2001') #not changing

my_bot.commentAndLike(10,1)