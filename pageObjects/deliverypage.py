from pageObjects.locators import SauceLocators

class DeliveryPage:

    def __init__(self, driver):
        self.driver = driver;

    def getFirstNameInput(self):
        return self.driver.find_element(*SauceLocators.first_name)

    def getLastNameInput(self):
        return self.driver.find_element(*SauceLocators.last_name)

    def getPostalCode(self):
        return self.driver.find_element(*SauceLocators.postal_code)

    def getContinueBtn(self):
        return self.driver.find_element(*SauceLocators.continue_btn)
