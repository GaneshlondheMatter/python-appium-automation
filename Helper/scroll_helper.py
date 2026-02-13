from appium.webdriver.common.appiumby import AppiumBy

class ScrollHelper:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_text(self, text, timeout=10):
        """
        Scroll until an element with exact text is visible
        """
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{text}"))'
        )

    def scroll_to_text_contains(self, partial_text):
        """
        Scroll until element containing given text is visible
        """
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().textContains("{partial_text}"))'
        )

    from appium.webdriver.common.appiumby import AppiumBy

    def scroll_down_to_resource_id(self, resource_id):

        return self.driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiScrollable(new UiSelector().scrollable(true))'
        f'.setAsVerticalList()'
        f'.scrollForward()'
        f'.scrollIntoView(new UiSelector().resourceId("{resource_id}"))'
    )

