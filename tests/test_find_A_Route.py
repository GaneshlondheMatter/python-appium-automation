from utils.base_test import BaseTest
from pages.control_page import ControlPage
from pages.find_A_Route_Page import FindARoutePage
from Helper.login_helper import LoginHelper
from Helper.swipe_helper import SwipeHelper
from Helper.scroll_helper import ScrollHelper
import time

class TestFindARouteFlow(BaseTest):

    def test_find_a_route_flow(self):
        # -------- Setup --------
        self.setup()
        driver = self.driver

        control = ControlPage(driver)
        find_a_route = FindARoutePage(driver)
        swipe = SwipeHelper(driver)
        scrollHelper = ScrollHelper(driver)

        # -------- Login --------
        LoginHelper.login_into_matterverse(driver)

        #-------Scroll to Find-My-Matter-----
        scrollHelper.scroll_to_text_contains('FIND MY MATTER')

        control.find_a_route_button().click()
        find_a_route.header().is_displayed()

        # -------- 1. Search Location --------
        time.sleep(2)
        find_a_route.find_a_route_field().click()
        time.sleep(2)
        find_a_route.find_a_route_input_field().send_keys("Bangalore")
        time.sleep(4)

        # -------- 2. Select random location --------
        find_a_route.select_random_location()

        # -------- 3. Verify location details card --------
        assert find_a_route.location_details_card().is_displayed()
        assert find_a_route.location_icon().is_displayed()
        assert find_a_route.location_name().is_displayed()
        assert find_a_route.location_address().is_displayed()

        print("Location Name:", find_a_route.location_name().text)
        print("Location Address:", find_a_route.location_address().text)

        assert find_a_route.download_btn().is_displayed()
        assert find_a_route.save_preset_btn().is_displayed()
        assert find_a_route.view_route().is_displayed()
        assert find_a_route.push_to_vehicle_btn().is_displayed()

        # -------- 4. View Route & choose start location --------
        find_a_route.view_route().click()
        find_a_route.choose_start_location_field().click()
        find_a_route.find_a_route_input_field().send_keys("Mumbai")
        time.sleep(2)
        find_a_route.select_random_location()

        # -------- 5. Verify Route Details --------
        assert find_a_route.route_card().is_displayed()
        assert find_a_route.direction().is_displayed()
        assert find_a_route.push_to_vehicle_route().is_displayed()

        # -------- 6. Directions --------
        find_a_route.direction().click()
        assert find_a_route.header().text == "Directions"

        # -------- 7. Verify Directions page --------
        assert find_a_route.start_location().is_displayed()
        assert find_a_route.route_preview().is_displayed()
        assert find_a_route.push_to_vehicle_route().is_displayed()

        # -------- 8. Route Preview --------
        find_a_route.route_preview().click()
        assert find_a_route.route_preview_card().is_displayed()
        assert find_a_route.turn_by_turn_navigation().is_displayed()
        assert find_a_route.previous_btn().is_displayed()
        assert find_a_route.next_btn().is_displayed()
        assert find_a_route.push_to_vehicle_direction_btn().is_displayed()

        # -------- 9. Push To Vehicle --------
        find_a_route.push_to_vehicle_direction_btn().click()
        assert find_a_route.back_button().is_displayed()
        assert find_a_route.proceed_btn().is_displayed()

        # -------- 10. Proceed --------
        find_a_route.proceed_btn().click()
        time.sleep(2)
        assert find_a_route.successful_msg().is_displayed()
        assert find_a_route.okay_btn().is_displayed()
        assert find_a_route.success_icon().is_displayed()

        # -------- 11. Verify Pushed Routes --------
        find_a_route.okay_btn().click()
        assert find_a_route.pushed_route_cards().is_displayed()
        assert find_a_route.header().is_displayed()
