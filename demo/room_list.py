from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://pencd1.peninsula.com/en/hong-kong/luxury-hotel-room-suite-types")
js="var action=document.documentElement.scrollTop=2500"
driver.execute_script(js)
sleep(10)
find_room_type = driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(18) > div > div > section.featureSection.featureSection-dark."
                                                     "featureSection--flushTop > div > div > div > div > div:nth-child(2) >"
                                                     " div > div.cardRoomDetails-content > div.cardRoomDetails-name > a > h3")
# find_room_type.text.lower()
# room = "PHK-" + find_room_type.text.lower().replace(" ", "-")
# print(room)
# find_room_check = driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(18) > div > div > section.featureSection.featureSection-dark."
#                                                       "featureSection--flushTop > div > div > div > div > div:nth-child(2) > div > div.cardRoomDetails-content > div.cardRoomDetails-cta > a")
# if find_room_check :
#     find_room_check.click()
# else:
#     find_room_type.click()
find_room_type.click()
