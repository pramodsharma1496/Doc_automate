from locators.Project_locators import ProjectLocators

class ProjectPage:
    def __init__(self,driver):
        self.driver = driver

    def clickSideMenu(self):
        self.driver.find_element(*ProjectLocators.Click_Sidemenu).click()

    def clickProjectMenu(self):
        self.driver.find_element(*ProjectLocators.Click_Projectmenu).click()

    def clickCreateProject(self):
        self.driver.find_element(*ProjectLocators.Click_CreateProject).click()

    def enterProjectName(self,projectname):
        self.driver.find_element(*ProjectLocators.Enter_projectName).send_keys(projectname)

