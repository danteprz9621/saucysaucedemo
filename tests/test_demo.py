from utilities.baseclass import BaseClass
import pytest
from TestData.logindata import getTestData

class TestDemo(BaseClass):
    def test_demo1(self):
        log = self.getLogger()
        print("Hi")
        print(getTestData(1))
        log.info(getTestData(1))