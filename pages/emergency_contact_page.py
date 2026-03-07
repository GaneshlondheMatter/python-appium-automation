import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class EmergencyContactsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ---------------- LOCATORS ----------------

    EMERGENCY_LINK = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvEmergencyContact"]'
    )

    MAIN_CONTAINERS = (
        By.XPATH,
        '//android.view.ViewGroup[@resource-id="com.matter.companion.qa:id/clMain"]'
    )

    ADD_CONTACT_ICONS = (
        By.XPATH,
        '//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/ivAddContact"]'
    )

    CONTACT_ICON = (
        By.XPATH,
        '//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/imgContact"]'
    )

    CONTACT_NUMBER_LIST = (
        By.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.samsung.android.app.contacts:id/contact_list_text_area"]'
    )

    SAVE_BUTTON = (
        By.XPATH,
        '//android.widget.Button[@resource-id="com.matter.companion.qa:id/btnSaveContact"]'
    )

    MENU_OPTION_BUTTONS = (
        By.XPATH,
        '//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/ivOptionContact"]'
    )

    DELETE_BUTTON = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvDelete"]'
    )

    DELETE_CONFIRM_BUTTON = (
        By.XPATH,
        '//android.widget.Button[@resource-id="com.matter.companion.qa:id/btnConfirm"]'
    )

    NAME_INPUT_FIELD = (
        By.XPATH,
        '//android.widget.EditText[@resource-id="com.matter.companion.qa:id/edtContactName"]'
    )

    PHONE_NUMBER_INPUT_FIELD = (
        By.XPATH,
        '//android.widget.EditText[@resource-id="com.matter.companion.qa:id/edtPhoneNumber"]'
    )

    # ---------------- DYNAMIC LOCATORS ----------------

    def get_main_container(self, index):
        return (
            By.XPATH,
            f'(//android.view.ViewGroup[@resource-id="com.matter.companion.qa:id/clMain"])[{index}]'
        )

    def get_add_contact_icon(self, index):
        return (
            By.XPATH,
            f'(//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/ivAddContact"])[{index}]'
        )

    def get_menu_option_button(self, index):
        return (
            By.XPATH,
            f'(//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/ivOptionContact"])[{index}]'
        )

    # ---------------- ACTION METHODS ----------------

    def click_emergency_link(self):
        self.wait.until(EC.visibility_of_element_located(self.EMERGENCY_LINK)).click()

    def get_main_containers(self):
        return self.driver.find_elements(*self.MAIN_CONTAINERS)

    def get_add_contact_icons(self):
        return self.driver.find_elements(*self.ADD_CONTACT_ICONS)

    def is_add_contact_icon_displayed(self, index=1):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.get_add_contact_icon(index))
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    # ---------------- ADD RANDOM CONTACT ----------------

    def add_random_contact(self):
        self.wait.until(EC.visibility_of_element_located(self.CONTACT_ICON)).click()

        self.wait.until(
            lambda driver: len(driver.find_elements(*self.CONTACT_NUMBER_LIST)) > 0
        )

        contacts = self.driver.find_elements(*self.CONTACT_NUMBER_LIST)

        random_index = random.randint(0, len(contacts) - 1)

        contacts[random_index].click()

        self.wait.until(EC.visibility_of_element_located(self.SAVE_BUTTON)).click()

    # ---------------- ADD MANUAL CONTACT ----------------

    def add_new_emergency_contact(self, name, number):
        self.wait.until(EC.visibility_of_element_located(self.NAME_INPUT_FIELD)).send_keys(name)

        self.wait.until(EC.visibility_of_element_located(self.PHONE_NUMBER_INPUT_FIELD)).send_keys(number)

        self.wait.until(EC.visibility_of_element_located(self.SAVE_BUTTON)).click()

    # ---------------- DELETE CONTACT ----------------

    def delete_existing_contact(self, index=1):
        self.wait.until(
            EC.visibility_of_element_located(self.get_menu_option_button(index))
        ).click()

        self.wait.until(EC.visibility_of_element_located(self.DELETE_BUTTON)).click()

        self.wait.until(EC.visibility_of_element_located(self.DELETE_CONFIRM_BUTTON)).click()
