import pytest
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class TestDeleteUser:

    def test_delete_user(self):

        phone_number = "9145496704"
        otp_value = "8319"   # Use valid OTP

        # ---------------------------------
        # ENABLE PERFORMANCE LOGGING
        # ---------------------------------
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        driver = webdriver.Chrome(options=chrome_options)
        wait = WebDriverWait(driver, 30)

        driver.get("https://newsite-qa.matter.in/")

        # Click Login
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
        ).click()

        # Enter phone
        wait.until(
            EC.visibility_of_element_located((By.ID, "mobileNumber"))
        ).send_keys(phone_number)

        driver.find_element(By.XPATH, "//*[@type='submit']").click()

        # Enter OTP
        otp_inputs = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//*[contains(@class,'otp-field__input')]")
            )
        )

        for i in range(4):
            otp_inputs[i].send_keys(otp_value[i])

        driver.find_element(By.XPATH, "//*[@type='submit']").click()

        # Wait for dashboard
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//img[@alt='Matter Black Logo']")
            )
        )

        print("✅ UI Login Successful")

        # ---------------------------------
        # EXTRACT TOKEN FROM NETWORK LOGS
        # ---------------------------------
        logs = driver.get_log("performance")
        token = None

        for log in logs:
            log_json = json.loads(log["message"])["message"]

            if log_json["method"] == "Network.responseReceived":
                response = log_json.get("params", {}).get("response", {})
                url = response.get("url", "")

                # Check validate endpoint
                if "validate" in url:
                    request_id = log_json["params"]["requestId"]

                    try:
                        body = driver.execute_cdp_cmd(
                            "Network.getResponseBody",
                            {"requestId": request_id}
                        )

                        response_data = json.loads(body["body"])

                        token = response_data.get("data", {}).get("userToken")
                        if token:
                            break
                    except Exception:
                        pass

        driver.quit()

        print("Extracted Token:", token)

        assert token is not None, "❌ Token not found in Validate response"

        # ---------------------------------
        # DELETE USER USING TOKEN
        # ---------------------------------
        headers = {
            "Authorization": f"Bearer {token}",
            "x-api-key": "552721c7ca971a196e73",
            "platform": "3",
            "Content-Type": "application/json"
        }

        delete_response = requests.delete(
            "https://orbitqa.matter.in/matter-auth/v1/auth/delete-user",
            headers=headers
        )

        print("Delete Status:", delete_response.status_code)
        print("Delete Response:", delete_response.text)

        assert delete_response.status_code in [200, 204], "❌ User deletion failed"

        print("✅ User deleted successfully")