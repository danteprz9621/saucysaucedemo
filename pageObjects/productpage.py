from pageObjects.locators import sauceLocators

class productPage:

    def __init__(self, driver):
        self.driver = driver;

    def getItemNames(self):
        return self.driver.find_elements(*sauceLocators.item_name)

    def getCartBtns(self):
        return self.driver.find_elements(*sauceLocators.addtocart_btn)

    def getSortBtn(self):
        return self.driver.find_element(*sauceLocators.sort_btn)

    def getLoHiOpt(self):
        return self.driver.find_element(*sauceLocators.lohi_opt)

    def getHiLoOpt(self):
        return self.driver.find_element(*sauceLocators.hilo_opt)

    def getCartBtn(self):
        return self.driver.find_element(*sauceLocators.cart_btn)

    def getItemsInCart(self):
        return self.driver.find_element(*sauceLocators.items_in_cart)

    def getMenuBtn(self):
        return self.driver.find_element(*sauceLocators.menu_btn)

    def getResetAppBtn(self):
        return self.driver.find_element(*sauceLocators.reset_app_menu)

    def getLogoutBtn(self):
        return self.driver.find_element(*sauceLocators.logout_menu)

    def getAboutBtn(self):
        return self.driver.find_element(*sauceLocators.about_menu)

    def getTwitterBtn(self):
        return self.driver.find_element(*sauceLocators.twitter_btn)

    def getFacebookBtn(self):
        return self.driver.find_element(*sauceLocators.fb_btn)

    def getLinkedinBtn(self):
        return self.driver.find_element(*sauceLocators.linkedin_btn)

