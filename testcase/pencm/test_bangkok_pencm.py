import unittest
from parameterized import parameterized

from Page.homepage import HomePage
from Page.propertypage import RoomListPage
from data.language_list import lan_list
from driver.browser import firefox_browser


class Test_Room_Bangkok_ZHCN(unittest.TestCase):

    def setUp(self):
        self.driver = firefox_browser()
        self.home = HomePage(self.driver)
        self.property_page = RoomListPage(self.driver)


    def tearDown(self):
        self.driver.close()

    @parameterized.expand(lan_list['live']['bangkok'])
    def test_room_booking_bangkok_(self, language):
        """
        Testing Property, Room, Romm Detail, Offer modules for Bangkok,
        """
        self.bace_url_test = f"https://{HomePage.environment_pen}.peninsula.com/{language}/bangkok/5-star-luxury-hotel-riverside"
        try:
            self.driver.get(f"{self.bace_url_test}")

        except:
            self.driver.execute_script("window.stop()")
        self.driver.execute_script(f"window.open('{self.bace_url_test}')")
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
