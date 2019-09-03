from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.common.keys import Keys

room_type = "Deluxe room"
from selenium.webdriver.common.by import By
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.maximize_window()
driver.get("https://pencm.peninsula.com/en/hong-kong/5-star-luxury-hotel-kowloon")

ActionChains(driver).send_keys(Keys.ESCAPE).perform()
