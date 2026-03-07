from utils.base_test import BaseTest
from pages.registration_document_page import RegistrationDocumentPage
from pages.vehicle_settings_page import VehicleSettingsPage
from pages.matter_home_page import MatterHomePage
from Helper.login_helper import LoginHelper
from Helper.upload_helper import UploadProfileHelper
import time


class TestRegistrationUpload(BaseTest):

    def test_upload_registration_document(self):

        self.setup()
        driver = self.driver

        # Page Objects
        registration_page = RegistrationDocumentPage(driver)
        vehicle_settings = VehicleSettingsPage(driver)
        home_page = MatterHomePage(driver)
        upload_helper = UploadProfileHelper(driver)

        # Login
        LoginHelper.login_into_matterverse(driver)

        # Navigate
        home_page.click_account_tab()
        vehicle_settings.click_vehicle_settings_link()
        vehicle_settings.click_documents_link()

        # Open Registration Certificate
        registration_page.click_registration_certificate_section()

        # ---------------- Delete if already uploaded ----------------

        if (
            registration_page.is_registration_uploaded(1)
            and registration_page.is_registration_uploaded(2)
        ):

            # Delete first
            registration_page.click_menu_icon(1)
            registration_page.delete_flow()
            time.sleep(2)

            # After deletion second becomes index 1
            registration_page.click_menu_icon(1)
            registration_page.delete_flow()
            time.sleep(2)

        # ---------------- Upload Both Sides ----------------

        registration_page.click_uploaded_document()
        upload_helper.updateDocumentImage()
        time.sleep(2)

        registration_page.click_uploaded_document()
        upload_helper.updateDocumentImage()
        time.sleep(2)

        # ---------------- Modify Both Sides ----------------

        if (
            registration_page.is_registration_uploaded(1)
            and registration_page.is_registration_uploaded(2)
        ):

            # Modify first
            registration_page.click_menu_icon(1)
            registration_page.modify_flow()
            upload_helper.updateDocumentImage()
            time.sleep(2)

            # Modify second
            registration_page.click_menu_icon(2)
            registration_page.modify_flow()
            upload_helper.updateDocumentImage()
            time.sleep(2)
