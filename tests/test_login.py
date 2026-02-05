import pytest
@pytest.mark.usefixtures("driver")
class TestLogin:

    def test_app_launch(self):
        print("Running test_app_launch")
        assert self.driver.current_package == "com.matter.companion.qa"
        print("✓ App launched with correct package")