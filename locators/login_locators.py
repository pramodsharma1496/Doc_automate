from selenium.webdriver.common.by import By


class LoginLocators:
    Email_input = (By.ID, "email")
    Pass_input = (By.ID, "password")
    Submit_click = (By.ID, "next")

    UserName_validation = (By.XPATH, "//*[@id=\"localAccountForm\"]/div[2]/p")
