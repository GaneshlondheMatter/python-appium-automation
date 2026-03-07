from selenium.webdriver.common.by import By
import time
import random


class FindARoutePage:
    
    def __init__(self, driver):
        self.driver = driver

    # ---------- BASIC ELEMENTS ----------

    HEADER = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvHeading"]'
    )

    FIND_A_ROUTE_FIELD = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvFindARoute"]'
    )

    FIND_A_ROUTE_INPUT_FIELD = (
        By.XPATH,
        '//android.widget.EditText[@resource-id="com.matter.companion.qa:id/edtFindARoute"]'
    )

    # ---------- LOCATION LIST ----------

    LOCATION_LIST = (
        By.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.matter.companion.qa:id/rvLocations"]'
    )

    LOCATION_ITEMS = (
        By.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.matter.companion.qa:id/rvLocations"]/*'
    )

    # ---------- LOCATION DETAILS ----------

    LOCATION_DETAILS_CARD = (
        By.XPATH,
        '//android.view.ViewGroup[@resource-id="com.matter.companion.qa:id/infoCard"]'
    )

    LOCATION_ICON = (
        By.XPATH,
        '//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/ivLocation"]'
    )

    LOCATION_NAME = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvplaceName"]'
    )

    LOCATION_ADDRESS = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvAddress"]'
    )

    # ---------- ACTION BUTTONS ----------

    DOWNLOAD_BTN = (
        By.XPATH,
        '//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/ivDownload"]'
    )

    SAVE_PRESET_BTN = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvSavePreset"]'
    )

    VIEW_ROUTE = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvViewRoute"]'
    )

    PUSH_TO_VEHICLE_BTN = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvPushToVehcile"]'
    )

    # ---------- ROUTE FLOW ----------

    CHOOSE_START_LOCATION_FIELD = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/etStartDestination"]'
    )

    ROUTE_CARD = (
        By.XPATH,
        '//android.view.ViewGroup[@resource-id="com.matter.companion.qa:id/routeCard"]'
    )

    DIRECTION = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvDirectionRouteCard"]'
    )

    PUSH_TO_VEHICLE_ROUTE = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvPushToVehcileRoute"]'
    )

    # ---------- DIRECTIONS ----------

    START_LOCATION = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvLocationName" and @text="Start Location"]'
    )

    ROUTE_PREVIEW = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvRoutePreview"]'
    )

    ROUTE_PREVIEW_CARD = (
        By.XPATH,
        '//android.view.ViewGroup[@resource-id="com.matter.companion.qa:id/routeDetailDirection"]'
    )

    TURN_BY_TURN_NAVIGATION = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvLocationName"]'
    )

    PREVIOUS_BTN = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/iv_back"]'
    )

    NEXT_BTN = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/iv_forward"]'
    )

    PUSH_TO_VEHICLE_DIRECTION_BTN = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvPushToVehcileRouteDirection"]'
    )

    # ---------- PUSH TO VEHICLE ----------

    BACK_BUTTON = (
        By.XPATH,
        '//android.widget.Button[@resource-id="com.matter.companion.qa:id/buttonBack"]'
    )

    PROCEED_BTN = (
        By.XPATH,
        '//android.widget.Button[@resource-id="com.matter.companion.qa:id/buttonContinue"]'
    )

    SUCCESSFUL_MSG = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvRoute"]'
    )

    OKAY_BTN = (
        By.XPATH,
        '//android.widget.Button[@resource-id="com.matter.companion.qa:id/buttonOkay"]'
    )

    SUCCESS_ICON = (
        By.XPATH,
        '//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/ivError"]'
    )

    PUSHED_ROUTE_CARDS = (
        By.XPATH,
        '//android.view.ViewGroup[@resource-id="com.matter.companion.qa:id/clRoot"]'
    )

    # ---------- SAFE RANDOM SELECTION ----------

    def select_random_location(self):
        time.sleep(2)

        items = self.driver.find_elements(*self.LOCATION_ITEMS)
        if not items:
            raise Exception("❌ No locations found in location list")

        random.choice(items).click()
