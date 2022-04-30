from pageObjects.locators import sauceLocators

class checkoutPage:

    def __init__(self, driver):
        self.driver = driver;

    def getCheckoutBtn(self):
        return self.driver.find_element(*sauceLocators.checkout_btn)

    def getCartItems(self):
        return self.driver.find_elements(*sauceLocators.cart_item)