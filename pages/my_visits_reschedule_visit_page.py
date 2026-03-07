from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
# from pages.book_test_ride_page import BookTestRidePage


class MyVisitAndReschedulePage:

    # ---------- LOCATORS ----------

    MY_VISIT_BTN = (
        By.XPATH,
        '//android.widget.Button[@resource-id="com.matter.companion.qa:id/btn_my_visit"]'
    )

    UPCOMING_VISITS_LIST = (
        By.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.matter.companion.qa:id/rv_upcoming_visits"]/android.view.ViewGroup'
    )

    RESCHEDULE_BTN = (
        By.XPATH,
        '//android.widget.Button[@resource-id="com.matter.companion.qa:id/btn_reschedule"]'
    )

    DATE_TEXT = (
        By.XPATH,
        '//android.widget.TextView[@resource-id="com.matter.companion.qa:id/tv_date_value"]'
    )

    RETRY_BTN = (
        By.XPATH,
        '//android.widget.Button[@resource-id="com.matter.companion.qa:id/btn_common_success_failed"]'
    )

    RESCHEDULE_TEST_RIDE_BTN = (
        By.XPATH,
        '//android.widget.Button[@resource-id="com.matter.companion.qa:id/btn_book_test_ride"]'
    )

    # ---------- INIT ----------

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # self.book_test_ride = BookTestRidePage(driver)

    # ---------- ACTIONS ----------

    def open_my_visits(self):
        self.wait.until(EC.visibility_of_element_located(self.MY_VISIT_BTN)).click()

    def open_first_upcoming_visit(self):
        time.sleep(1)
        visits = self.driver.find_elements(*self.UPCOMING_VISITS_LIST)
        if visits:
            visits[0].click()
        else:
            raise Exception("No upcoming visits found")

    def open_reschedule(self):
        self.wait.until(EC.visibility_of_element_located(self.RESCHEDULE_BTN)).click()

    def click_retry(self):
        self.wait.until(EC.visibility_of_element_located(self.RETRY_BTN)).click()

    def confirm_reschedule(self):
        self.wait.until(
            EC.element_to_be_clickable(self.RESCHEDULE_TEST_RIDE_BTN)
        ).click()

    def get_date_value(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.DATE_TEXT)
        )
        return element.text

    # =========================
    # SMART DATE PICK + RESCHEDULE
    # =========================

    def smart_reschedule(self, base_day):

        today_day = datetime.now().day
        print("Today:", today_day)

        days_to_try = []

        if base_day < today_day:
            print("➡️ Base < Today → Move FORWARD next 7 days")
            for i in range(0, 8):
                days_to_try.append(today_day + i)

        elif base_day > today_day:
            print("⬅️ Base > Today → Move BACKWARD last 7 days")
            for i in range(0, 8):
                days_to_try.append(today_day - i)

        else:
            print("🔁 Base == Today → Forward only")
            for i in range(1, 8):
                days_to_try.append(today_day + i)

        print("Days to Try:", days_to_try)

        clicked = False

        for day in days_to_try:
            try:
                print(f"🟡 Trying Day: {day}")

                date_element = self.book_test_ride.get_date_element(day)

                try:
                    WebDriverWait(self.driver, 3).until(
                        EC.visibility_of(date_element)
                    )
                    WebDriverWait(self.driver, 3).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, date_element.get_attribute("xpath"))
                        )
                    )
                except TimeoutException:
                    print(f"⚠️ Day {day} not ready")
                    continue

                try:
                    date_element.click()
                except Exception:
                    print("⚠️ Normal click failed → using tap")
                    self.driver.tap([(date_element.location['x'],
                                      date_element.location['y'])])

                time.sleep(1.5)

                reschedule_btn = self.driver.find_element(
                    *self.RESCHEDULE_TEST_RIDE_BTN
                )

                if reschedule_btn.is_enabled():
                    print("🎯 Reschedule button enabled → clicking")
                    self.confirm_reschedule()
                    clicked = True
                    break
                else:
                    print("❌ Button still disabled → trying next day")

            except Exception as err:
                print(f"❌ Error on day {day}: {err}")

        if not clicked:
            raise Exception("❌ No Suitable Date Found or Button did not enable")
