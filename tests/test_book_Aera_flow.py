import random
from Helper.scroll_helper import ScrollHelper
from utils.base_test import BaseTest
from pages.book_your_aera_page import BookYourAeraPage
from pages.matter_home_page import MatterHomePage
from pages.account_page import AccountPage
from Helper.login_helper import LoginHelper


class TestBikeBookingFlow(BaseTest):

    def setup_method(self):
        self.setup()
        self.driver = self.driver
        self.driver.implicitly_wait(10)

        self.book_page = BookYourAeraPage(self.driver)
        self.home_page = MatterHomePage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.scroll_helper = ScrollHelper(self.driver)

    def test_complete_bike_booking_flow(self):

        # Login
        LoginHelper.login_into_matterverse(self.driver)

        # Navigate
        self.home_page.click_account_tab()
        self.account_page.click_my_orders()

        # Book Aera
        self.book_page.click_book_your_aera()
        self.book_page.select_aera_5000_plus()

        # Random color
        random_color = random.randint(1, 5)
        self.book_page.select_bike_color(random_color)

        assert self.book_page.is_bike_image_displayed()

        # Location
        self.book_page.enter_location("413502")
        self.book_page.select_random_location()

        # Availability handling
        if self.book_page.is_not_available_displayed():
            self.book_page.retry_location("413502")
            self.book_page.select_random_location()
        # Scroll to dealer / availability section 
        self.scroll_helper.scroll_to_text_contains( "BOOK @ ₹1.0*" )

        # Order summary validation
        assert self.driver.find_element(
            *self.book_page.ORDER_SUMMARY_TEXT
        ).is_displayed()

        assert self.driver.find_element(
            *self.book_page.AERA_MODEL_SUMMARY
        ).is_displayed()

        assert self.driver.find_element(
            *self.book_page.AERA_COLOR_SUMMARY
        ).is_displayed()

        assert self.driver.find_element(
            *self.book_page.USER_LOCATION_SUMMARY
        ).is_displayed()

        assert self.driver.find_element(
            *self.book_page.DEALER_LOC_SUMMARY
        ).is_displayed()

        # Agree & Book
        self.book_page.agree_and_book()

        # Payment validation
        assert self.driver.find_element(
            *self.book_page.PAYMENT_PAGE_HEADER
        ).is_displayed()

        self.book_page.enter_invalid_upi("8*&(*@upi")

        assert self.driver.find_element(
            *self.book_page.UPI_ERROR_MSG
        ).is_displayed()