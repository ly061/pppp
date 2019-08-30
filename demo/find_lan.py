from Page.propertypage import RoomListPage
from selenium import webdriver
driver = webdriver.Firefox()
url1 = "http://pencm.peninsula.com/en/manila/special-offers/rooms/x_salu-salo-series-room-package"
driver.get(url1)
url = driver.current_url
city = url.split("/")[4]
offer = url.split("/")[7].replace(" ","")
a = RoomListPage(11)
a.offer_code_in_jsondata(city,offer)
print(RoomListPage.offer_rate)
print(url)