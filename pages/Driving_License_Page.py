from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class DrivingLicensePage:

    # ------------------- LOCATORS -------------------

    DRIVING_LICENSE_HEADER = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvHeading']"
    )

    DRIVING_LICENSE_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvDrivingLicense']"
    )

    REGISTRATION_CERTIFICATE = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvRegistration_Certificate']"
    )

    INSURANCE_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvRegistration_Certificate']"
    )

    UPLOAD_FRONT_SIDE = (
        By.XPATH,
        "//android.view.ViewGroup[@resource-id='com.matter.companion.qa:id/viewUploadOne']"
    )

    UPLOAD_BACK_SIDE = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvUploadTwo']"
    )

    CAMERA_OPTION = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvCamer']"
    )

    GALLERY_OPTION = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvGallery']"
    )

    UPLOAD_POP_CLOSE_ICON = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivCrossing']"
    )

    DOWNLOAD_FOLDER = (
        By.XPATH,
        "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/thumbnail'])[5]"
    )

    SELECT_ITEM = (
        By.XPATH,
        "//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout']"
    )

    CANCEL_BTN = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvCancel']"
    )

    DONE_BTN = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvCropDone']"
    )

    ROTATE_BUTTON = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivRetake']"
    )

    FRONT_PAGE_MENU_BTN = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivMenu']"
    )

    BACK_PAGE_MENU_BTN = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivMenuBack']"
    )

    DELETE_BTN = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvDelete']"
    )

    MODIFY_BTN = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvModify']"
    )

    DELETE_CONFIRM_BTN = (
        By.XPATH,
        "//android.widget.Button[@resource-id='com.matter.companion.qa:id/btnDelete']"
    )

    DELETE_CONFIRM_POP = (
        By.XPATH,
        "//android.widget.FrameLayout[@resource-id='com.matter.companion.qa:id/design_bottom_sheet']/android.view.ViewGroup"
    )

    DELETE_CLOSE_ICON = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivCross']"
    )

    DRIVING_FRONT_SIDE_UPLOADED = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivdocument']"
    )

    DRIVING_BACK_SIDE_UPLOADED = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivdocumentBack']"
    )

    Album_OPTION = (  
          By.XPATH,   
          "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/icon'])[2]"   
    )
    DOWNLOAD_ALBUM = (    
        By.XPATH,   
        "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/thumbnail'])[5]"   
    )

    # ------------------- INIT -------------------
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ------------------- WAIT + CLICK METHOD -------------------

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    # ------------------- MAIN ACTION METHODS -------------------

    def open_driving_license_section(self):
        self.click_element(self.DRIVING_LICENSE_LINK)

    def upload_front_side(self, is_modify=False):
        if not is_modify:
            self.click_element(self.UPLOAD_FRONT_SIDE)
            
        self.click_element(self.GALLERY_OPTION)
        self.click_element(self.Album_OPTION)
        self.click_element(self.DOWNLOAD_FOLDER)
        self.click_element(self.SELECT_ITEM)
        self.click_element(self.DONE_BTN)

    def upload_back_side(self, is_modify=False):
        if not is_modify:
            self.click_element(self.UPLOAD_BACK_SIDE)

        self.click_element(self.GALLERY_OPTION)
        self.click_element(self.Album_OPTION)
        self.click_element(self.DOWNLOAD_FOLDER)
        self.click_element(self.SELECT_ITEM)
        self.click_element(self.DONE_BTN)

    def delete_front_side(self):
        self.click_element(self.FRONT_PAGE_MENU_BTN)
        self.click_element(self.DELETE_BTN)
        self.click_element(self.DELETE_CONFIRM_BTN)

    def delete_back_side(self):
        self.click_element(self.BACK_PAGE_MENU_BTN)
        self.click_element(self.DELETE_BTN)
        self.click_element(self.DELETE_CONFIRM_BTN)

    def front_page_modify(self):
        self.click_element(self.FRONT_PAGE_MENU_BTN)
        self.click_element(self.MODIFY_BTN)

    def back_page_modify(self):
        self.click_element(self.BACK_PAGE_MENU_BTN)
        self.click_element(self.MODIFY_BTN)

    def is_front_side_uploaded(self):
        try:
            element = self.driver.find_element(*self.DRIVING_FRONT_SIDE_UPLOADED)
            return element.is_displayed()
        except NoSuchElementException:
            return False
        
    def is_back_side_uploaded(self):
        try:
            element = self.driver.find_element(*self.DRIVING_BACK_SIDE_UPLOADED)
            return element.is_displayed()
        except NoSuchElementException:
            return False
