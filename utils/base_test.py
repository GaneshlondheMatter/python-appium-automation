from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
from dotenv import load_dotenv

# ✅ ADD THIS
from utils.ssh_tunnel import start_ssh_tunnel, stop_ssh_tunnel

load_dotenv()

class BaseTest:

    driver = None
    ssh_process = None   # ✅ ADD THIS

    @staticmethod
    def setup():
        try:
            print("Initializing Appium driver...")

            # ✅ START SSH TUNNEL (ADDED)
            if BaseTest.ssh_process is None:
                BaseTest.ssh_process = start_ssh_tunnel()

            options = UiAutomator2Options()
            options.platform_name = os.getenv("platformName")
            options.device_name = os.getenv("deviceName")
            options.platform_version = os.getenv("andrioid_version")
            options.app_package = os.getenv("appPackage")
            options.app_activity = os.getenv("appActivity")
            options.app_wait_activity = "*"
            options.no_reset = False
            options.auto_grant_permissions = True
            options.new_command_timeout = 300

            BaseTest.driver = webdriver.Remote(
                command_executor=os.getenv("appium_server_url"),
                options=options
            )

            # ✅ GLOBAL implicit wait (applies to ALL find_element calls)
            BaseTest.driver.implicitly_wait(20)
            print("✅ Appium driver started successfully")

        except Exception as e:
            print("Error starting Appium driver:", e)
            raise

    @staticmethod
    def tear_down():
        if BaseTest.driver:
            BaseTest.driver.quit()
            print("Driver quit successfully")

        # ✅ STOP SSH TUNNEL (ADDED)
        if BaseTest.ssh_process:
            stop_ssh_tunnel(BaseTest.ssh_process)
            BaseTest.ssh_process = None