# saucysaucedemo

Directory ditribution:

├───docs - Contains test cases (some of them are meant to be implemented later)
├───pageObjects - Contains locators and POM 
├───TestData - Contains test data in xlsx format
├───tests - Contains conftest for pytest and test cases
├───utilities - Contains base class for tests

External libraries used:

assertpy:
pip install assertpy

selenium:
pip install selenium

pytest:
pip install pytest

openpyxl:
pip install openpyxl

Usage:

Inside the tests directory run:

py.test (default browser is chrome)
py.test --browser chrome
py.test --browser firefox

Log file for all tests is stored in the saucy.log file inside tests directory.

Driver paths in the project are stored in the tests directory, inside conftest.py. (Mine were located on C:\\).

chromedriver.exe - https://chromedriver.chromium.org/ - Chrome Driver
geckodriver.exe - https://github.com/mozilla/geckodriver/releases - Firefox Driver

Python version: 3.10.1
