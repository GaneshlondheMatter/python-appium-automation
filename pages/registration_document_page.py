from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class RegistrationDocumentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    # ---------------- LOCATORS ----------------

    # ✅ Added Registration Certificate Section Locator
    Registration_certificate_section = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvRegistration_Certificate']"
    )

    RegistrationFrontSide = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivdocument'][1]"
    )

    HEADER = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvHeading']"
    )

    REGISTRATION_UPLOADED_DOC = (
        By.XPATH,
        "(//android.view.ViewGroup[@resource-id='com.matter.companion.qa:id/viewUploadOne']/android.view.ViewGroup)"
    )

    MENU_BTN = (
        By.XPATH,
        "(//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivMenu'])[1]"
    )

    MODIFY_BTN = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvModify']"
    )

    DELETE_BTN = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvDelete']"
    )

    DELETE_CONFIRM_BTN = (
        By.XPATH,
        "//android.widget.Button[@resource-id='com.matter.companion.qa:id/btnDelete']"
    )

    UPLOAD_REGISTRATION_DOC = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvUploadOne']"
    )

    FIRST_REGISTRATION_DOC = (
        By.XPATH,
        "(//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivdocument'])[1]"
    )

    SECOND_REGISTRATION_DOC = (
        By.XPATH,
        "(//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivdocument'])[2]"
    )

    # ---------------- DYNAMIC LOCATORS ----------------

    def get_registration_doc(self, index):
        return (
            By.XPATH,
            f"(//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivdocument'])[{index}]"
        )

    def get_menu_icon(self, index):
        return (
            By.XPATH,
            f"(//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivMenu'])[{index}]"
        )

    # ---------------- ACTIONS ----------------

    def click_registration_certificate_section(self):
        self.wait.until(
            EC.element_to_be_clickable(self.Registration_certificate_section)
        ).click()

    def click_menu_icon(self, index):
        self.wait.until(
            EC.element_to_be_clickable(self.get_menu_icon(index))
        ).click()

    def delete_flow(self):
        self.click_delete()
        self.click_delete_confirm()

    def modify_flow(self):
        self.click_modify()

    def click_menu(self):
        self.wait.until(
            EC.element_to_be_clickable(self.MENU_BTN)
        ).click()

    def click_modify(self):
        self.wait.until(
            EC.element_to_be_clickable(self.MODIFY_BTN)
        ).click()

    def click_delete(self):
        self.wait.until(
            EC.element_to_be_clickable(self.DELETE_BTN)
        ).click()

    def click_delete_confirm(self):
        self.wait.until(
            EC.element_to_be_clickable(self.DELETE_CONFIRM_BTN)
        ).click()

    def click_uploaded_document(self):
        self.wait.until(
            EC.element_to_be_clickable(self.REGISTRATION_UPLOADED_DOC)
        ).click()

    def click_upload_registration_doc(self):
        self.wait.until(
            EC.element_to_be_clickable(self.UPLOAD_REGISTRATION_DOC)
        ).click()

    # ---------------- VALIDATION ----------------

    def is_page_loaded(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.HEADER)
        ).is_displayed()

    # ✅ Added Safe Dynamic Validation Method
    def is_registration_uploaded(self, index):
        try:
            element = self.driver.find_element(*self.get_registration_doc(index))
            return element.is_displayed()
        except NoSuchElementException:
            return False