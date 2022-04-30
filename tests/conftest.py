from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser")

    match browser_name:
        case 'chrome':
            driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        case 'firefox':
            driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    #driver.close()
