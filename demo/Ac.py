from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(firefox_profile=firefox_profile)
# driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://staging.peninsula.com/en/hong-kong/luxury-hotel-room-suite-types/deluxe-room")

element = driver.find_element_by_xpath("//div[@data-react-component='BookingBar']")
driver.execute_script("arguments[0].scrollIntoView();", element)

driver.find_element_by_xpath(
    "//div[@data-react-component='BookingBar']//input[@type='text' and @name='startDate']").send_keys("11/12/2019")
driver.find_element_by_xpath(
    "//div[@data-react-component='BookingBar']//input[@type='text' and @name='endDate']").send_keys("12/12/2019")

buttonElement = driver.find_element_by_xpath("//div[@data-react-component='BookingBar']//button[@type='submit']")

try:
    driver.set_page_load_timeout(10)
    driver.set_script_timeout(10)
    buttonElement.click()

except Exception as err:
    driver.execute_script('window.stop()')
    print(driver.current_url,err)
    driver.close()