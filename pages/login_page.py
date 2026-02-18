from selenium.common import exceptions
from pages.base_page import BasePage

UF=("id","username")
PF=("id","password")
SB=("id","submit")
err_msg=("id","error")
succ_msg=("xpath","//h1[@class='post-title']")

class LoginPage(BasePage):
    def open_login_page(self, base_url):
        self.get_url(f"{base_url}practice-test-login/")
        print(f"url is ")

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

    def get_success_message(self):
        return self.find_element(succ_msg).text


    def error(self):
         try:
             return self.get_text(err_msg)
         except exceptions.NoSuchElementException:
             return None







