from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

room_type = "Deluxe room"
from selenium.webdriver.common.by import By
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.maximize_window()
driver.get("https://staging.peninsula.com/en/hong-kong/luxury-hotel-room-suite-types")

js = f"var action=document.documentElement.scrollTop=2100"
driver.execute_script(js)
time.sleep(10)
driver.find_element(By.XPATH,'//div[@class = "BookingBar-content"]//input[@id = "startDate"]').send_keys("11/12/2019")
driver.find_element(By.XPATH,'//div[@class = "BookingBar-content"]//input[@id = "endDate"]').send_keys("11/12/2019")
driver.find_element(By.XPATH,'//div[@class = "BookingBar-content"]//button[@type="submit"]').click()
driver.close()