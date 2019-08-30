import re
import json
base = "https://www.peninsula.com/"
with open(r"C:\Users\PenUser\Desktop\Automation\peninsula_project\pppp\data\bookingdata.json", 'r') as f:
    data_json = f.read()
url_offer = "https://staging.peninsula.com/zh-cn/hong-kong/special-offers/rooms/more-time-with-our-compliments"
match_text = r".com/([a-z]{2}.{0,3})/(.*)/special-offers/rooms/(.*)"
search_text = re.search(match_text, url_offer)
print(search_text.group(1),search_text.group(2),search_text.group(3))
city_text = search_text.group(2) # 获取city
offer_text = search_text.group(3) # 获取offer type
change_data_to_py = json.loads(data_json)
for aaa in range(len(change_data_to_py)):
    if change_data_to_py[aaa]["Name"] == city_text:
        rooms_list_detail = change_data_to_py[aaa]["OfferList"]
        for bbb in range(len(rooms_list_detail)):
            if rooms_list_detail[bbb]["Name"] == offer_text:
                offer_rate = rooms_list_detail[bbb]["RateCode"]
                print(f"{base}{offer_rate}")