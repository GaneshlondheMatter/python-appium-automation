from selenium.webdriver.common.by import By


class ControlPage:
    def __init__(self, driver):
        self.driver = driver

    # ---------- Locators ----------

    BIKE_NAME = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvMyMatterName']"
    )

    CONTROL_BUTTON = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvControl']"
    )

    IMAGE_DISPLAY = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivBike']"
    )

    TAP_TO_LOCK_BUTTON = (
        By.XPATH,
        "//android.widget.TextView[@text='Tap to lock']"
    )

    LOCATION_ICON = (
        By.XPATH,
        "//android.widget.RelativeLayout[@resource-id='com.matter.companion.qa:id/swipeBtn']/android.widget.ImageView"
    )

    FIND_MY_MATTER_BTN = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvfindMyMatter']"
    )

    FIND_A_ROUTE_BTN = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvFindARoute']"
    )

    # ---------- Element getters ----------

    def bike_name(self):
        return self.driver.find_element(*self.BIKE_NAME)

    def control_button(self):
        return self.driver.find_element(*self.CONTROL_BUTTON)

    def bike_image(self):
        return self.driver.find_element(*self.IMAGE_DISPLAY)

    def tap_to_lock_button(self):
        return self.driver.find_element(*self.TAP_TO_LOCK_BUTTON)

    def location_icon(self):
        return self.driver.find_element(*self.LOCATION_ICON)

    def find_my_matter_button(self):
        return self.driver.find_element(*self.FIND_MY_MATTER_BTN)

    def find_a_route_button(self):
        return self.driver.find_element(*self.FIND_A_ROUTE_BTN)

    # ---------- Actions ----------

    def tap_lock(self):
        self.tap_to_lock_button().click()

    def open_find_my_matter(self):
        self.find_my_matter_button().click()

    def open_find_a_route(self):
        self.find_a_route_button().click()
