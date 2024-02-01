from locators.login_locators import LoginLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(*LoginLocators.Email_input).send_keys(email)

    def enter_pass(self, password):
        self.driver.find_element(*LoginLocators.Pass_input).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*LoginLocators.Submit_click).click()

    def is_error_message_displayed(self):
        return self.driver.find_element(*LoginLocators.UserName_validation).is_displayed()

    def get_error_message(self):
        return self.driver.find_element(
            *LoginLocators.UserName_validation).text if self.is_error_message_displayed() else None
