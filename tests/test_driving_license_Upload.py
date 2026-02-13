from utils.base_test import BaseTest
from pages.Driving_License_Page import DrivingLicensePage
from pages.vehicle_settings_page import VehicleSettingsPage
from pages.matter_home_page import MatterHomePage
# from utils.login_helper import LoginHelper
from Helper.login_helper import LoginHelper
from selenium.common.exceptions import NoSuchElementException           
import time

class TestDrivingLicenseUpload(BaseTest):

    def test_upload_driving_license(self):

        # Setup driver
        self.setup()
        driver = self.driver

        # Create page objects
        driving_license = DrivingLicensePage(driver)
        vehicle_settings = VehicleSettingsPage(driver)
        home_page = MatterHomePage(driver)

        # Login
        LoginHelper.login_into_matterverse(driver)

        # Go to My Matter → Account
        # home_page.click_matter_home_logo()
        # home_page.click_my_matter_tab()
        home_page.click_account_tab()

        # Go to Vehicle Settings → Documents
        vehicle_settings.click_vehicle_settings_link()
        vehicle_settings.click_documents_link()

        # Open Driving License page
        driving_license.open_driving_license_section()

        # Delete already uploaded images (if present)
        if driving_license.is_front_side_uploaded():
            driving_license.delete_front_side()
            time.sleep(3)

        if driving_license.is_back_side_uploaded():
            driving_license.delete_back_side()
            time.sleep(3)


        # Upload front side
        driving_license.upload_front_side(is_modify=False)
        time.sleep(1)

        # Upload back side
        driving_license.upload_back_side(is_modify=False)
        time.sleep(2)

        # Modify front side
        if driving_license.is_front_side_uploaded():
            driving_license.front_page_modify()
            time.sleep(2)
            driving_license.upload_front_side(is_modify=True)
            time.sleep(2)

        # Modify back side
        if driving_license.is_back_side_uploaded():
            driving_license.back_page_modify()
            time.sleep(2)
            driving_license.upload_back_side(is_modify=True)
