from utils.base_test import BaseTest
from Helper.login_helper import LoginHelper
from pages.matter_home_page import MatterHomePage
from pages.vehicle_settings_page import VehicleSettingsPage
from pages.my_places_page import MyPlacesPage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestMyPlacesPresetFlow(BaseTest):

    def test_delete_and_add_home_work_presets(self):

        # ----------- Setup Driver -----------
        self.setup()
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        # ----------- Login & Navigation -----------
        LoginHelper.login_into_matterverse(driver)

        home_page = MatterHomePage(driver)
        vehicle_settings = VehicleSettingsPage(driver)
        my_places = MyPlacesPage(driver)

        home_page.click_matter_home_logo()
        home_page.click_my_matter_tab()
        home_page.click_account_tab()

        vehicle_settings.click_vehicle_settings_link()

        wait.until(EC.visibility_of_element_located(my_places.MY_PLACES_LINK)).click()
        wait.until(EC.visibility_of_element_located(my_places.PRESET_LOCATION_LINK)).click()

        # ----------- Delete Existing Presets -----------
        my_places.delete_existing_presets()

        # =====================================================
        #                ADD PRESET 1 (HOME)
        # =====================================================

        wait.until(EC.visibility_of_element_located(my_places.ADD_PRESET_1)).click()
        wait.until(EC.visibility_of_element_located(my_places.FIND_A_PLACE_FIELD)).click()

        wait.until(
            EC.visibility_of_element_located(my_places.FIND_A_PLACE_INPUT_FIELD)
        ).send_keys("Bangalore")

        wait.until(EC.visibility_of_element_located(my_places.RANDOM_LOCATION)).click()

        # ----------- Validate Info Card -----------
        wait.until(EC.visibility_of_element_located(my_places.INFO_CARD))
        wait.until(EC.visibility_of_element_located(my_places.LOCATION_ICON))
        wait.until(EC.visibility_of_element_located(my_places.PLACE_NAME))
        wait.until(EC.visibility_of_element_located(my_places.ADDRESS))
        wait.until(EC.visibility_of_element_located(my_places.CONFIRM_LOCATION_BTN))

        info_place_name_1 = driver.find_element(*my_places.PLACE_NAME).text
        info_address_1 = driver.find_element(*my_places.ADDRESS).text

        driver.find_element(*my_places.CONFIRM_LOCATION_BTN).click()

        wait.until(
            EC.visibility_of_element_located(my_places.HOME_PRESET_NAME)
        ).send_keys("MyHome")

        driver.find_element(*my_places.SAVE_PRESET).click()

        # ----------- Validate Home Preset -----------
        wait.until(
            EC.text_to_be_present_in_element(
                my_places.ADDED_PLACE_NAME_1, info_place_name_1
            )
        )

        wait.until(
            EC.text_to_be_present_in_element(
                my_places.HOME_ADDRESS_NAME, info_address_1
            )
        )

        # =====================================================
        #                ADD PRESET 2 (WORK)
        # =====================================================

        wait.until(EC.visibility_of_element_located(my_places.ADD_PRESET_2)).click()
        wait.until(EC.visibility_of_element_located(my_places.FIND_A_PLACE_FIELD)).click()

        wait.until(
            EC.visibility_of_element_located(my_places.FIND_A_PLACE_INPUT_FIELD)
        ).send_keys("Electronic City")

        wait.until(EC.visibility_of_element_located(my_places.RANDOM_LOCATION)).click()

        info_place_name_2 = driver.find_element(*my_places.PLACE_NAME).text
        info_address_2 = driver.find_element(*my_places.ADDRESS).text

        driver.find_element(*my_places.CONFIRM_LOCATION_BTN).click()

        wait.until(
            EC.visibility_of_element_located(my_places.HOME_PRESET_NAME)
        ).send_keys("MyWork")

        driver.find_element(*my_places.SAVE_PRESET).click()

        # ----------- Validate Work Preset -----------
        wait.until(
            EC.text_to_be_present_in_element(
                my_places.ADDED_PLACE_NAME_2, info_place_name_2
            )
        )

        wait.until(
            EC.text_to_be_present_in_element(
                my_places.WORK_ADDRESS_NAME, info_address_2
            )
        )

        print("✅ My Places Preset Location Flow completed successfully")

        driver.quit()