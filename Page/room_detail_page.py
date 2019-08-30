from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By

class RoomDetailPage():
    """
    room detail page
    """
    def __init__(self,driver):
        self.driver = driver
        self.driver.find_element_check_in = By.XPATH, "//div[@data-react-component='BookingBar']//input[@type='text' and @id='startDate']"
        self.driver.find_element_check_out = By.XPATH,"//div[@data-react-component='BookingBar']//input[@type='text' and @id='endDate']"
        self.driver.find_element_submit_button = By.XPATH,"//div[@data-react-component='BookingBar']//button[@type='submit']"

    def input_check_in(self):
        self.driver.find_element(*self.driver.find_element_check_in).send_keys("12/12/2022")

    def input_check_out(self):
        self.driver.find_element(*self.driver.find_element_check_out).send_keys("12/13/2022")

    def click_submit_button(self):
        self.driver.find_element(*self.driver.find_element_submit_button).click()

    def input_data(self):
        js1 = "var action=document.documentElement.scrollTop=900"
        self.driver.execute_script(js1)
        self.input_check_in()
        self.input_check_out()
        self.click_submit_button()





