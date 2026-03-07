from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyPlacesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ================= HEADER & NAVIGATION =================

    HEADER = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvHeading']"
    )

    MY_PLACES_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tv_my_places']"
    )

    PRESET_LOCATION_LINK = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvPresetLocations']"
    )

    # ================= EXISTING PRESETS =================

    EXISTING_PRESET_ONE = (
        By.XPATH,
        "//android.view.ViewGroup[@resource-id='com.matter.companion.qa:id/clPreset1Data']"
    )

    EXISTING_PRESET_TWO = (
        By.XPATH,
        "//android.view.ViewGroup[@resource-id='com.matter.companion.qa:id/clPreset2Data']"
    )

    # ================= MENU & DELETE =================

    MENU_BUTTON_ONE = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivOption1']"
    )

    MENU_BUTTON_TWO = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivOption2']"
    )

    DELETE_OPTION = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvDelete']"
    )

    CONFIRM_DELETE_BTN = (
        By.XPATH,
        "//android.widget.Button[@resource-id='com.matter.companion.qa:id/btnDelete']"
    )

    # ================= ADD PRESET =================

    ADD_PRESET_1 = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivAddPreset1']"
    )

    ADD_PRESET_2 = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivAddPreset2']"
    )

    # ================= FIND A PLACE =================

    FIND_A_PLACE_FIELD = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvFindARoute']"
    )

    FIND_A_PLACE_INPUT_FIELD = (
        By.XPATH,
        "//android.widget.EditText[@resource-id='com.matter.companion.qa:id/edtFindARoute']"
    )

    LOCATIONS_LIST = (
        By.XPATH,
        "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.matter.companion.qa:id/rvRecentLocations']"
    )

    RANDOM_LOCATION = (
        By.XPATH,
        "(//androidx.recyclerview.widget.RecyclerView[@resource-id='com.matter.companion.qa:id/rvRecentLocations']//android.view.ViewGroup)[1]"
    )

    # ================= INFO CARD =================

    INFO_CARD = (
        By.XPATH,
        "//android.view.ViewGroup[@resource-id='com.matter.companion.qa:id/infoCard']"
    )

    LOCATION_ICON = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivLocation']"
    )

    PLACE_NAME = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvplaceName']"
    )

    ADDRESS = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvAddress']"
    )

    CONFIRM_LOCATION_BTN = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvViewRoute']"
    )

    HOME_PRESET_NAME = (
        By.XPATH,
        "//android.widget.EditText[@resource-id='com.matter.companion.qa:id/edtPresetName']"
    )

    SAVE_PRESET = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvSavePreset']"
    )

    # ================= RESULT VALIDATION =================

    ADDED_PLACE_NAME_1 = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvResultLine1']"
    )

    HOME_ADDRESS_NAME = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvAddressHome']"
    )

    ADDED_PLACE_NAME_2 = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvResultLine2']"
    )

    WORK_ADDRESS_NAME = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvAddressWork']"
    )

    SEARCHING_TEXT = (
        By.XPATH,
        "//android.widget.TextView[@text='Searching...']"
    )

    # ================= ACTION METHODS =================

    def delete_existing_presets(self):

        # Delete Preset 1
        try:
            self.wait.until(EC.visibility_of_element_located(self.MENU_BUTTON_ONE)).click()
            self.driver.find_element(*self.DELETE_OPTION).click()
            self.driver.find_element(*self.CONFIRM_DELETE_BTN).click()
        except TimeoutException:
            pass  # Preset 1 not present

        # Delete Preset 2
        try:
            self.wait.until(EC.visibility_of_element_located(self.MENU_BUTTON_TWO)).click()
            self.driver.find_element(*self.DELETE_OPTION).click()
            self.driver.find_element(*self.CONFIRM_DELETE_BTN).click()
        except TimeoutException:
            pass  # Preset 2 not present
