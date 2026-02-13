from selenium.webdriver.common.by import By


class UploadProfileHelper:

    PROFILE_IMAGE = (
        By.XPATH,
        '//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/ivUserImage"]'
    )

    GALLERY = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvGallery"]'
    )

    SELECT_IMAGE_FROM_PHONE = (
        By.XPATH,
        '(//android.widget.ImageView[@resource-id="com.sec.android.gallery3d:id/thumbnail"])[5]'
    )

    SELECT_IMAGE_ITEM = (
        By.XPATH,
        '//android.widget.FrameLayout[@resource-id="com.sec.android.gallery3d:id/deco_view_layout"]'
    )

    DONE_BUTTON = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvCropDone"]'
    )

    def __init__(self, driver):
        self.driver = driver

    # Upload Profile Image
    def updateProfileImage(self):
        self.driver.find_element(*self.PROFILE_IMAGE).click()
        self.driver.find_element(*self.PROFILE_IMAGE).click()  # Double tap
        self.driver.find_element(*self.GALLERY).click()
        self.driver.find_element(*self.SELECT_IMAGE_FROM_PHONE).click()
        self.driver.find_element(*self.SELECT_IMAGE_ITEM).click()
        self.driver.find_element(*self.DONE_BUTTON).click()

    # Upload Document Image
    def updateDocumentImage(self):
        self.driver.find_element(*self.GALLERY).click()
        self.driver.find_element(*self.SELECT_IMAGE_FROM_PHONE).click()
        self.driver.find_element(*self.SELECT_IMAGE_ITEM).click()
        self.driver.find_element(*self.DONE_BUTTON).click()
