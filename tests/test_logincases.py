import time

import pytest

from Pages.login import LoginPage
from base import BaseClass


class Testcase(BaseClass):
    @pytest.fixture
    def test_successful_login(self):
        login_page = LoginPage(self.driver)
        email = "AdminUser@luvfilms.com"
        password = "Admin@123"
        login_page.enter_email(email)
        login_page.enter_pass(password)
        login_page.click_submit()
        time.sleep(20)
        assert "Dashboard" in self.driver.title
        print("Login success")

    @pytest.mark.parametrize("emailID, password, expected_error_message", [
        ("AdminUser@luvfilms.com", "test123", "Your password is incorrect"),
        ("AdminUser1@luvfilms.com", "Admin@123", "We can't seem to find your account,Self Failing"),
        ("AdminUser1@luvfilms.com", "test123", "We can't seem to find your account")
    ])
    def test_username_validation(self, emailID, password, expected_error_message):
        login_page = LoginPage(self.driver)

        login_page.enter_email(emailID)
        login_page.enter_pass(password)
        login_page.click_submit()
        time.sleep(10)
        assert login_page.is_error_message_displayed()
        assert login_page.get_error_message() == expected_error_message


if __name__ == "__main__":
    pytest.main()
