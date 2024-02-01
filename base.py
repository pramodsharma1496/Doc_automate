from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BaseClass:
    def setup_method(self, method):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://dev-admin-directorofcasting.azurewebsites.net/adminlogin")
        self.driver.implicitly_wait(2000)

    def teardown_method(self, method):
        self.driver.quit()
