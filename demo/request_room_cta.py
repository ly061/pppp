import json
import re

from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By

from Page.propertypage import RoomListPage
hotelid = ""
lan_id = ""
li_button = []
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.maximize_window()
driver.get("https://staging.peninsula.com/en/hong-kong/luxury-hotel-room-suite-types")

li = driver.find_elements(By.XPATH,f'//div[@class = "roomListing-rooms"]//div[@class="cardRoomDetails-cta"]')
print(len(li))
for i in range(0,len(li)):
    base_url = driver.find_element(By.XPATH,f'//div[@class = "roomListing-rooms"]//div[@index = "{i}"]//div[@class="cardRoomDetails-cta"]/a').get_attribute("href")
    print(base_url)
    li.append(base_url)
print(len(li))
a= len(li)/2
li_new = li[-len(li)//2:]
print(li_new)
print(len(li_new))

http_headers = {'Accept': '*/*', 'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
url = f"http://staging.peninsula.com{li_new[0]}"
requests.DEFAULT_RETRIES = 5 # 增加重连次数
s = requests.session()
s.keep_alive = False
res = requests.get(url,headers=http_headers,timeout=10)
print(res.url)
