from utils.base_test import BaseTest
from utils.login_helper import LoginHelper

class TestLoginFlow(BaseTest):

    def test_Verify_login_flow(self):
        self.setup()
        self.driver = BaseTest.driver
        LoginHelper.login_into_matterverse(self.driver)
