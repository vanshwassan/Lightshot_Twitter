from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import urllib
import urllib.request
import string
import random
import time

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)

def generateRandomString():
    rand_str = ''.join(random.choice(string.ascii_lowercase + string.digits) for K in range(6))
    return rand_str

def scraper():
    rand_str = generateRandomString()
    url = "https://prnt.sc/" + rand_str
    driver.get(url)
    time.sleep(3)
    try:
        image = driver.find_element(By.CSS_SELECTOR, '.under-image > img:nth-child(1)')
        img_data = image.get_attribute('src')
        print("Image Found!")
        urllib.request.urlretrieve(img_data, "img.png")
    except:
        print("No image found")
        scraper()