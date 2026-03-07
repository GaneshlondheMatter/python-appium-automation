from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta


class BookTestRidePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ----------------------------
    # Page Header / Intro
    # ----------------------------

    EXP_PAGE_HEADER = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvMyMatterName"]'
    )

    TEST_RIDE_TEXT = (
        By.XPATH,
        '//android.widget.TextView[@text="Test ride the new AERA!"]'
    )

    BOOK_A_TEST_RIDE_BTN = (
        By.XPATH,
        '//android.widget.Button[@resource-id="com.matter.companion.qa:id/btn_book_a_test_ride"]'
    )

    ENTER_LOCATION_INPUT = (
        By.XPATH,
        '//android.widget.EditText[@resource-id="com.matter.companion.qa:id/et_find_a_place"]'
    )

    LOCATIONS_LIST = (
        By.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.matter.companion.qa:id/rv_locations"]//android.widget.TextView'
    )

    YOUR_LOC_CARD = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_dealer_address" and @text="Home Test Ride"]'
    )

    EXP_CENTER_CARD = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_dealer_address" and @text="Matter Experience Hub"]'
    )

    # ----------------------------
    # Date Selection
    # ----------------------------

    DATES_CARD = (
        By.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.matter.companion.qa:id/rv_dates"]/android.view.ViewGroup[1]'
    )

    BOOK_TEST_RIDE_BUTTON = (
        By.XPATH,
        '//android.widget.Button[@resource-id="com.matter.companion.qa:id/btn_book_test_ride"]'
    )

    # ----------------------------
    # Booking Confirmation
    # ----------------------------

    SUCCESS_EXPERIENCE_HUB_TEXT = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_common_success_failed_title"]'
    )

    EXPERIENCE_CENTER_DEALER_NAME = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_dealer_name"]'
    )

    DATE_OF_TEST_RIDE = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_date_value"]'
    )

    VISIT_ID = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_visit_ID"]'
    )

    PHONE_NUMBER = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_phone"]'
    )

    OKAY_BUTTON = (
        By.XPATH,
        '//android.widget.Button[@resource-id="com.matter.companion.qa:id/btn_okay"]'
    )

    GET_DIRECTION = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_get_direction"]'
    )

    EXPERIENCE_HUB_KHARADI = (
        By.XPATH,
        '//android.widget.ImageView[@content-desc="View Street view imagery for MATTER | Experience Hub Kharadi - Pune"]'
    )

    # ====================================================
    # ACTION METHODS
    # ====================================================

    def click_book_test_ride(self):
        self.wait.until(EC.element_to_be_clickable(self.BOOK_A_TEST_RIDE_BTN)).click()

    def enter_location(self, location):
        field = self.wait.until(EC.visibility_of_element_located(self.ENTER_LOCATION_INPUT))
        field.clear()
        field.send_keys(location)

    def select_first_location(self):
        elements = self.wait.until(EC.presence_of_all_elements_located(self.LOCATIONS_LIST))
        if elements:
            elements[0].click()

    def select_date(self, days_to_add):
        """
        Selects date dynamically based on today's date + days_to_add
        """
        target_date = datetime.now() + timedelta(days=days_to_add)
        day = str(target_date.day).zfill(2)

        dynamic_locator = (
            By.XPATH,
            f'//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_date" and @text="{day}"]'
        )

        self.wait.until(EC.element_to_be_clickable(dynamic_locator)).click()

    def click_book_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BOOK_TEST_RIDE_BUTTON)).click()

    def click_okay(self):
        self.wait.until(EC.element_to_be_clickable(self.OKAY_BUTTON)).click()

    # ====================================================
    # VALIDATION METHODS
    # ====================================================

    def is_booking_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_EXPERIENCE_HUB_TEXT)
        ).is_displayed()

    def get_visit_id(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.VISIT_ID)
        ).text
