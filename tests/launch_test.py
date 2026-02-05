from utils.base_test import BaseTest
import time

def main():
    BaseTest.setup()
    try:
        # AndroidDriver-specific method
        print("Current package:", BaseTest.driver.current_package)

        time.sleep(5)  # Just to observe the app

    except Exception as e:
        print("Error during test execution:", e)

    finally:
        BaseTest.tear_down()

if __name__ == "__main__":
    main()