# utils/login_helper.py
from pages.login_page import LoginPage
import time
import os
from dotenv import load_dotenv

load_dotenv()


class LoginHelper:

    @staticmethod
    def login_into_matterverse(driver):
        
        login_page = LoginPage(driver)

        try:
            # 1️ App launch screen
            print("\nStep 1: Waiting for welcome screen...")
            login_page.wait_for_welcome_screen()

            # 2️ Navigate forward
            print("\nStep 2: Clicking forward arrow...")
            login_page.click_forward_arrow()

            # 3️ Phone number screen
            print("\nStep 3: Waiting for phone number screen...")
            login_page.wait_for_phone_screen()
            login_page.enter_phone_number(os.getenv("phoneNumber"))

            # 4️ Wait for OTP screen and enter OTP
            print("\nStep 4: Waiting for OTP screen...")
            time.sleep(3)
            login_page.enter_otp(os.getenv("OTP"))

            # 5️ Login
            print("\nStep 5: Clicking login...")
            login_page.click_login()

            # 6️ Verify login success (optional - add your verification)
            print("\nStep 6: Verifying login success...")
            time.sleep(5)  # Wait for login to complete
                        
            return True
            
        except Exception as e:
            print(f"\n✗ Login failed with error: {e}")
            # Take screenshot on failure
            driver.save_screenshot("login_failure.png")
            raise