from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    try:
        login_page=LoginPage(driver)
        login_page.login("student","Password123")
        assert "logged-in-succesfully" in driver.current_url,login_page.error()
        print("Login Test Passed")

    except Exception as ex:
        print(f"Login test Failed: {ex}")

    finally:
        driver.quit()

test_valid_login()

