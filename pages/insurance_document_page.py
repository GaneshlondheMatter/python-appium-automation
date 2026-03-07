from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Helper.upload_helper import UploadProfileHelper


class InsuranceDocumentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.upload_helper = UploadProfileHelper(driver)

    # ---------------- LOCATORS ----------------

    INSURANCE_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvInsurance']"
    )

    UPLOAD_DOC = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvUploadOne']"
    )

    MODIFY_BTN = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvModify']"
    )

    DELETE_BTN = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvDelete']"
    )

    DELETE_CONFIRM = (
        By.XPATH,
        "//android.widget.Button[@resource-id='com.matter.companion.qa:id/btnDelete']"
    )

    # ---------------- DYNAMIC LOCATORS ----------------

    def get_uploaded_doc(self, index):
        return (
            By.XPATH,
            f"(//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivdocument'])[{index}]"
        )

    def get_menu_icon(self, index):
        return (
            By.XPATH,
            f"(//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivMenu'])[{index}]"
        )

    # ---------------- BASIC ACTIONS ----------------

    def click_insurance_uploaded_link(self):
        self.wait.until(EC.element_to_be_clickable(self.INSURANCE_LINK)).click()

    def click_menu(self, index):
        self.wait.until(EC.element_to_be_clickable(self.get_menu_icon(index))).click()

    def click_delete(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE_BTN)).click()

    def click_delete_confirm(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE_CONFIRM)).click()

    def click_modify(self):
        self.wait.until(EC.element_to_be_clickable(self.MODIFY_BTN)).click()

    def click_upload(self):
        self.wait.until(EC.element_to_be_clickable(self.UPLOAD_DOC)).click()

    # ---------------- METHODS (Used in Test) ----------------

    def is_doc_present(self, index):
        try:
            return self.driver.find_element(*self.get_uploaded_doc(index)).is_displayed()
        except NoSuchElementException:
            return False

    def delete_existing_documents(self):
        if self.is_doc_present(1) and self.is_doc_present(2):
            # Delete first
            self.click_menu(1)
            self.click_delete()
            self.click_delete_confirm()

            # After delete second becomes index 1
            self.click_menu(1)
            self.click_delete()
            self.click_delete_confirm()

    def upload_both_sides(self):
        self.click_upload()
        self.upload_helper.updateDocumentImage()

        self.click_upload()
        self.upload_helper.updateDocumentImage()

    def modify_both_sides(self):
        if self.is_doc_present(1) and self.is_doc_present(2):
            # Modify first
            self.click_menu(1)
            self.click_modify()
            self.upload_helper.updateDocumentImage()

            # Modify second
            self.click_menu(2)
            self.click_modify()
            self.upload_helper.updateDocumentImage()
