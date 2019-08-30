import json
import re

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

from Page.propertypage import RoomListPage
hotelid = ""
lan_id = ""
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.maximize_window()
driver.get("https://staging.peninsula.com/en/hong-kong/5-star-luxury-hotel-kowloon")

js = f"var action=document.documentElement.scrollTop=300"
driver.execute_script(js)
print("打开网址")

with open("C:/Users/yan.liu/PycharmProjects/pppp/data/staging_bookingdata.json", 'r') as f:
    data_json = f.read()
url_city = driver.current_url.rstrip()
match_text = r".com/([a-z]{2}.{0,3})/(.*)/5-star"
search_text = re.search(match_text, url_city)
language_text = search_text.group(1)  # 获取语言
city_text = search_text.group(2).replace("-", " ").title()  # 正则匹配城市
change_data_to_py = json.loads(data_json)
for i in range(len(change_data_to_py)):
    if change_data_to_py[i]["Name"] == city_text:
        hotelid = change_data_to_py[i]["HotelId"]
if language_text == "en":
    lan_id = "en-GB"
elif language_text == "zh-cn":
    lan_id = "zh-CN"
elif language_text == "zh":
    lan_id = "zh-TW"
elif language_text == "ja":
    lan_id = "ja-JP"
elif language_text == "fr":
    lan_id = "fr-FR"
elif language_text == "kr":
    lan_id = "ko-KR"
elif language_text == "es":
    lan_id = "es-ES"
elif language_text == "pt":
    lan_id = "pt-PT"
elif language_text == "ar":
    lan_id = "ar-EG"


driver.find_element(By.XPATH,'//div[@class="BookingBar-content"]//input[@id="startDate"]').send_keys("11/11/2019")
driver.find_element(By.XPATH,'//div[@class="BookingBar-content"]//input[@id="endDate"]').send_keys("12/11/2019")
try:
    print("click")
    driver.set_page_load_timeout(5)
    driver.set_script_timeout(5)
    driver.find_element(By.XPATH,'//div[@class="BookingBar-content"]//button[@type="submit"]').click()

except:
    driver.execute_script('window.stop()')
    print(driver.current_url)
    dir_url = f"https://secure.peninsula.com/?locale={lan_id}&level=chain&chain=5440&hotel={hotelid}&arrive=2019-11-11&depart=2019-11-12&room=&rate=&promo=&group=&agencyId="
    assert driver.current_url == dir_url
    print("验证成功")
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)
    driver.back()
    print("返回成功")