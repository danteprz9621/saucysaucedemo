from pageObjects.locators import SauceLocators

class ProductPage:

    def __init__(self, driver):
        self.driver = driver;

    def getItemNames(self):
        return self.driver.find_elements(*SauceLocators.item_name)

    def getCartBtns(self):
        return self.driver.find_elements(*SauceLocators.addtocart_btn)

    def getSortBtn(self):
        return self.driver.find_element(*SauceLocators.sort_btn)

    def getLoHiOpt(self):
        return self.driver.find_element(*SauceLocators.lohi_opt)

    def getHiLoOpt(self):
        return self.driver.find_element(*SauceLocators.hilo_opt)

    def getCartBtn(self):
        return self.driver.find_element(*SauceLocators.cart_btn)

    def getItemsInCart(self):
        return self.driver.find_element(*SauceLocators.items_in_cart)

    def getMenuBtn(self):
        return self.driver.find_element(*SauceLocators.menu_btn)

    def getResetAppBtn(self):
        return self.driver.find_element(*SauceLocators.reset_app_menu)

    def getLogoutBtn(self):
        return self.driver.find_element(*SauceLocators.logout_menu)

    def getAboutBtn(self):
        return self.driver.find_element(*SauceLocators.about_menu)

    def getTwitterBtn(self):
        return self.driver.find_element(*SauceLocators.twitter_btn)

    def getFacebookBtn(self):
        return self.driver.find_element(*SauceLocators.fb_btn)

    def getLinkedinBtn(self):
        return self.driver.find_element(*SauceLocators.linkedin_btn)

