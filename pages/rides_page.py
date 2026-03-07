from selenium.webdriver.common.by import By


class RidesPage:

    # ---------- LOCATORS ----------

    RIDES_TAB = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvRides"]'
    )

    RIDES_COUNT = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvRidesCount"]'
    )

    RIDES_SUMMARY_TEXT = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvRidesSummary"]'
    )

    RIDES_DATA = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvRideData"]'
    )

    SHARE_SUMMARY_ICON = (
        By.XPATH,
        '//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/ivShareSummary"]'
    )

    VIEW_MORE = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvViewMore"]'
    )

    RIDE_SUMMARY_DETAILS = (
        By.XPATH,
        '//android.view.ViewGroup[@resource-id="com.matter.companion.qa:id/clRide"]'
    )

    # ---------- INIT ----------

    def __init__(self, driver):
        self.driver = driver

    # ---------- ELEMENT METHODS ----------

    def get_rides_tab(self):
        return self.driver.find_element(*self.RIDES_TAB)

    def get_rides_count(self):
        return self.driver.find_element(*self.RIDES_COUNT)

    def get_rides_summary_text(self):
        return self.driver.find_element(*self.RIDES_SUMMARY_TEXT)

    def get_rides_data(self):
        return self.driver.find_element(*self.RIDES_DATA)

    def get_share_summary_icon(self):
        return self.driver.find_element(*self.SHARE_SUMMARY_ICON)

    def get_view_more(self):
        return self.driver.find_element(*self.VIEW_MORE)

    def get_ride_summary_details(self):
        return self.driver.find_elements(*self.RIDE_SUMMARY_DETAILS)
