from pageObjects.locators import SauceLocators

class CompletePage:

    def __init__(self, driver):
        self.driver = driver;

    def getDispatchedText(self):
        return self.driver.find_element(*SauceLocators.dispatched_text)