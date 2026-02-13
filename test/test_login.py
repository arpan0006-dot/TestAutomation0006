
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



def test_valid_login(driver, config):
    login_page = LoginPage(driver)
    login_page.open_login_page(config["base_url"])
    login_page.login(config["valid_username"], config["valid_password"])
    assert "Logged In Successfully" in login_page.get_success_message()


def test_invalid_login(driver):
    login_page=LoginPage(driver)
    login_page.login("Student","password123")
    assert login_page.error() in "Your username is invalid!","No Error Message Shown"
    print("Wrong Credentials Detected")

