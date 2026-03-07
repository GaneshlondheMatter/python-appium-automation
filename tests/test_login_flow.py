import pytest
from Helper.login_helper import LoginHelper
from utils.base_test import BaseTest

class TestLoginFlow(BaseTest):

    # @pytest.mark.skip(reason="Feature not ready")
    def test_Verify_login_flow(self):
        self.setup()
        self.driver = BaseTest.driver
        LoginHelper.login_into_matterverse(self.driver)
