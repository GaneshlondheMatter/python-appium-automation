from utils.base_test import BaseTest
from Helper.login_helper import LoginHelper
# from utils.login_helper import LoginHelper
from pages.find_my_matter_page import FindMyMatterPage
from pages.control_page import ControlPage
from Helper.swipe_helper import SwipeHelper
# from utils.swipe_helper import SwipeHelper
import time
import os
from PIL import Image
import numpy as np


# ---------- Screenshot Helpers ----------
def take_screenshot(driver, file_name):
    screenshot_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    path = os.path.join(screenshot_dir, file_name)
    driver.save_screenshot(path)
    return path


def images_are_equal(img1_path, img2_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    if img1.size != img2.size:
        return False

    return np.array_equal(
        np.array(img1),
        np.array(img2)
    )


# ---------- Test Class ----------
class TestFindMyMatterFlow(BaseTest):

    def test_find_my_matter_flow(self):
        self.setup()
        driver = self.driver

        # Login
        LoginHelper.login_into_matterverse(driver)

        find_matter = FindMyMatterPage(driver)
        control_page = ControlPage(driver)
        swipe = SwipeHelper(driver)

        # Scroll & click Find My Matter
        swipe.scroll_down_until_visible(
            control_page.find_my_matter_button,
            max_scrolls=8
        )
        control_page.find_my_matter_button().click()

        # ---------- Screenshot 1 ----------
        find_matter.click_navigate_to_vehicle()
        time.sleep(2)
        screenshot_1 = take_screenshot(driver, "after_navigate.png")

        # ---------- Screenshot 2 ----------
        find_matter.click_recenter()
        time.sleep(2)
        screenshot_2 = take_screenshot(driver, "after_recenter.png")

        # ---------- Compare Screenshots ----------
        are_same = images_are_equal(screenshot_1, screenshot_2)

        assert are_same is False, "❌ Screenshots should NOT be identical after recenter action"

        # Back navigation
        find_matter.click_back()
        time.sleep(1)