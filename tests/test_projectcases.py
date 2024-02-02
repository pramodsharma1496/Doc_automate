import time
from telnetlib import EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pages.login import LoginPage
from Pages.Project import ProjectPage
from base import BaseClass
from selenium.webdriver.support.ui import Select


def test_navigateToProject(self):
    login_page = LoginPage(self.driver)
    email = "AdminUser@luvfilms.com"
    password = "Admin@123"
    login_page.enter_email(email)
    login_page.enter_pass(password)
    login_page.click_submit()
    time.sleep(20)
    project_page = ProjectPage(self.driver)
    project_page.clickSideMenu()
    project_page.clickProjectMenu()
    project_page.clickCreateProject()
    time.sleep(10)
    print("Login success")


class Testcase(BaseClass):

    def test_createProject(self):
        test_navigateToProject(self)
        project_page = ProjectPage(self.driver)
        projectname = "Test123"
        project_page.enterProjectName(projectname)
