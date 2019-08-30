from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
"""
room detail page
"""

from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://pencd1.peninsula.com/en/hong-kong/luxury-hotel-room-suite-types/deluxe-room")

b = 1500
for i in range(0, 4):
    js = f"var action=document.documentElement.scrollTop={b}"
    driver.execute_script(js)
    b = b + 650
    sleep(3)

# driver.find_element(By.XPATH,'//*[@id="startDate"]').send_keys("12/12/2022")
# print(driver.find_elements(By.ID,'startDate'))
driver.find_element(By.XPATH,"//input[@aria-describedby='DateInput__screen-reader-message-startDate_bookingbar']").send_keys("12/12/2022")
driver.find_element(By.XPATH,"//input[@aria-describedby='DateInput__screen-reader-message-endDate_bookingbar']").send_keys("12/13/2022")
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div/div/button").click()


