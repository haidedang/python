from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--disable-dev-shm-usage')        


def login(self, url, username, pw): 
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get(url)
    try:
        self.driver.find_element_by_xpath("//input[@name=\"email\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()
    except NoSuchElementException:
        pass


    return self.driver