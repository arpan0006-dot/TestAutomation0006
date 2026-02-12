
import pytest
from selenium import webdriver

url="https://practicetestautomation.com/practice-test-login/"
url2="https://testautomationpractice.blogspot.com/"
@pytest.fixture
def driver():
    browser=webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)
    yield browser
    browser.quit()


def driver2():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url2)
    yield browser
    browser.quit()

