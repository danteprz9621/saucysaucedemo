from pageObjects.locators import sauceLocators

class completePage:

    def __init__(self, driver):
        self.driver = driver;

    def getDispatchedText(self):
        return self.driver.find_element(*sauceLocators.dispatched_text)