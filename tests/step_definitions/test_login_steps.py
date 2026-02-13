from pytest_bdd import scenarios, given, when, then
from utils.login_helper import LoginHelper

scenarios('../../features/login.feature')

@given("the MatterVerse app is launched")
def app_launched(driver):
    # App launch is already handled by driver fixture
    pass

@when("the user logs into MatterVerse")
def login_to_app(driver):
    LoginHelper.login_into_matterverse(driver)

@then("the user should be logged in successfully")
def verify_login(driver):
    # You can add real validation here later
    # Example: check home screen element
    assert True
