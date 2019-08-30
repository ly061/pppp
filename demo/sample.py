from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
bace_url = "https://www.peninsula.com/"
# lan = "en"
language = [1]

"""
选择语言
"""
for select_language in language:
    driver.maximize_window()
    driver.get("https://www.peninsula.com/en")
    driver.find_element(By.ID,"react-select-3--value-item").click()
    driver.find_elements(By.CLASS_NAME,"Select-option")[select_language].click()
    if select_language == 0:
        lan = "zh-cn"
    else:
        lan = "en"
    home_url = "/default"
    url = bace_url+lan+home_url
    print(url)
    assert url == f"https://www.peninsula.com/{lan}/default"

"""
选择城市
"""
city = 0
driver.find_elements(By.CLASS_NAME,"Select-arrow-zone")[0].click()
driver.find_element(By.ID,f"react-select-2--option-{city}").click()
if city == 0:
    city_code = "/hong-kong"
    url_pro = bace_url + lan + city_code + "/5-star-luxury-hotel-kowloon"
    print(url_pro)
    assert url_pro == f"https://www.peninsula.com/{lan}/{city_code}/5-star-luxury-hotel-kowloon"

