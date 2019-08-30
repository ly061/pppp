from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

room_type = "Deluxe room"
from selenium.webdriver.common.by import By
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.maximize_window()
driver.get("https://staging.peninsula.com/en/hong-kong/5-star-luxury-hotel-kowloon")

def another_lan(lan_num):
    driver.find_elements(By.CSS_SELECTOR,'div.navigationSettingsBar-content>div>div>span.Select-arrow-zone')[1].click()
    driver.find_elements(By.CLASS_NAME,"Select-option")[lan_num].click()