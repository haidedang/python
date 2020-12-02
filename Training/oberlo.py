from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://app.oberlo.com/import")

emailInput = driver.find_elements_by_tag_name("input")
emailInput.find_element_by_name("name")
emailInput.send_keys("haiduc.dang91@gmail.com")