from pageObjects.locators import sauceLocators


class loginPage:

    def __init__(self, driver):
        self.driver = driver;

    def getUsernameInput(self):
        return self.driver.find_element(*sauceLocators.username)

    def getPasswordInput(self):
        return self.driver.find_element(*sauceLocators.password)

    def getLoginBtn(self):
        return self.driver.find_element(*sauceLocators.login_btn)

    def getLogErrorMsg(self):
        return self.driver.find_element(*sauceLocators.logerror_msg)



