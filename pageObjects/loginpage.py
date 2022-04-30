from pageObjects.locators import SauceLocators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver;

    def getUsernameInput(self):
        return self.driver.find_element(*SauceLocators.username)

    def getPasswordInput(self):
        return self.driver.find_element(*SauceLocators.password)

    def getLoginBtn(self):
        return self.driver.find_element(*SauceLocators.login_btn)

    def getLogErrorMsg(self):
        return self.driver.find_element(*SauceLocators.logerror_msg)



