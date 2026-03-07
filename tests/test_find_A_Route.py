from logger import get_logger
from utils.base_test import BaseTest
from pages.control_page import ControlPage
from pages.find_a_route_page import FindARoutePage
from Helper.login_helper import LoginHelper
from Helper.swipe_helper import SwipeHelper
from Helper.scroll_helper import ScrollHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

class TestFindARouteFlow(BaseTest):

    def test_find_a_route_flow(self):
        logger = get_logger(__name__)
        logger.info("===== Starting Find A Route Test Flow =====")

        # -------- Setup --------
        self.setup()
        driver = self.driver
        logger.info("Act I - Driver setup completed")

        control = ControlPage(driver)
        find_a_route = FindARoutePage(driver)
        # swipe = SwipeHelper(driver)
        # scrollHelper = ScrollHelper(driver)

        # -------- Login --------
        logger.info("Act II - Logging into MatterVerse application")
        LoginHelper.login_into_matterverse(driver)
        logger.info("Assert I - Login successful")

        # ------- Scroll to Find-My-Matter -----
        logger.info("Act III - Scrolling to FIND MY MATTER section")
        # scrollHelper.scroll_to_text_contains('FIND MY MATTER')

        logger.info("Act IV - Clicking on Find A Route button")
        control.find_a_route_button().click()

        assert find_a_route.header().is_displayed()
        logger.info("Assert II - Find A Route screen opened successfully")

        # -------- 1. Search Location --------
        time.sleep(3)
        logger.info("Act V - Clicking Find A Route search field")
        find_a_route.find_a_route_field().click()

        time.sleep(2)
        try:
            logger.info("Act VI - Entering location: Bangalore")
            find_a_route.find_a_route_input_field().send_keys("Bangalore")

        except NoSuchElementException:
            logger.info("Act VI.a - Input field not found, retrying")

            find_a_route.find_a_route_field().click()

            input_field = WebDriverWait(driver, 15).until(
                EC.visibility_of(find_a_route.find_a_route_input_field())
            )

            input_field.send_keys("Bangalore")
            logger.info("Act VI.b - Location entered after retry")

        time.sleep(4)

        # -------- 2. Select random location --------
        logger.info("Act VII - Selecting random location from suggestions")
        find_a_route.select_random_location()

        # -------- 3. Verify location details card --------
        logger.info("Assert III - Verifying location details card")
        assert find_a_route.location_details_card().is_displayed()
        assert find_a_route.location_icon().is_displayed()
        assert find_a_route.location_name().is_displayed()
        assert find_a_route.location_address().is_displayed()

        logger.info(f"Assert IV - Location Name displayed: {find_a_route.location_name().text}")
        logger.info(f"Assert V - Location Address displayed: {find_a_route.location_address().text}")

        assert find_a_route.download_btn().is_displayed()
        assert find_a_route.save_preset_btn().is_displayed()
        assert find_a_route.view_route().is_displayed()
        assert find_a_route.push_to_vehicle_btn().is_displayed()
        logger.info("Assert VI - Location action buttons verified")

        # -------- 4. View Route & choose start location --------
        logger.info("Act VIII - Clicking View Route button")
        find_a_route.view_route().click()

        logger.info("Act IX - Choosing start location")
        find_a_route.choose_start_location_field().click()
        find_a_route.find_a_route_input_field().send_keys("Mumbai")
        time.sleep(2)

        logger.info("Act X - Selecting random start location")
        find_a_route.select_random_location()

        # -------- 5. Verify Route Details --------
        logger.info("Assert VII - Verifying route details card")
        assert find_a_route.route_card().is_displayed()
        assert find_a_route.direction().is_displayed()
        assert find_a_route.push_to_vehicle_route().is_displayed()

        # -------- 6. Directions --------
        logger.info("Act XI - Opening Directions page")
        find_a_route.direction().click()

        assert find_a_route.header().text == "Directions"
        logger.info("Assert VIII - Directions page opened successfully")

        # -------- 7. Verify Directions page --------
        logger.info("Assert IX - Verifying directions page elements")
        assert find_a_route.start_location().is_displayed()
        assert find_a_route.route_preview().is_displayed()
        assert find_a_route.push_to_vehicle_route().is_displayed()

        # -------- 8. Route Preview --------
        logger.info("Act XII - Opening route preview")
        find_a_route.route_preview().click()

        assert find_a_route.route_preview_card().is_displayed()
        assert find_a_route.turn_by_turn_navigation().is_displayed()
        assert find_a_route.previous_btn().is_displayed()
        assert find_a_route.next_btn().is_displayed()
        assert find_a_route.push_to_vehicle_direction_btn().is_displayed()
        logger.info("Assert X - Route preview verified")

        # -------- 9. Push To Vehicle --------
        logger.info("Act XIII - Clicking Push To Vehicle button")
        find_a_route.push_to_vehicle_direction_btn().click()

        assert find_a_route.back_button().is_displayed()
        assert find_a_route.proceed_btn().is_displayed()
        logger.info("Assert XI - Push To Vehicle confirmation screen displayed")

        # -------- 10. Proceed --------
        logger.info("Act XIV - Clicking Proceed button")
        find_a_route.proceed_btn().click()
        time.sleep(2)

        assert find_a_route.successful_msg().is_displayed()
        assert find_a_route.okay_btn().is_displayed()
        assert find_a_route.success_icon().is_displayed()
        logger.info("Assert XII - Route pushed successfully")

        # -------- 11. Verify Pushed Routes --------
        logger.info("Act XV - Clicking OK button")
        find_a_route.okay_btn().click()

        assert find_a_route.pushed_route_cards().is_displayed()
        assert find_a_route.header().is_displayed()
        logger.info("Assert XIII - Pushed routes verified")

        logger.info("===== Find A Route Test Flow Completed Successfully =====")