import pytest
import logging
import inspect
from pageObjects.loginpage import LoginPage
from pageObjects.productpage import ProductPage
from pageObjects.checkoutpage import CheckoutPage
from pageObjects.deliverypage import DeliveryPage
from pageObjects.overviewpage import OverviewPage
from pageObjects.completepage import CompletePage

@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('saucy.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def restart(self):
        self.driver.get("https://www.saucedemo.com/")