# import pytest
# from appium import webdriver
# from appium.options.android import UiAutomator2Options


# @pytest.fixture(scope="class")
# def driver(request):
#     print("\nStarting Appium driver...")

#     options = UiAutomator2Options()
#     options.platform_name = "Android"
#     options.device_name = "RZCXA02WYYH"
#     options.platform_version = "16"
#     options.app_package = "com.matter.companion.qa"
#     options.app_wait_activity = "*"
#     options.no_reset = False
#     options.auto_grant_permissions = True
#     options.new_command_timeout = 300

#     driver = webdriver.Remote(
#         command_executor="http://127.0.0.1:4723",
#         options=options
#     )

#     # 🔥 Make driver available to test class
#     request.cls.driver = driver

#     yield driver   # 👉 test execution happens here

#     print("\nQuitting Appium driver...")
#     driver.quit()
