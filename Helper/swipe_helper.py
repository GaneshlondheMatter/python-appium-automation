import time
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException
)

class SwipeHelper:

    def __init__(self, driver):
        self.driver = driver

    # ----------------- Vertical Swipe Down -----------------
    def scroll_down(self):
        window_size = self.driver.get_window_size()
        height = window_size['height']
        width = window_size['width']

        start_x = width // 2
        start_y = int(height * 0.75)
        end_y = int(height * 0.25)

        self._perform_swipe(start_x, start_y, start_x, end_y)
        # time.sleep(0.8)

    def scroll_down_until_visible(self, element_func, max_scrolls=10):
        for _ in range(max_scrolls):
            try:
                element = element_func()
                if element.is_displayed():
                    return True
            except (NoSuchElementException, StaleElementReferenceException):
                pass

            self.scroll_down()

        raise Exception("Element not visible even after scrolling down.")

    # ----------------- Vertical Swipe Up -----------------
    def scroll_up(self):
        window_size = self.driver.get_window_size()
        height = window_size['height']
        width = window_size['width']

        start_x = width // 2
        start_y = int(height * 0.30)
        end_y = int(height * 0.80)

        self._perform_swipe(start_x, start_y, start_x, end_y)
        # time.sleep(0.8)

    def scroll_up_until_visible(self, element_func, max_scrolls=10):
        for _ in range(max_scrolls):
            try:
                element = element_func()
                if element.is_displayed():
                    return True
            except (NoSuchElementException, StaleElementReferenceException):
                pass

            self.scroll_up()

        raise Exception("Element not visible even after scrolling up.")

    # ----------------- Horizontal Swipe Left -----------------
    def swipe_left(self):
        window_size = self.driver.get_window_size()
        height = window_size['height']
        width = window_size['width']

        start_y = height // 2
        start_x = int(width * 0.80)
        end_x = int(width * 0.20)

        self._perform_swipe(start_x, start_y, end_x, start_y)
        # time.sleep(0.8)

    # ----------------- Horizontal Swipe Right -----------------
    def swipe_right(self):
        window_size = self.driver.get_window_size()
        height = window_size['height']
        width = window_size['width']

        start_y = height // 2
        start_x = int(width * 0.20)
        end_x = int(width * 0.80)

        self._perform_swipe(start_x, start_y, end_x, start_y)
        # time.sleep(0.8)

    # ----------------- Private Helper Method -----------------
    def _perform_swipe(self, start_x, start_y, end_x, end_y):
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.actions.action_builder import ActionBuilder
        from selenium.webdriver.common.actions.pointer_input import PointerInput
        from selenium.webdriver.common.actions.interaction import POINTER_TOUCH

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver,
            mouse=PointerInput(POINTER_TOUCH, "touch")
        )

        actions.w3c_actions.pointer_action \
            .move_to_location(start_x, start_y) \
            .pointer_down() \
            .move_to_location(end_x, end_y) \
            .pause(0.2) \
            .pointer_up()

        actions.perform()
