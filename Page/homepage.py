import logging
from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage():
    environment_pen = "www"

    def __init__(self,driver):
        self.driver = driver
        self.find_element_change_element = By.CSS_SELECTOR,'div.navigationSettingsBar-content>div>div>span.Select-arrow-zone' #选择点击语言
        self.find_elelments_select_language = By.CLASS_NAME,"Select-option" #选择具体语言
        self.find_element_click_city_botton = By.CLASS_NAME,"Select-arrow-zone" #点击选择城市按钮
        self.find_lan_num = By.XPATH, '//div[@role = "listbox"]/*[@role="option"]'
        self.find_switch_city_arrow = By.CSS_SELECTOR,'div.navigationSettingsBar-content>div>div>span.Select-arrow-zone'

    def smart_wait(self,element):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((element)))

    def select_language(self,select_language):
        """
        select language
        """
        self.driver.find_elements(*self.find_element_change_element)[1].click()
        self.driver.find_elements(*self.find_elelments_select_language)[select_language].click()

    def select_city(self, city):
        """
        选择城市
        """
        self.driver.find_elements(*self.find_element_click_city_botton)[city].click()
        self.driver.find_element(By.ID, f"react-select-2--option-{city}").click()

    def switch_city(self,city):
        """
        switch city
        :return:
        """
        self.driver.find_elements(*self.find_switch_city_arrow)[0].click()
        self.driver.find_element(By.ID, f"react-select-2--option-{city}").click()



