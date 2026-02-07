from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
from dotenv import load_dotenv

# load_dotenv()


# class BaseTest:

#     driver = None

#     @staticmethod
#     def setup():
#         try:
#             print("Initializing Appium driver...")

#             options = UiAutomator2Options()
#             options.platform_name = os.getenv("platformName")
#             options.device_name = os.getenv("deviceName")
#             # options.device_name = "Android Emulator"
#             options.platform_version = os.getenv("andrioid_version")
#             # options.platform_version = "11"

#             options.app_package = os.getenv("appPackage")
#             options.app_activity = os.getenv("appActivity")

#             # Important for splash → onboarding → home transitions
#             options.app_wait_activity = "*"

#             options.no_reset = False
#             options.auto_grant_permissions = True
#             options.new_command_timeout = 300

#             BaseTest.driver = webdriver.Remote(
#                 command_executor=os.getenv("appium_server_url"),
#                 options=options
#             )

#             # ✅ GLOBAL implicit wait (applies to ALL find_element calls)
#             BaseTest.driver.implicitly_wait(20)

#             print("✅ Appium driver started successfully")

#         except Exception as e:
#             print("❌ Error starting Appium driver:", e)
#             raise

#     @staticmethod
#     def tear_down():
#         if BaseTest.driver:
#             BaseTest.driver.quit()
#             print("Driver quit successfully")
            


load_dotenv()

class BaseTest:
    driver = None

    @staticmethod
    def setup():
        print("🚀 Initializing Appium driver...")

        appium_url = os.getenv(
            "appium_server_url",
            "http://127.0.0.1:4723/wd/hub"
        )
        print(f"🔗 Appium URL: {appium_url}")

        options = UiAutomator2Options()
        options.platform_name = os.getenv("platformName")
        options.device_name = os.getenv("deviceName")
        options.platform_version = os.getenv("android_version")

        options.app_package = os.getenv("appPackage")
        options.app_activity = os.getenv("appActivity")

        options.app_wait_activity = "*"
        options.auto_grant_permissions = True
        options.no_reset = False
        options.new_command_timeout = 300
        options.automation_name = "UiAutomator2"

        # 🔒 Validate required capabilities
        required_caps = {
            "platformName": options.platform_name,
            "deviceName": options.device_name,
            "platformVersion": options.platform_version,
            "appPackage": options.app_package,
            "appActivity": options.app_activity,
        }

        for cap, value in required_caps.items():
            if not value:
                raise RuntimeError(f"❌ Missing capability: {cap}")

        try:
            BaseTest.driver = webdriver.Remote(
                command_executor=appium_url,
                options=options
            )
            BaseTest.driver.implicitly_wait(15)
            print("✅ Appium driver started successfully")

        except Exception as e:
            print("❌ Failed to start Appium driver")
            raise RuntimeError(e)

    @staticmethod
    def tear_down():
        if BaseTest.driver:
            BaseTest.driver.quit()
            print("🛑 Driver quit successfully")
