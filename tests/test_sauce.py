from utilities.baseclass import BaseClass
from TestData.logindata import getTestData
from assertpy import assert_that
from selenium import webdriver
from pageObjects.loginpage import LoginPage
from pageObjects.productpage import ProductPage
from pageObjects.checkoutpage import CheckoutPage
from pageObjects.deliverypage import DeliveryPage
from pageObjects.overviewpage import OverviewPage
from pageObjects.completepage import CompletePage

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

    def test_CompletePurchase(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        productpage = ProductPage(self.driver)
        checkoutpage = CheckoutPage(self.driver)
        deliverypage = DeliveryPage(self.driver)
        overviewpage = OverviewPage(self.driver)
        completepage = CompletePage(self.driver)

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

        checkoutpage.getCheckoutBtn().click()

        deliverypage.getFirstNameInput().send_keys(data.get("first name"))

        deliverypage.getLastNameInput().send_keys(data.get("last name"))

        deliverypage.getPostalCode().send_keys(data.get("postal code"))

        deliverypage.getContinueBtn().click()

        overviewpage.getFinishBtn().click()

        assert_that(completepage.getDispatchedText().text).is_equal_to("Your order has been dispatched, and will arrive just as fast as the pony can get there!")

        self.restart()

    def test_InvalidUserLogin(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        data = getTestData(5)
        log.info(data)
        loginpage.getUsernameInput().send_keys(data.get("username"))
        loginpage.getPasswordInput().send_keys(data.get("password"))
        loginpage.getLoginBtn().click()

        log.info(loginpage.getLogErrorMsg().text)

        assert_that(loginpage.getLogErrorMsg().text).is_equal_to("Epic sadface: Username and password do not match any user in this service")
        self.restart()

    def test_Logout(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        productpage = ProductPage(self.driver)
        data = getTestData(1)
        log.info(data)
        loginpage.getUsernameInput().send_keys(data.get("username"))
        loginpage.getPasswordInput().send_keys(data.get("password"))
        loginpage.getLoginBtn().click()

        productpage.getMenuBtn().click()
        productpage.getLogoutBtn().click()

        assert_that(self.driver.current_url).is_equal_to("https://www.saucedemo.com/")

        self.restart()

    def test_LoHiSort(self):
        pass

    def test_HiLoSort(self):
        pass

    def test_MultipleItems(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        productpage = ProductPage(self.driver)
        checkoutpage = CheckoutPage(self.driver)
        deliverypage = DeliveryPage(self.driver)
        overviewpage = OverviewPage(self.driver)
        completepage = CompletePage(self.driver)

        data = getTestData(1)
        log.info(data)
        loginpage.getUsernameInput().send_keys(data.get("username"))
        loginpage.getPasswordInput().send_keys(data.get("password"))
        loginpage.getLoginBtn().click()

        addcartbtns = productpage.getCartBtns()

        i = 0
        for x in productpage.getItemNames():
            addcartbtns[i].click()
            i += 1

        assert_that(int(productpage.getItemsInCart().text)).is_greater_than(1)

        #self.restart()






