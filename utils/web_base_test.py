import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

load_dotenv()


class WebBaseTest:
    driver = None

    @staticmethod
    def setup():
        print("🌐 Initializing Web driver...")

        browser = os.getenv("browser", "chrome").lower()

        if browser == "firefox":
            options = FirefoxOptions()
            WebBaseTest.driver = webdriver.Firefox(options=options)
        else:
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            WebBaseTest.driver = webdriver.Chrome(options=options)

        WebBaseTest.driver.implicitly_wait(10)

        web_url = os.getenv("web_url")
        if web_url:
            WebBaseTest.driver.get(web_url)

        print("✅ Web driver started successfully")

    @staticmethod
    def tear_down():
        if WebBaseTest.driver:
            WebBaseTest.driver.quit()
            print("🛑 Web driver quit successfully")
