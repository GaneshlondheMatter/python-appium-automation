import random
from selenium.webdriver.common.by import By


class BookYourAeraPage:

    def __init__(self, driver):
        self.driver = driver

    # ---------------------- LOCATORS ----------------------

    BOOK_YOUR_AERA_BTN = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_book_another_aera"]'
    )

    AERA_5000_PLUS_OPTION = (
        By.XPATH,
        '//android.widget.TextView[@text="AERA 5000+"]'
    )

    BIKE_IMAGE = (
        By.XPATH,
        '//androidx.viewpager.widget.ViewPager[@resource-id="com.matter.companion.qa:id/vp_bike"]//android.widget.ImageView'
    )

    ENTER_YOUR_LOC_FIELD = (
        By.XPATH,
        '//android.widget.EditText[@resource-id="com.matter.companion.qa:id/et_enter_your_location"]'
    )

    ENTER_YOUR_LOC_INPUT_FIELD = (
        By.XPATH,
        '//android.widget.EditText[@resource-id="com.matter.companion.qa:id/et_find_a_place"]'
    )

    LOCATIONS_LIST = (
        By.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.matter.companion.qa:id/rv_locations"]//android.widget.TextView'
    )

    SORRY_AERA_NOT_AVAILABLE = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_aera_not_available_at_location"]'
    )

    LOCATION_CLOSE_ICON = (
        By.XPATH,
        '//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/iv_edt_location_cross"]'
    )

    AERA_IS_AVAILABLE_TEXT = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_aera_available_at_location"]'
    )

    I_AGREE_CHECKBOX = (
        By.XPATH,
        '//android.widget.CheckBox[@resource-id="com.matter.companion.qa:id/cb_agree"]'
    )

    BOOK_AERA_BTN = (
        By.XPATH,
        '//android.widget.Button[@resource-id="com.matter.companion.qa:id/btn_book_your_aera"]'
    )

    ORDER_SUMMARY_TEXT = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_order_summary"]'
    )

    AERA_MODEL_SUMMARY = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_selection_bike_model"]'
    )

    AERA_COLOR_SUMMARY = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_selection_bike_color"]'
    )

    USER_LOCATION_SUMMARY = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_location_value"]'
    )

    DEALER_LOC_SUMMARY = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_dealer_value"]'
    )

    PAYMENT_PAGE_HEADER = (
        By.XPATH,
        '//android.widget.TextView[@text="MATTER MOTOR WORKS PRIVATE LIMITED"]'
    )

    UPI_OPTION = (
        By.XPATH,
        '//android.widget.TextView[@text="UPI"]'
    )

    UPI_INPUT_FIELD = (
        By.XPATH,
        '//android.widget.EditText'
    )

    CONTINUE_BTN = (
        By.XPATH,
        '//android.widget.Button[@text="Continue"]'
    )

    UPI_ERROR_MSG = (
        By.XPATH,
        '//android.widget.TextView[@text="Please enter a correct UPI ID"]'
    )

    # ---------------------- ACTION METHODS ----------------------

    def click_book_your_aera(self):
        self.driver.find_element(*self.BOOK_YOUR_AERA_BTN).click()

    def select_aera_5000_plus(self):
        self.driver.find_element(*self.AERA_5000_PLUS_OPTION).click()

    def select_bike_color(self, index):
        locator = (
            By.XPATH,
            f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.matter.companion.qa:id/rv_bike_color"]/android.view.ViewGroup[{index}]'
        )
        self.driver.find_element(*locator).click()

    def is_bike_image_displayed(self):
        return self.driver.find_element(*self.BIKE_IMAGE).is_displayed()

    def enter_location(self, pincode):
        self.driver.find_element(*self.ENTER_YOUR_LOC_FIELD).click()
        self.driver.find_element(*self.ENTER_YOUR_LOC_INPUT_FIELD).clear()
        self.driver.find_element(*self.ENTER_YOUR_LOC_INPUT_FIELD).send_keys(pincode)

    def select_random_location(self):
        locations = self.driver.find_elements(*self.LOCATIONS_LIST)
        random.choice(locations).click()

    def is_not_available_displayed(self):
        elements = self.driver.find_elements(*self.SORRY_AERA_NOT_AVAILABLE)
        return len(elements) > 0 and elements[0].is_displayed()

    def retry_location(self, pincode):
        self.driver.find_element(*self.LOCATION_CLOSE_ICON).click()
        self.enter_location(pincode)

    def agree_and_book(self):
        self.driver.find_element(*self.I_AGREE_CHECKBOX).click()
        self.driver.find_element(*self.BOOK_AERA_BTN).click()

    def enter_invalid_upi(self, upi):
        self.driver.find_element(*self.UPI_OPTION).click()
        self.driver.find_element(*self.UPI_INPUT_FIELD).send_keys(upi)
        self.driver.find_element(*self.CONTINUE_BTN).click()

    # ---------------------- VALIDATION METHODS ----------------------

    def is_order_summary_displayed(self):
        return self.driver.find_element(*self.ORDER_SUMMARY_TEXT).is_displayed()

    def is_payment_page_displayed(self):
        return self.driver.find_element(*self.PAYMENT_PAGE_HEADER).is_displayed()

    def is_upi_error_displayed(self):
        return self.driver.find_element(*self.UPI_ERROR_MSG).is_displayed()