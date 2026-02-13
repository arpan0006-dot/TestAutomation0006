

# url="https://practicetestautomation.com/practice-test-login/"
# url2="https://testautomationpractice.blogspot.com/"
# @pytest.fixture
# def driver():
#     browser=webdriver.Chrome()
#     browser.maximize_window()
#     browser.get(url)
#     yield browser
#     browser.quit()
#
#
# def driver2():
#     browser = webdriver.Chrome()
#     browser.maximize_window()
#     browser.get(url2)
#     yield browser
#     browser.quit()
#
#

import pytest
from selenium import webdriver
from utilities.config_reader import ConfigReader

@pytest.fixture(scope="session")
def config():
    return ConfigReader.read_config()

@pytest.fixture(scope="session")
def driver(config):
    browser=config["browser"]

    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    else:
        raise Exception(f"Unsupported browser {browser}")


