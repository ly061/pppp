from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def chrome_browser():
    chrome_opt = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_opt.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_opt)
    driver.maximize_window()
    return driver

def firefox_browser():
    desired_capabilities = DesiredCapabilities.CHROME  #修改页面加载策略
    desired_capabilities["pageLoadStrategy"] = "none"
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.image', 2)
    driver = webdriver.Firefox(firefox_profile=firefox_profile)
    # driver = webdriver.Firefox()
    driver.maximize_window()
    return driver

