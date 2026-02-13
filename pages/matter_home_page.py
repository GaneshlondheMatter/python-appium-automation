from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MatterHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # ------------------ LOCATORS ------------------

    MATTER_HOME_LOGO = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/tvMatter']"
    )

    MY_MATTER_TAB = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvRide']"
    )

    EXPERIENCE_TAB = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvExperience']"
    )

    CARE_TAB = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvCare']"
    )

    ACCOUNT_TAB = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvAccount']"
    )

    RIDES_TAB = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvRides']"
    )

    CONTROL_TAB = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvControl']"
    )

    # ------------------ HELPER METHOD ------------------

    def click_element(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message="Element not visible"
        )
        element.click()

    # ------------------ ACTION METHODS ------------------

    def click_matter_home_logo(self):
        self.click_element(self.MATTER_HOME_LOGO)

    def click_my_matter_tab(self):
        self.click_element(self.MY_MATTER_TAB)

    def click_experience_tab(self):
        self.click_element(self.EXPERIENCE_TAB)

    def click_care_tab(self):
        self.click_element(self.CARE_TAB)

    def click_account_tab(self):
        self.click_element(self.ACCOUNT_TAB)

    def click_rides_tab(self):
        self.click_element(self.RIDES_TAB)

    def click_control_tab(self):
        self.click_element(self.CONTROL_TAB)
