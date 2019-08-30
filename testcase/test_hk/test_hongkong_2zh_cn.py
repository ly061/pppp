import unittest
from ddt import ddt
from Page.homepage import HomePage
from Page.propertypage import RoomListPage
from driver.browser import chrome_browser, firefox_browser

@ddt
class Test_Room_HK_ZHCN(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = firefox_browser()
        cls.bace_url_test = f"https://{HomePage.environment_pen}.peninsula.com/zh-cn/hong-kong/5-star-luxury-hotel-kowloon"
        try:
            cls.driver.get(f"{cls.bace_url_test}")

        except:
            cls.driver.refresh()
        cls.driver.execute_script(f"window.open('{cls.bace_url_test}')")
        cls.home = HomePage(cls.driver)
        cls.property_page = RoomListPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    def test_room_booking_hk_zh_cn(self):
        """
        Testing Property, Room, Romm Detail, Offer modules for Hongkong, zh-cn
        """
        self.property_page.property_bookingbar()
        self.property_page.proferty_navigation_mega()
        self.property_page.click_room_suite()
        self.property_page.rooms_booking_bar()
        self.property_page.roomlist_check_availability()
        self.property_page.roomdetail_bookingbar()
        self.property_page.click_property_offer()
        self.property_page.offer_room_booking_widget()
        try:
            assert RoomListPage.err_mum == 0
        except:
            RoomListPage.err_mum = 0
            raise
        finally:
            RoomListPage.err_mum = 0

    if __name__ == '__main__':
        unittest.main()
