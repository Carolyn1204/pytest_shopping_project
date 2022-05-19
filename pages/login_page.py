from selenium import webdriver
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class LoginPage(BasePage):

    login_page_url = "https://www.roots.com/on/demandware.store/Sites-RootsCA-Site/en_CA/Account-Show"
    # page elements
    email = (By.ID, "dwfrm_login_username")
    pwd = (By.ID, "dwfrm_login_password")
    rememberMe = (By.ID, "lbl_dwfrm_login_rememberme")
    signIn_button = (By.ID, "login")
    createNow_button = (By.ID, "create-an-account-now-button")
    track_order = (By.CLASS_NAME, "trackright")
    adver_close = (By.XPATH, "//span[@class='ui-icon ui-icon-closethick']")

    def get_url(self):
        self.open_url(self.login_page_url)

    def login(self, username, password):
        self.input(self.email, username)
        self.input(self.pwd, password)
        self.click(self.rememberMe)
        self.click(self.signIn_button)

    def clear_login(self):
        self.clear(self.email)
        self.clear(self.pwd)

    def create_account(self):
        self.click(self.createNow_button)

    def track_order(self):
        self.click(self.track_order)


if __name__ == '__main__':
    lp = LoginPage(webdriver.Chrome())
    lp.get_url()
