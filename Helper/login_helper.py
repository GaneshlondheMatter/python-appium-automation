from pages.login_page import LoginPage
import time
import os
from dotenv import load_dotenv
# from Helper.otp_helper import OTPHelper
from Helper.prod_otp_helper import OTPHelper
load_dotenv()

class LoginHelper:

    @staticmethod
    def login_into_matterverse(driver):
        
        login_page = LoginPage(driver)

        try:
            # 1️ App launch screen
            print("\nStep 1: Waiting for welcome screen...")
            # login_page.wait_for_welcome_screen()

            # 2️ Navigate forward
            print("\nStep 2: Clicking forward arrow...")
            login_page.click_forward_arrow()

            # 3️ Phone number screen
            print("\nStep 3: Waiting for phone number screen...")
            # login_page.wait_for_phone_screen()
            
            phone_number = os.getenv("phoneNumber")
            login_page.enter_phone_number(phone_number)

            # 4️ Wait for OTP screen
            print("\nStep 4: Waiting for OTP screen...")
            time.sleep(3)

            # ✅ Fetch OTP from DB
            print("\nFetching OTP from database...")
            otp = OTPHelper.wait_for_otp(phone_number, timeout=60)

            print(f"OTP fetched: {otp}")
            login_page.enter_otp(str(otp))

            # 5️ Login
            print("\nStep 5: Clicking login...")
            login_page.click_login()

            # 6️ Verify login success
            print("\nStep 6: Verifying login success...")
            time.sleep(5)

            return True
            
        except Exception as e:
            print(f"\n✗ Login failed with error: {e}")
            driver.save_screenshot("login_failure.png")
            raise