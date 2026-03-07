from utils.base_test import BaseTest
from pages.insurance_document_page import InsuranceDocumentPage
from pages.vehicle_settings_page import VehicleSettingsPage
from pages.matter_home_page import MatterHomePage
from Helper.login_helper import LoginHelper

class TestInsuranceUpload(BaseTest):

    def test_upload_insurance_document(self):

        # ---------------- Setup ----------------
        self.setup()
        driver = self.driver

        # Page Objects
        insurance_page = InsuranceDocumentPage(driver)
        vehicle_settings = VehicleSettingsPage(driver)
        home_page = MatterHomePage(driver)

        # ---------------- Login ----------------
        LoginHelper.login_into_matterverse(driver)

        # ---------------- Navigation ----------------
        home_page.click_account_tab()

        vehicle_settings.click_vehicle_settings_link()
        vehicle_settings.click_documents_link()

        # Open Insurance Section
        insurance_page.click_insurance_uploaded_link()

        # ---------------- Delete Existing Docs ----------------
        insurance_page.delete_existing_documents()

        # ---------------- Upload Both Sides ----------------
        insurance_page.upload_both_sides()

        # ---------------- Modify Both Sides ----------------
        insurance_page.modify_both_sides()
