from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VehicleSettingsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 8)

    # ------------------- LOCATORS -------------------

    NOTIFICATION_PREFERENCE = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvNotification']"
    )

    DOCUMENTS_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvMyDocument']"
    )

    MY_PLACES_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tv_my_places']"
    )

    VEHICLE_DETAILS_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvVehicleDetails']"
    )

    VEHICLE_SETTINGS_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvbikeDetails']"
    )

    # ------------------- COMMON CLICK METHOD -------------------

    def click_element(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message="Element is not visible or clickable"
        )
        element.click()

    # ------------------- ACTION METHODS -------------------

    def click_notification_preference(self):
        self.click_element(self.NOTIFICATION_PREFERENCE)

    def click_vehicle_settings_link(self):
        self.click_element(self.VEHICLE_SETTINGS_LINK)

    def click_documents_link(self):
        self.click_element(self.DOCUMENTS_LINK)

    def click_my_places_link(self):
        self.click_element(self.MY_PLACES_LINK)

    def click_vehicle_details_link(self):
        self.click_element(self.VEHICLE_DETAILS_LINK)
