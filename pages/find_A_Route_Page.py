import time
import random

class FindARoutePage:
    def __init__(self, driver):
        self.driver = driver

    # ---------- BASIC ELEMENTS ----------

    def header(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvHeading"]'
        )

    def find_a_route_field(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvFindARoute"]'
        )

    def find_a_route_input_field(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.EditText[@resource-id="com.matter.companion.qa:id/edtFindARoute"]'
        )

    # ---------- LOCATION LIST ----------

    def location_list(self):
        return self.driver.find_element(
            "xpath",
            '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.matter.companion.qa:id/rvLocations"]'
        )

    def location_items(self):
        return self.driver.find_elements(
            "xpath",
            '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.matter.companion.qa:id/rvLocations"]/*'
        )

    # ---------- LOCATION DETAILS ----------

    def location_details_card(self):
        return self.driver.find_element(
            "xpath",
            '//android.view.ViewGroup[@resource-id="com.matter.companion.qa:id/infoCard"]'
        )

    def location_icon(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/ivLocation"]'
        )

    def location_name(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvplaceName"]'
        )

    def location_address(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvAddress"]'
        )

    # ---------- ACTION BUTTONS ----------

    def download_btn(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/ivDownload"]'
        )

    def save_preset_btn(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvSavePreset"]'
        )

    def view_route(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvViewRoute"]'
        )

    def push_to_vehicle_btn(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvPushToVehcile"]'
        )

    # ---------- ROUTE FLOW ----------

    def choose_start_location_field(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/etStartDestination"]'
        )

    def route_card(self):
        return self.driver.find_element(
            "xpath",
            '//android.view.ViewGroup[@resource-id="com.matter.companion.qa:id/routeCard"]'
        )

    def direction(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvDirectionRouteCard"]'
        )

    def push_to_vehicle_route(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvPushToVehcileRoute"]'
        )

    # ---------- DIRECTIONS ----------

    def start_location(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvLocationName" and @text="Start Location"]'
        )

    def route_preview(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvRoutePreview"]'
        )

    def route_preview_card(self):
        return self.driver.find_element(
            "xpath",
            '//android.view.ViewGroup[@resource-id="com.matter.companion.qa:id/routeDetailDirection"]'
        )

    def turn_by_turn_navigation(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvLocationName"]'
        )

    def previous_btn(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/iv_back"]'
        )

    def next_btn(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/iv_forward"]'
        )

    def push_to_vehicle_direction_btn(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvPushToVehcileRouteDirection"]'
        )

    # ---------- PUSH TO VEHICLE ----------

    def back_button(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.Button[@resource-id="com.matter.companion.qa:id/buttonBack"]'
        )

    def proceed_btn(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.Button[@resource-id="com.matter.companion.qa:id/buttonContinue"]'
        )

    def successful_msg(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tvRoute"]'
        )

    def okay_btn(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.Button[@resource-id="com.matter.companion.qa:id/buttonOkay"]'
        )

    def success_icon(self):
        return self.driver.find_element(
            "xpath",
            '//android.widget.ImageView[@resource-id="com.matter.companion.qa:id/ivError"]'
        )

    def pushed_route_cards(self):
        return self.driver.find_element(
            "xpath",
            '//android.view.ViewGroup[@resource-id="com.matter.companion.qa:id/clRoot"]'
        )

    # ---------- SAFE RANDOM SELECTION ----------

    def select_random_location(self):
        time.sleep(2)  # allow list to populate

        items = self.location_items()
        if not items:
            raise Exception("❌ No locations found in location list")

        random.choice(items).click()
