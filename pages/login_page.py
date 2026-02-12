from selenium.common import exceptions
from pages.base_page import BasePage

UF=("id","username")
PF=("id","password")
SB=("id","submit")
err_msg=("id","error")

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    def username(self,username):
        self.send_keys(UF,username)
        print(f"Entered Username :{username}")

    def password(self,password):
        self.send_keys(PF,password)
        print(f"Entered Password :{password}")

    def submit(self,submit):
        self.click_element(SB)

    def login(self,username,password):
        self.username(username)
        self.password(password)
        self.submit(self)

    def error(self):
         try:
             return self.get_text(err_msg)
         except exceptions.NoSuchElementException:
             return None







