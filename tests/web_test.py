import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.web_base_test import WebBaseTest

class TestWebLogin(WebBaseTest):

    def setup_method(self):
        self.setup()
        self.driver = WebBaseTest.driver
        self.wait = WebDriverWait(self.driver, 15)

    def test_flipkart_e2e(self):
        # Scenario 1: Navigate to Flipkart and Search
        self.driver.get("https://www.flipkart.com")
        
        # Close login popup if it appears
        try:
            close_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='_30XB9F']")))
            close_btn.click()
            print("Closed login popup")
        except:
            print("Login popup not found")

        # Search for iPhone 15
        search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys("Samsung Galaxy S24")
        search_box.send_keys(Keys.ENTER)
        print("Searched for Samsung Galaxy S24")

        # Scenario 2: Verify Search Results and Filter
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Showing 1 –')]" )))
        print("Search results verified")

        # Scenario 3: Click on the first product
        first_product = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@href, '/p/')])[1]")))
        product_name_el = first_product.find_element(By.XPATH, ".//div[contains(text(), 'Samsung') or contains(text(), 'Galaxy')]" )
        product_name = product_name_el.text
        print(f"Clicking on product: {product_name}")
        first_product.click()

        # Handle New Tab or Same Tab
        time.sleep(2)
        if len(self.driver.window_handles) > 1:
            original_window = self.driver.current_window_handle
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    print("Switched to new tab")
                    break
        else:
            print("Product opened in the same tab")
        
        # Scenario 4: Add to Cart
        add_to_cart_xpath = "//button[not(@disabled) and (contains(., 'ADD TO CART') or contains(., 'Add to cart'))]"
        add_to_cart_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_btn)
        time.sleep(1) # Small wait to ensure scroll completes
        add_to_cart_btn.click()
        print("Added to cart")
        time.sleep(3) # Wait for cart to update or page to navigate

        # Scenario 5: Verify Cart and Remove Item
        # Wait for cart page to load, or click cart icon if not redirected
        try:
            self.wait.until(EC.url_contains("viewcart"))
            print("Redirected to cart page successfully")
        except:
            print("Not redirected to cart, attempting to click cart icon")
            cart_icon_xpath = "//a[contains(@href, '/viewcart')]"
            cart_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, cart_icon_xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", cart_icon)
            time.sleep(1)
            cart_icon.click()
            self.wait.until(EC.url_contains("viewcart"))
            print("Navigated to cart page via cart icon")

        # Verify product is in cart and visible 'Remove' button
        remove_btn_in_cart_xpath = "//div[text()='Remove']"
        self.wait.until(EC.presence_of_element_located((By.XPATH, remove_btn_in_cart_xpath)))
        print("Verified product is in cart")

        # Remove item from cart
        # First, try to close any potential overlay that might be intercepting clicks
        try:
            # This XPath targets a common close button for overlays on Flipkart
            overlay_close_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., '✕')]" )))
            overlay_close_btn.click()
            print("Closed an intervening overlay before removing item.")
            time.sleep(1) # Give some time for the overlay to disappear
        except:
            print("No intervening overlay found or clickable before removing item.")

        remove_btns = self.driver.find_elements(By.XPATH, remove_btn_in_cart_xpath)
        if remove_btns:
            remove_element = self.wait.until(EC.element_to_be_clickable(remove_btns[0]))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", remove_element)
            time.sleep(1) # Small wait after scroll
            try:
                remove_element.click()
            except:
                self.driver.execute_script("arguments[0].click();", remove_element)
            print("Clicked Remove button in cart")
            
            # Confirm removal in popup
            time.sleep(2) # Added a sleep to wait for any overlay to disappear
            confirm_remove_xpath = "//div[contains(@class, 'sBxzFz') and text()='Remove']"
            confirm_remove = self.wait.until(EC.element_to_be_clickable((By.XPATH, confirm_remove_xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", confirm_remove)
            time.sleep(1) # Small wait after scroll
            try:
                confirm_remove.click()
            except:
                self.driver.execute_script("arguments[0].click();", confirm_remove)
            print("Confirmed item removal from cart")

            # Verify cart is empty
            empty_msg_xpath = "//div[contains(text(), 'Your cart is empty!')]"
            self.wait.until(EC.presence_of_element_located((By.XPATH, empty_msg_xpath)))
            print("Cart is now empty")
        else:
            print("Remove button not found in cart, skipping removal")

    def teardown_method(self):
        self.tear_down()