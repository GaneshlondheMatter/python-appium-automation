from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FindMyMatterPage:

    def __init__(self, driver, timeout=25):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ================= LOCATORS =================

    # Header
    HEADER = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvHeading']"
    )

    # Buttons & Icons
    NAVIGATE_TO_VEHICLE_BTN = (
        By.XPATH,
        "//android.widget.TextView[@text='Navigate to Vehicle']"
    )

    NORTH_DIRECTION = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/tvNorthDirection']"
    )

    RECENTER_ICON = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/iv_recenter']"
    )

    BUZZ_MY_VEHICLE = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvBuzzMyVehicleDisabled']"
    )

    # Map
    MAPPLS_MAP = (
        By.XPATH,
        "//android.view.View[contains(@content-desc,'Map created with Mappls')]"
    )

    SURFACE_VIEW = (
        By.XPATH,
        "//android.view.SurfaceView"
    )

    # Navigate Card
    NAVIGATE_TO_VEHICLE_CARD = (
        By.XPATH,
        "//android.view.ViewGroup[@resource-id='com.matter.companion.qa:id/findMyVehicleCard']"
    )

    NAVIGATE_CARD_HEADER = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvCardHeading']"
    )

    DISTANCE = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvDistance']"
    )

    ROAD_ICON = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/iv_road']"
    )

    METER_TEXT = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvMeter']"
    )

    CROSS_ICON = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/crossIcon']"
    )

    # Navigation
    BACK_ARROW_BTN = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivBack']"
    )

    BACK_TO_RECENTER_VIEW_BTN = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/tv3DView']"
    )

    # ================= ELEMENT GETTERS =================

    def header(self):
        return self.wait.until(
            EC.presence_of_element_located(self.HEADER)
        )

    def navigate_to_vehicle_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.NAVIGATE_TO_VEHICLE_BTN)
        )

    def north_direction_icon(self):
        return self.wait.until(
            EC.presence_of_element_located(self.NORTH_DIRECTION)
        )

    def recenter_icon(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.RECENTER_ICON)
        )

    def buzz_my_vehicle(self):
        return self.wait.until(
            EC.presence_of_element_located(self.BUZZ_MY_VEHICLE)
        )

    def mappls_map(self):
        return self.wait.until(
            EC.presence_of_element_located(self.MAPPLS_MAP)
        )

    def navigate_vehicle_card(self):
        return self.wait.until(
            EC.presence_of_element_located(self.NAVIGATE_TO_VEHICLE_CARD)
        )

    def navigate_card_header(self):
        return self.wait.until(
            EC.presence_of_element_located(self.NAVIGATE_CARD_HEADER)
        )

    def distance_text(self):
        return self.wait.until(
            EC.presence_of_element_located(self.DISTANCE)
        )

    def meter_text(self):
        return self.wait.until(
            EC.presence_of_element_located(self.METER_TEXT)
        )

    def back_arrow(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.BACK_ARROW_BTN)
        )

    def back_to_recenter_view_btn(self):
        return self.wait.until(
            EC.presence_of_element_located(self.BACK_TO_RECENTER_VIEW_BTN)
        )

    # ================= ACTIONS =================

    def click_navigate_to_vehicle(self):
        self.navigate_to_vehicle_button().click()

    def click_recenter(self):
        self.recenter_icon().click()

    def click_back(self):
        self.back_arrow().click()

    # ================= VALIDATIONS =================

    def is_back_to_recenter_visible(self):
        try:
            return self.back_to_recenter_view_btn().is_displayed()
        except Exception:
            return False
