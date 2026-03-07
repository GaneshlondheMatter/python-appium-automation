import random
import string
from pages.emergency_contact_page import EmergencyContactsPage
from pages.matter_home_page import MatterHomePage
from Helper.login_helper import LoginHelper
from utils.base_test import BaseTest


class TestEmergencyContactFlow(BaseTest):

    # ---------------- COMMON SETUP (Runs Before Every Test) ----------------
    def setup_method(self):
        self.setup()
        self.driver = self.driver

        # Initialize Pages
        self.home_page = MatterHomePage(self.driver)
        self.emergency_page = EmergencyContactsPage(self.driver)

        # Login & Navigate (Before each test)
        LoginHelper.login_into_matterverse(self.driver)
        self.home_page.click_account_tab()
        self.emergency_page.click_emergency_link()

    # ---------------- RANDOM DATA METHODS ----------------
    def generate_random_name(self):
        return "TestUser_" + ''.join(random.choices(string.ascii_letters, k=5))

    def generate_random_phone(self):
        return "9" + ''.join(random.choices(string.digits, k=9))

    # ---------------- TEST 1: DELETE CONTACTS ----------------
    def test_delete_emergency_contacts(self):

        print("Checking for existing emergency contacts...")

        while True:
            try:
                menu_button = self.driver.find_element(
                    *self.emergency_page.get_menu_option_button(1)
                )

                if menu_button.is_displayed():
                    self.emergency_page.delete_existing_contact(1)
                    print("Deleted one emergency contact")
                else:
                    break

            except Exception:
                print("No more emergency contacts to delete")
                break

        print("Delete emergency contact test completed")

    # ---------------- TEST 2: ADD CONTACTS ----------------
    def test_add_emergency_contacts(self):

        add_icons = self.emergency_page.get_add_contact_icons()
        add_icon_count = len(add_icons)

        print(f"Add Contact icons found: {add_icon_count}")
        assert add_icon_count > 0, "No Add Contact icons found"

        for _ in range(add_icon_count):

            random_name = self.generate_random_name()
            random_phone = self.generate_random_phone()

            add_icon = self.driver.find_element(
                *self.emergency_page.get_add_contact_icon(1)
            )

            add_icon.click()

            self.emergency_page.add_new_emergency_contact(
                random_name,
                random_phone
            )

            print(f"Added emergency contact: {random_name} - {random_phone}")

        print("Add emergency contact test completed")