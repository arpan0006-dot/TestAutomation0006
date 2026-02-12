
from pages.login_page import LoginPage

# def test_valid_login():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://practicetestautomation.com/practice-test-login/")
#     try:
#         login_page=LoginPage(driver)
#         login_page.login("student","Password123")
#         assert "logged-in-succesfully" in driver.current_url,login_page.error()
#         print("Login Test Passed")
#
#     except Exception as ex:
#         print(f"Login test Failed: {ex}")
#
#     finally:
#         driver.quit()
#
# test_valid_login()
#
#

def test_valid_login(driver):
    login_page=LoginPage(driver)
    login_page.login("student","Password123")
    assert "logged-in-successfully" in driver.current_url,login_page.error()

def test_invalid_login(driver):
    login_page=LoginPage(driver)
    login_page.login("Student","password123")
    assert login_page.error() in "Your username is invalid!","No Error Message Shown"
    print("Wrong Credentials Detected")

