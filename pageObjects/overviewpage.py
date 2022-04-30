from pageObjects.locators import sauceLocators

class overviewPage:

    def __init__(self, driver):
        self.driver = driver;

    def getFinishBtn(self):
        return self.driver.find_element(*sauceLocators.finish_btn)
