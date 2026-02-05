# pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver, timeout=25):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------- LOCATORS (UNCHANGED) ----------

    MATTER_LOGO = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivLogo']"
    )

    WELCOME_TEXT = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvHeadTitle']"
    )

    SUB_TEXT = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.matter.companion.qa:id/tvTitle']"
    )

    NEXT_ARROW_BTN = (
        By.XPATH,
        "//android.widget.ImageView[@resource-id='com.matter.companion.qa:id/ivNext']"
    )

    PHONE_NUMBER_INPUT = (
        By.XPATH,
        "//android.widget.EditText[@resource-id='com.matter.companion.qa:id/edtPhoneNumber']"
    )

    GET_OTP_BTN = (
        By.XPATH,
        "//android.widget.Button[@resource-id='com.matter.companion.qa:id/buttonGetOtp']"
    )

    OTP_INPUT_FIELDS = (
        By.XPATH,
        "//android.widget.EditText[contains(@resource-id,'otp_')]"
    )

    LOGIN_BTN = (
        By.XPATH,
        "//android.widget.Button[@resource-id='com.matter.companion.qa:id/buttonlogin']"
    )

    # ---------- ACTIONS ----------

    def wait_for_welcome_screen(self):
        self.wait.until(EC.presence_of_element_located(self.MATTER_LOGO))
        self.wait.until(EC.presence_of_element_located(self.WELCOME_TEXT))
        self.wait.until(EC.presence_of_element_located(self.SUB_TEXT))

    def go_to_phone_screen(self):
        self.wait.until(
            EC.element_to_be_clickable(self.NEXT_ARROW_BTN)
        ).click()

    # ✅ Alias to keep LoginHelper working
    def click_forward_arrow(self):
        self.go_to_phone_screen()

    def wait_for_phone_screen(self):
        self.wait.until(
            EC.visibility_of_element_located(self.PHONE_NUMBER_INPUT)
        )
        self.wait.until(
            EC.presence_of_element_located(self.GET_OTP_BTN)
        )

    def enter_phone_number(self, phone_number):
        phone_input = self.wait.until(
            EC.visibility_of_element_located(self.PHONE_NUMBER_INPUT)
        )
        phone_input.clear()
        phone_input.send_keys(phone_number)

        self.wait.until(
            EC.element_to_be_clickable(self.GET_OTP_BTN)
        ).click()

    def enter_otp(self, otp):
        otp_fields = self.wait.until(
            EC.presence_of_all_elements_located(self.OTP_INPUT_FIELDS)
        )

        for digit, field in zip(otp, otp_fields):
            field.send_keys(digit)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BTN)
        ).click()
