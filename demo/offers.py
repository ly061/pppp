from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

room_type = "Deluxe room"
from selenium.webdriver.common.by import By
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.maximize_window()
driver.get("https://pencd1.peninsula.com/en/hong-kong/special-offers")

element = driver.find_element(By.ID,"Rooms & Suites")
driver.execute_script("arguments[0].scrollIntoView();", element)
cur_url_offer_1 = ""
element.click()
time.sleep(3)

offer_list = driver.find_elements(By.XPATH,'//*[@class = "offersListing-cardsWrapper"]/li')
open_offer_tab_err = 0
for offer_index in range(0, len(offer_list)):
    try:
        find_offer_url = driver.find_element(By.XPATH,
                                                  f'//*[@index = "{offer_index}"]//div[@class = "cardMedium-text"]/a').get_attribute(
            "href")
        js_open = f"window.open('{find_offer_url}')"
        driver.execute_script(js_open)
    except:
        open_offer_tab_err += 1
        pass
print("open all offers")
for i in range((len(offer_list) - open_offer_tab_err)):

    all_handles = driver.window_handles
    driver.switch_to_window(all_handles[-1])
    print("start switch")
    time.sleep(3)

    js = f"var action=document.documentElement.scrollTop=1000"
    driver.execute_script(js)
    # driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH,'//div[@class="campaignReservationsWText-calendar"]//input[@id="startDate"]'))

    print("scroll to time bar")

    try:
        driver.find_element(By.XPATH,'//div[@class="campaignReservationsWText-calendar"]//input[@id="startDate"]').send_keys("11/12/2019")
        driver.find_element(By.XPATH,'//div[@class="campaignReservationsWText-calendar"]//input[@id="endDate"]').send_keys("12/12/2019")
    except:
        time.sleep(30)
        cur_url_offer_1 = driver.current_url
        driver.find_element(By.XPATH,
                            '//div[@class="campaignReservationsWText-calendar"]//input[@id="startDate"]').send_keys(
            "11/12/2019")
        driver.find_element(By.XPATH,
                            '//div[@class="campaignReservationsWText-calendar"]//input[@id="endDate"]').send_keys(
            "12/12/2019")
    try:
        driver.set_page_load_timeout(5)
        driver.set_script_timeout(5)
        time.sleep(3)
        # driver.find_element(By.XPATH,'//div[@class="campaignReservationsWText-calendar"]//button[@type="submit"]').click()
        driver.execute_script("arguments[0].click()",driver.find_element(By.XPATH,'//div[@class="campaignReservationsWText-calendar"]//button[@type="submit"]'))
        print("end sleep")
        print(driver.current_url)

    except Exception as err:
        driver.execute_script('window.stop()')
        print(err)

        print(driver.current_url)
        driver.set_page_load_timeout(60)
        driver.set_script_timeout(60)
        driver.close()
        print("返回成功")

all_handles = driver.window_handles
driver.switch_to_window(all_handles[-1])

