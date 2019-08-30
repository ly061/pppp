import logging

from selenium import webdriver
from time import sleep, time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import json
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib3

from Page.log import Log

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RoomListPage():

    hotelid = ""
    li_url = []
    lan_id = ""
    room_type_code = ""
    base_url = ""
    base_url2 = ""
    offer_rate = ""
    err_mum = 0
    room_type_text = ""
    data_json = ""
    start_date = "11/12/2019"
    arrive_time = "2019-12-11"
    end_date = "12/12/2019"
    depart_time = "2019-12-12"
    property_dir_url = ""
    property_dir_url2 = ""
    dir_url_room = ""
    mega_dir_url = ""
    mega_dir_url2 = ""

    def __init__(self, driver):
        self.driver = driver
        self.find_element_room_suit = By.ID, "focus-0"  # 定位到room suit
        self.find_element_property_offer = By.ID, "focus-3"
        self.find_element_offer_room = By.ID, "Rooms & Suites"
        self.find_element_offer_spa = By.ID, "Spa And Wellness"
        self.find_room_list = By.XPATH, '//div[@class="roomListing-rooms"]/div'
        self.find_room_input_start = By.CSS_SELECTOR, '#bookingbar-main-start'
        self.find_room_input_end = By.CSS_SELECTOR, '#bookingbar-main-end'
        self.find_room_submit = By.XPATH, '//div[@class="BookingBar-content"]//button[@type="submit" and @class="button-secondary"]'
        self.find_offer_list = By.XPATH, '//*[@class = "offersListing-cardsWrapper"]/li'
        self.find_room_bookingbar_start_date = By.CSS_SELECTOR, '#bookingbar-main-start'
        self.find_room_bookingbar_end_date = By.CSS_SELECTOR, '#bookingbar-main-end'
        self.find_room_bookingbar_submit = By.XPATH, '//div[@class = "BookingBar-content"]//button[@type="submit"]'
        self.find_room_cta = By.XPATH, f'//div[@class = "roomListing-rooms"]//div[@class="cardRoomDetails-cta"]'
        self.find_mega_cta_herf = By.CSS_SELECTOR, ".navigationTertiary > section > div > div > div > div > div > div.navigationTertiary-description > div:nth-child(4) > a"
        self.find_room_cta = By.XPATH, f'//div[@class = "roomListing-rooms"]//div[@class="cardRoomDetails-cta"]'
        self.find_offer_input_start = By.CSS_SELECTOR, '#bookingbar-res-start'
        self.find_offer_input_end = By.CSS_SELECTOR, '#bookingbar-res-end'
        self.find_offer_date_submit_button = By.XPATH, '//div[@class="campaignReservationsWText-calendar"]//button[@type="submit"]'
        self.find_property_submit_buttom = By.XPATH, '//div[@class="BookingBar-content"]//button[@type="submit"]'
        self.find_property_input_start_time = By.CSS_SELECTOR, '#bookingbar-main-start'
        self.find_property_input_end_time = By.CSS_SELECTOR, '#bookingbar-main-end'
        self.log = Log()
    # def log_info(self,message):
    #     logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #     logger = logging.getLogger(__name__)
    #     logger.info(message)

    def identify_language(self, language_input):
        data_lan = {"en": "en-GB",
                    "zh-cn": "zh-CN",
                    "zh": "zh-TW",
                    "ja": "ja-JP",
                    "fr": "fr-FR",
                    "kr": "ko-KR",
                    "es": "es-ES",
                    "pt": "pt-PT",
                    "ar": "ar-EG"}
        RoomListPage.lan_id = data_lan[language_input]

    def offer_code_in_jsondata(self, city, offer):
        self.read_json_data()
        data_json = json.loads(RoomListPage.data_json)
        dic_city = {}
        dic_offer = {}
        for i in range(len(data_json)):
            dic_city[data_json[i]["Name"].replace("-", "")] = i
        offer_list = data_json[dic_city[city]]["OfferList"]
        for jj in range(len(offer_list)):  # 生成offer
            dic_offer[offer_list[jj]["Name"]] = jj
        RoomListPage.offer_rate = offer_list[dic_offer[offer]]["RateCode"].replace(
            " ", "")

    def room_type_code_in_jsondata(self, city, room_type):
        self.read_json_data()
        data_json = json.loads(RoomListPage.data_json)
        dic_city = {}
        dic_roomtype = {}
        for i in range(len(data_json)):
            dic_city[data_json[i]["Name"].replace("-", "")] = i
        room_list = data_json[dic_city[city]]["RoomList"]
        RoomListPage.hotelid = data_json[dic_city[city]]["HotelId"]
        for cc in range(len(room_list)):
            dic_roomtype[room_list[cc]["Name"]] = cc
        RoomListPage.room_type_code = room_list[dic_roomtype[room_type]]["Code"]

    def city_id_in_jsondata(self, city):
        self.read_json_data()
        data_json = json.loads(RoomListPage.data_json)
        dic_city = {}
        for i in range(len(data_json)):
            dic_city[data_json[i]["Name"].replace("-", "")] = i
        RoomListPage.hotelid = data_json[dic_city[city]]["HotelId"]

    def scorll_to_top(self):
        js_scr_to_top = f"var action=document.documentElement.scrollTop=300"
        self.driver.execute_script(js_scr_to_top)

    def scroll_to_number(self, num):
        js = f"var action=document.documentElement.scrollTop={num}"
        self.driver.execute_script(js)

    def scroll_many_times(self, scroll_times):
        """
        every time scoll 500
        :param scroll_times:
        """
        num = 0
        sleep(1)
        for i in range(0, scroll_times):
            js = f"var action=document.documentElement.scrollTop={num}"
            self.driver.execute_script(js)
            num += 500
            sleep(0.25)
        self.scroll_to_number(0)

    def scroll_to_element_xpath(self, element):
        scroll_add_crowd_button = self.driver.find_element_by_xpath(element)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            scroll_add_crowd_button)

    def read_json_data(self):
        with open(r".\data\pencm_bookingdata.json", 'r') as f:
            RoomListPage.data_json = f.read()

    def click_room_suite(self):
        """
        click room suit and jump to room list
        """
        try:
            WebDriverWait(
                self.driver, 60, 0.5).until(
                EC.presence_of_element_located(
                    (By.ID, "focus-0")))
            self.driver.find_element(*self.find_element_room_suit).click()
        except BaseException:
            self.driver.refresh()
            self.driver.find_element(*self.find_element_room_suit).click()
        sleep(5)

    def click_property_offer(self):
        """
        click property offer
        """

        try:
            WebDriverWait(
                self.driver, 60, 0.5).until(
                EC.presence_of_element_located(
                    (By.ID, "focus-3")))
        except BaseException:
            self.driver.refresh()
        finally:
            self.driver.find_element(*self.find_element_property_offer).click()

    def switch_handls(self):
        """
        switch to the latest tab
        """
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])

    def setting_time_out(self, timeouting):
        self.driver.set_page_load_timeout(timeouting)
        self.driver.set_script_timeout(timeouting)

    def offer_room_booking_widget(self):
        """
        check offer room&suite booking
        """

        print("</br></br>")
        try:
            # self.scroll_many_times(6)
            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
                self.driver.find_element(
                    *self.find_element_offer_room))
        except BaseException:
            self.driver.refresh()
            # self.scroll_many_times(6)
            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
                self.driver.find_element(
                    *self.find_element_offer_room))
        finally:
            self.driver.find_element(*self.find_element_offer_room).click()

        WebDriverWait(
            self.driver, 20, 0.5).until(
            EC.presence_of_element_located(
                (self.find_offer_list)))
        offer_list = self.driver.find_elements(*self.find_offer_list)
        open_offer_tab_err = 0

        for offer_index in range(0, len(offer_list)):
            try:
                find_offer_url = self.driver.find_element(
                    By.XPATH,
                    f'//*[@index = "{offer_index}"]//div[@class = "cardMedium-text"]/a').get_attribute("href")
                js_open = f"window.open('{find_offer_url}')"
                self.driver.execute_script(js_open)
            except BaseException:
                open_offer_tab_err += 1
                pass

        for i in range((len(offer_list) - open_offer_tab_err)):
            if i == 0:
                sleep(10)
            self.switch_handls()
            self.read_json_data()
            try:
                url_offer = self.driver.current_url.rstrip()
                url_offer_split = url_offer.split("/")
                city_text = url_offer_split[4].replace("-", "")       # city
                offer_text = url_offer_split[7]                       # offer
                self.offer_code_in_jsondata(city_text, offer_text)
                offer_dir = f"https://secure.peninsula.com/?locale={RoomListPage.lan_id}&level=chain&chain=5440&hotel={RoomListPage.hotelid}&arrive={RoomListPage.arrive_time}&depart={RoomListPage.depart_time}&room=&rate={RoomListPage.offer_rate}&promo=&group=&agencyId="

            except BaseException:
                print("this room don't have booking widget</br>")
                print(f"{self.driver.current_url}</br>")
                self.driver.close()
                continue

            self.scroll_many_times(6)
            try:
                self.scroll_to_element_xpath(
                    '//div[@class="campaignReservationsWText-calendar"]//input[@id="startDate"]')
                self.driver.find_element(
                    *
                    self.find_offer_input_start).send_keys(
                    RoomListPage.start_date)
                self.driver.find_element(
                    *
                    self.find_offer_input_end).send_keys(
                    RoomListPage.end_date)
            except BaseException:
                try:
                    self.driver.refresh()
                    self.scroll_many_times(6)
                    self.scroll_to_element_xpath(
                        '//div[@class="campaignReservationsWText-calendar"]//input[@id="startDate"]')
                    self.driver.find_element(
                        *
                        self.find_offer_input_start).send_keys(
                        RoomListPage.start_date)
                    self.driver.find_element(
                        *
                        self.find_offer_input_end).send_keys(
                        RoomListPage.end_date)
                except BaseException:
                    self.driver.close()
                    continue

            try:
                self.setting_time_out(6)
                self.driver.find_element(
                    *
                    self.find_offer_date_submit_button).send_keys(
                    Keys.ENTER)
                sleep(6)

            except Exception as err:
                self.driver.execute_script('window.stop()')
                self.setting_time_out(200)

            try:
                assert offer_dir in self.driver.current_url
                print(f"Offer_{offer_text}_Booking widget, success</br>")
                print(f"{self.driver.current_url}</br>")
            except BaseException:
                try:
                    assert RoomListPage.offer_rate in self.driver.current_url
                    assert RoomListPage.hotelid in self.driver.current_url
                    print(f"Offer_{offer_text}_Booking widget, success</br>")
                    print(f"{offer_dir}</br>")
                except BaseException:
                    print(
                        f"Offer_{offer_text}_Booking widget, <span style='color:red'>failed</span></br>")
                    print(f"Correct: {offer_dir}</br>")
                    print(f"Wrong: {self.driver.current_url}</br>")
                    RoomListPage.err_mum += 1
            self.driver.close()
            self.setting_time_out(200)
        self.switch_handls()
        self.setting_time_out(200)

    def offer_spa_booking_widget(self):
        """
        check spa offer booking
        """

        print("</br></br>")
        try:
            # self.scroll_many_times(6)
            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
                self.driver.find_element(
                    *self.find_element_offer_room))
        except BaseException:
            self.driver.refresh()
            # self.scroll_many_times(6)
            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
                self.driver.find_element(
                    *self.find_element_offer_room))
        finally:
            self.driver.find_element(*self.find_element_offer_spa).click()

        WebDriverWait(
            self.driver, 20, 0.5).until(
            EC.presence_of_element_located(
                (self.find_offer_list)))
        offer_list = self.driver.find_elements(*self.find_offer_list)
        open_offer_tab_err = 0

        for offer_index in range(0, len(offer_list)):
            try:
                find_offer_url = self.driver.find_element(
                    By.XPATH,
                    f'//*[@index = "{offer_index}"]//div[@class = "cardMedium-text"]/a').get_attribute("href")
                js_open = f"window.open('{find_offer_url}')"
                self.driver.execute_script(js_open)
            except BaseException:
                open_offer_tab_err += 1
                pass

        for i in range((len(offer_list) - open_offer_tab_err)):
            if i == 0:
                sleep(10)
            self.switch_handls()
            self.read_json_data()
            try:
                url_offer = self.driver.current_url.rstrip()
                url_offer_split = url_offer.split("/")
                city_text = url_offer_split[4].replace("-", "")       # city
                offer_text = url_offer_split[7]                       # offer
                self.offer_code_in_jsondata(city_text, offer_text)
                offer_dir = f"https://secure.peninsula.com/?locale={RoomListPage.lan_id}&level=chain&chain=5440&hotel={RoomListPage.hotelid}&arrive={RoomListPage.arrive_time}&depart={RoomListPage.depart_time}&room=&rate={RoomListPage.offer_rate}&promo=&group=&agencyId="

            except BaseException:
                print("this room don't have booking widget</br>")
                print(f"{self.driver.current_url}</br>")
                self.driver.close()
                continue

            self.scroll_many_times(6)
            try:
                self.scroll_to_element_xpath(
                    '//div[@class="campaignReservationsWText-calendar"]//input[@id="startDate"]')
                self.driver.find_element(
                    *
                    self.find_offer_input_start).send_keys(
                    RoomListPage.start_date)
                self.driver.find_element(
                    *
                    self.find_offer_input_end).send_keys(
                    RoomListPage.end_date)
            except BaseException:
                try:
                    self.driver.refresh()
                    self.scroll_many_times(6)
                    self.scroll_to_element_xpath(
                        '//div[@class="campaignReservationsWText-calendar"]//input[@id="startDate"]')
                    self.driver.find_element(
                        *
                        self.find_offer_input_start).send_keys(
                        RoomListPage.start_date)
                    self.driver.find_element(
                        *
                        self.find_offer_input_end).send_keys(
                        RoomListPage.end_date)
                except BaseException:
                    self.driver.close()
                    continue

            try:
                self.setting_time_out(6)
                self.driver.find_element(
                    *
                    self.find_offer_date_submit_button).send_keys(
                    Keys.ENTER)
                sleep(6)

            except Exception as err:
                self.driver.execute_script('window.stop()')
                self.setting_time_out(200)

            try:
                assert offer_dir in self.driver.current_url
                print(f"Offer_spa_{offer_text}_Booking widget, success</br>")
                print(f"{self.driver.current_url}</br>")
            except BaseException:
                try:
                    assert RoomListPage.offer_rate in self.driver.current_url
                    assert RoomListPage.hotelid in self.driver.current_url
                    print(
                        f"Offer_spa_{offer_text}_Booking widget, success</br>")
                    print(f"{offer_dir}</br>")
                except BaseException:
                    print(
                        f"Offer_spa_{offer_text}_Booking widget, <span style='color:red'>failed</span></br>")
                    print(f"Correct: {offer_dir}</br>")
                    print(f"Wrong: {self.driver.current_url}</br>")
                    RoomListPage.err_mum += 1
            self.driver.close()
            self.setting_time_out(200)
        self.switch_handls()
        self.setting_time_out(200)

    def roomdetail_bookingbar(self):
        """
        open rooms in new tabs
        """

        print("</br>")

        self.scroll_many_times(5)
        rooms_list = self.driver.find_elements(*self.find_room_list)
        open_tab_num = 0
        for room_num in range(len(rooms_list)):
            try:
                find_room_url = self.driver.find_element(
                    By.CSS_SELECTOR,
                    f'div.roomListing-rooms div[index="{room_num}"] h3 a').get_attribute("href")
            except BaseException:
                continue
            try:
                if self.driver.find_element(
                        By.CSS_SELECTOR,
                        f'div.roomListing-rooms div[index="{room_num}"] div.cardRoomDetails-cta'):
                    js_open = f"window.open('{find_room_url}')"
                    self.driver.execute_script(js_open)
                    open_tab_num += 1

            except Exception:
                pass

        for room_num in range(0, open_tab_num):
            self.switch_handls()
            self.scroll_many_times(5)

            try:
                self.scroll_to_element_xpath(
                    '//div[@class="bookingbar-dateRanger-container"]//input[@type="text" and @id = "bookingbar-main-start"]')
                self.city_code()
                direct_url = f"https://secure.peninsula.com/?locale={RoomListPage.lan_id}&hotel={RoomListPage.hotelid}&arrive={RoomListPage.arrive_time}&depart={RoomListPage.depart_time}&room=&rate=&promo=&group=&agencyId=&accessible="
                WebDriverWait(
                    self.driver,
                    60,
                    0.5).until(
                    EC.presence_of_element_located(
                        (By.XPATH,
                         '//div[@class="bookingbar-dateRanger-container"]//input[@type="text" and @id = "bookingbar-main-start"]'))).send_keys(
                    RoomListPage.start_date)
                self.driver.find_element(
                    *
                    self.find_room_input_end).send_keys(
                    RoomListPage.end_date)
            except BaseException:
                self.driver.close()
                continue
            try:
                self.setting_time_out(15)
                self.driver.find_element(*self.find_room_submit).click()
                # sleep(10)
                cur_url = self.driver.current_url
            except BaseException:
                self.driver.execute_script('window.stop()')
                self.setting_time_out(200)
                cur_url = self.driver.current_url

            try:
                assert cur_url == direct_url
                print(
                    f"RoomDetail_{RoomListPage.room_type_text}_Bookingbar, success</br>")
                print(f"{cur_url}</br>")
            except BaseException:
                try:
                    assert RoomListPage.hotelid in self.driver.current_url
                    assert RoomListPage.room_type_code in self.driver.current_url
                    print(
                        f"RoomDetail_{RoomListPage.room_type_text}_Bookingbar, success</br>")
                    print(f"{direct_url}</br>")
                except BaseException:
                    print(
                        f"RoomDetail_{RoomListPage.room_type_text}_Bookingbar, <span style='color:red'>failed</span></br>")
                    print(f"{self.driver.current_url}</br>")
                    RoomListPage.err_mum += 1
            finally:
                self.driver.close()
        self.switch_handls()
        self.setting_time_out(200)

    def city_code(self):
        self.read_json_data()
        url_city = self.driver.current_url.rstrip()
        url_city_split = url_city.split("/")

        language_text = url_city_split[3]  # language
        city_text = url_city_split[4].replace("-", "")  # city
        RoomListPage.room_type_text = url_city_split[6]  # room_type

        # change_data_to_py = json.loads(RoomListPage.data_json)
        # for i in range(len(change_data_to_py)):
        #     if change_data_to_py[i]["Name"].replace("-","") == city_text:
        #         RoomListPage.hotelid = change_data_to_py[i]["HotelId"]
        #         rooms_list_detail = change_data_to_py[i]["RoomList"]
        #         for j in range(len(rooms_list_detail)):
        #             if rooms_list_detail[j]["Name"] == RoomListPage.room_type_text:
        #                 RoomListPage.room_type_code = rooms_list_detail[j]["Code"]
        self.room_type_code_in_jsondata(city_text, RoomListPage.room_type_text)

        self.identify_language(language_text)

    def property_bookingbar(self):
        """
        booking from the hotel property page and check the url has hotel id
        """

        self.read_json_data()
        url_city = self.driver.current_url.rstrip()
        url_city_split = url_city.split("/")
        language_text = url_city_split[3]  # language
        city_text = url_city_split[4].replace("-", "")  # city
        self.city_id_in_jsondata(city_text)
        self.identify_language(language_text)
        self.scroll_many_times(6)
        try:
            self.scroll_to_element_xpath(
                '//div[@class="BookingBar-content"]//input[@id="bookingbar-main-start"]')
            self.driver.find_element(
                *
                self.find_property_input_start_time).send_keys(
                RoomListPage.start_date)
            self.driver.find_element(
                *
                self.find_property_input_end_time).send_keys(
                RoomListPage.end_date)
        except BaseException:
            try:
                self.driver.refresh()
                self.scroll_many_times(6)
                self.scroll_to_element_xpath(
                    '//div[@class="BookingBar-content"]//input[@id="bookingbar-main-start"]')
                self.driver.find_element(
                    *
                    self.find_property_input_start_time).send_keys(
                    RoomListPage.start_date)
                self.driver.find_element(
                    *
                    self.find_property_input_end_time).send_keys(
                    RoomListPage.end_date)
            except BaseException:
                self.driver.refresh()
                sleep(10)
                self.scroll_many_times(6)
                self.scroll_to_element_xpath(
                    '//div[@class="BookingBar-content"]//input[@id="bookingbar-main-start"]')
                self.driver.find_element(
                    *
                    self.find_property_input_start_time).send_keys(
                    RoomListPage.start_date)
                self.driver.find_element(
                    *
                    self.find_property_input_end_time).send_keys(
                    RoomListPage.end_date)

        try:
            self.setting_time_out(25)
            self.driver.find_element(*self.find_property_submit_buttom).click()
            sleep(24)

        except BaseException:
            self.driver.execute_script('window.stop()')

            self.setting_time_out(200)
        RoomListPage.mega_dir_url = f"https://secure.peninsula.com/?locale={RoomListPage.lan_id}&hotel={RoomListPage.hotelid}&arrive=&depart=&room=&rate=&promo=&group=&agencyId=&accessible="
        RoomListPage.property_dir_url = f"https://secure.peninsula.com/?locale={RoomListPage.lan_id}&hotel={RoomListPage.hotelid}&arrive={RoomListPage.arrive_time}&depart={RoomListPage.depart_time}&room=&rate=&promo=&group=&agencyId=&accessible="
        RoomListPage.base_url = f"https://secure.peninsula.com/?locale={RoomListPage.lan_id}&chain=5440&hotel={RoomListPage.hotelid}&arrive={RoomListPage.arrive_time}&depart={RoomListPage.depart_time}&room=&rate="

        try:
            assert self.driver.current_url == RoomListPage.property_dir_url
            # print(f"Property_Bookingbar, success</br>")
            # print(f"{self.driver.current_url}</br></br>")
            print("Property_Bookingbar, success</br>")
            print(self.driver.current_url,"</br></br>")
        except BaseException:
            try:
                assert RoomListPage.hotelid in self.driver.current_url
                # print(f"Property_Bookingbar, success</br>")
                # print(f"{RoomListPage.property_dir_url}</br></br>")
                print("Property_Bookingbar, success")
                print(self.driver.current_url)
            except BaseException:
                # print(f"Property_Bookingbar, <span style='color:red'>failed</span></br>")
                # print(f"{self.driver.current_url}</br></br>")
                print(
                    f"Property_Bookingbar, <span style='color:red'>failed</span>")
                print(f"{self.driver.current_url}</br>")
                RoomListPage.err_mum += 1
        self.driver.close()
        self.switch_handls()
        self.setting_time_out(200)

    def rooms_booking_bar(self):
        """
        check room list booking bar
        """

        self.driver.execute_script(f'window.open("{self.driver.current_url}")')
        self.scroll_many_times(6)

        try:
            self.scroll_to_element_xpath(
                '//div[@class = "BookingBar-content"]//input[@id = "startDate"]')
            self.driver.find_element(
                *
                self.find_room_bookingbar_start_date).send_keys(
                RoomListPage.start_date)
            self.driver.find_element(
                *
                self.find_room_bookingbar_end_date).send_keys(
                RoomListPage.end_date)
        except BaseException:
            self.driver.refresh()
            self.scroll_to_number(1200)
            try:
                WebDriverWait(
                    self.driver, 20, 0.5).until(
                    EC.presence_of_element_located(
                        (self.find_room_bookingbar_start_date)))
                self.driver.find_element(
                    *
                    self.find_room_bookingbar_start_date).send_keys(
                    RoomListPage.start_date)
                self.driver.find_element(
                    *
                    self.find_room_bookingbar_end_date).send_keys(
                    RoomListPage.end_date)
            except BaseException:
                self.driver.refresh()
                self.scroll_to_number(2300)
                self.driver.find_element(
                    *
                    self.find_room_bookingbar_start_date).send_keys(
                    RoomListPage.start_date)
                self.driver.find_element(
                    *
                    self.find_room_bookingbar_end_date).send_keys(
                    RoomListPage.end_date)

        try:
            self.setting_time_out(15)
            self.driver.find_element(*self.find_room_bookingbar_submit).click()
            sleep(15)

        except BaseException:
            self.driver.execute_script('window.stop()')
            self.setting_time_out(200)

        try:
            assert self.driver.current_url == RoomListPage.property_dir_url
            print(f"Rooms_Bookingbar, success</br>")
            print(f"{self.driver.current_url}</br></br>")
        except BaseException:
            try:
                assert RoomListPage.hotelid in self.driver.current_url
                print(f"Rooms_Bookingbar, success</br>")
                print(f"{RoomListPage.property_dir_url}</br></br>")
            except BaseException:
                print(f"Rooms_Bookingbar, <span style='color:red'>failed</span></br>")
                print(f"{self.driver.current_url}</br></br>")
                RoomListPage.err_mum += 1

        self.driver.close()
        self.switch_handls()
        self.setting_time_out(200)

    def roomlist_check_availability(self):

        cur_room_url_city = self.driver.current_url.split("/")[4].replace("-", "")  # city
        cur_room_url_lan = self.driver.current_url.split("/")[3]  # lan
        self.identify_language(cur_room_url_lan)
        self.read_json_data()
        data_py = json.loads(RoomListPage.data_json)

        li = self.driver.find_elements(*self.find_room_cta)
        for i in range(0, len(li)):
            try:
                base_url = self.driver.find_element(
                    By.CSS_SELECTOR,
                    f'div.roomListing-rooms div[index="{i}"] div.cardRoomDetails-cta a').get_attribute("href")
                RoomListPage.li_url.append(base_url)
            except BaseException:
                pass

        for j in range(0, len(RoomListPage.li_url)):
            base_url_roomtype = self.driver.find_element(
                By.CSS_SELECTOR,
                f'div.roomListing-rooms div[index="{j}"] h3 a').get_attribute("href")
            room_type_name = base_url_roomtype.split("/")[-1]  # room_type

            self.room_type_code_in_jsondata(cur_room_url_city, room_type_name)

            RoomListPage.dir_url_room = f"https://secure.peninsula.com/?locale={RoomListPage.lan_id}&hotel={RoomListPage.hotelid}&arrive=&depart=&room={RoomListPage.room_type_code}&rate=&promo=&group=&agencyId=&accessible="
            url_origin = RoomListPage.li_url[j]

            s = requests.session()
            res = requests.get(url_origin, allow_redirects=False, verify=False)
            try:
                self.location = res.headers['Location']

                assert self.location == RoomListPage.dir_url_room
                print(
                    f"Rooms_Roomlist_{room_type_name}_Check Availability, success</br>")
                print(f"{self.location}</br>")

            except BaseException:
                print(
                    f"Rooms_Roomlist_{room_type_name}_Check Availability, <span style='color:red'>failed</span></br>")
                print(f"location: {self.location}")
                print(RoomListPage.dir_url_room)
                RoomListPage.err_mum += 1

        RoomListPage.li_url = []

    def proferty_navigation_mega(self):
        try:
            adove_element = self.driver.find_element(
                *self.find_element_room_suit)
            ActionChains(self.driver).move_to_element(adove_element).perform()
            sleep(5)
            find_mega_cta = self.driver.find_element(*self.find_mega_cta_herf)
            mega_url = find_mega_cta.get_attribute("href")
        except BaseException:
            self.driver.refresh()
            adove_element = self.driver.find_element(
                *self.find_element_room_suit)
            ActionChains(self.driver).move_to_element(adove_element).perform()
            sleep(5)
            find_mega_cta = self.driver.find_element(*self.find_mega_cta_herf)
            mega_url = find_mega_cta.get_attribute("href")

        s = requests.session()
        res = requests.get(mega_url, allow_redirects=False, verify=False)
        try:
            location_mega = res.headers['Location']
            assert RoomListPage.mega_dir_url == location_mega
            print("Property_Navigation Mega, success</br>")
            print(f"{location_mega}</br></br>")


        except BaseException:
            print(f"Property_Navigation Mega,<span style='color:red'>failed</span></br> ")
            print(f"{self.driver.current_url}</br></br>")
            RoomListPage.err_mum += 1
