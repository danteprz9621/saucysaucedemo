from pageObjects.locators import sauceLocators

class deliveryPage:

    def __init__(self, driver):
        self.driver = driver;

    def getFirstNameInput(self):
        return self.driver.find_element(*sauceLocators.first_name)

    def getLastNameInput(self):
        return self.driver.find_element(*sauceLocators.last_name)

    def getPostalCode(self):
        return self.driver.find_element(*sauceLocators.postal_code)

    def getContinueBtn(self):
        return self.driver.find_element(*sauceLocators.continue_btn)
