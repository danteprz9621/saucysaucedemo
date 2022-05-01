from utilities.baseclass import BaseClass
from TestData.logindata import getTestData
from assertpy import assert_that
from selenium import webdriver
from pageObjects.loginpage import LoginPage
from pageObjects.productpage import ProductPage
from pageObjects.checkoutpage import CheckoutPage

class TestSauce(BaseClass):

    def test_ValidUser(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        data = getTestData(1)
        log.info(data)
        loginpage.getUsernameInput().send_keys(data.get("username"))
        loginpage.getPasswordInput().send_keys(data.get("password"))
        loginpage.getLoginBtn().click()

        assert_that(self.driver.current_url).is_equal_to("https://www.saucedemo.com/inventory.html")
        self.restart()

    def test_AddLabsOnesie(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        productpage = ProductPage(self.driver)
        checkoutpage = CheckoutPage(self.driver)

        data = getTestData(1)
        log.info(data)
        loginpage.getUsernameInput().send_keys(data.get("username"))
        loginpage.getPasswordInput().send_keys(data.get("password"))
        loginpage.getLoginBtn().click()

        addcartbtns = productpage.getCartBtns()

        i = 0
        for x in productpage.getItemNames():
            if x.text == 'Sauce Labs Onesie':
                addcartbtns[i].click()
            i += 1

        productpage.getCartBtn().click()

        items = checkoutpage.getCartItems()

        assert_that(items[0].text).is_equal_to("Sauce Labs Onesie")

        self.restart()




