from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver

    # ---------- LOCATORS ----------

    ACCOUNT_PAGE_HEADER = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvHeading']"
    )

    BIKE_NAME = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvBikeName']"
    )

    VEHICLE_IMAGE = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivBikeImage']"
    )

    BATTERY_WARRANTY_ACTIVE_TEXT = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/etBikeWarranty']"
    )

    VEHICLE_SETTINGS_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvbikeDetails']"
    )

    SECURITY_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvSecurity']"
    )

    EMERGENCY_CONTACTS_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvEmergencyContact']"
    )

    MY_ORDERS_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvMyOrders']"
    )

    REPORT_A_CONCERN_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvReportAConcern']"
    )

    VERSION_NUMBER = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvAppVersion']"
    )

    LOGOUT_BTN = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvLogout']"
    )

    NOTIFICATION_ICON = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivNotification']"
    )

    HELP_BUTTON = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvHelp']"
    )

    ABOUT_US_BUTTON = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvAboutUs']"
    )

    LEGAL_BUTTON = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvlegal']"
    )

    # ---------- ACTION METHODS ----------

    def click_vehicle_settings(self):
        self.driver.find_element(*self.VEHICLE_SETTINGS_LINK).click()

    def click_security(self):
        self.driver.find_element(*self.SECURITY_LINK).click()

    def click_emergency_contacts(self):
        self.driver.find_element(*self.EMERGENCY_CONTACTS_LINK).click()

    def click_my_orders(self):
        self.driver.find_element(*self.MY_ORDERS_LINK).click()
    def click_my_orders(self):
        self.driver.find_element(*self.Boo).click()

    def click_report_a_concern(self):
        self.driver.find_element(*self.REPORT_A_CONCERN_LINK).click()

    def click_logout(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()

    def click_notification_icon(self):
        self.driver.find_element(*self.NOTIFICATION_ICON).click()

    def click_help(self):
        self.driver.find_element(*self.HELP_BUTTON).click()

    def click_about_us(self):
        self.driver.find_element(*self.ABOUT_US_BUTTON).click()

    def click_legal(self):
        self.driver.find_element(*self.LEGAL_BUTTON).click()