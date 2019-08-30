from selenium import webdriver
import time
room_type = "Deluxe room"
from selenium.webdriver.common.by import By
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.maximize_window()
driver.get("https://www.jd.com")
driver.execute_script('window.scrollTo({top:1000},behavior:"smooth")')
