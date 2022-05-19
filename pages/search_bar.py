
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class SearchBar(BasePage):
    url = "https://www.roots.com/ca/en/homepage"
    # page elements
    search_icon = (By.XPATH, "//button[@aria-label='Search']/span[@class='header-icon-search']")
    search_input = (By.ID, "searchInput")
    # adver_close = (By.XPATH, "//span[@class='ui-icon ui-icon-closethick']")
    bag_icon = (By.XPATH, "//button[@aria-label='Minicart Icon']/img[@alt='minicart-icon']")
    view_bag = (By.XPATH, "//a[contains(@class,'mini-cart-link-cart')]")

    # elements operations
    def search(self, search_content):
        # self.open_url(self.url)
        # self.maximize_window()
        # self.close_popup()

        self.click(self.search_icon)
        self.click(self.search_input)
        self.input(self.search_input, search_content)
        self.key_enter(self.search_input)

    def click_bag_icon(self):
        self.click(self.bag_icon)

    def click_view_bag(self):
        self.click(self.view_bag)



if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.roots.com/ca/en/homepage")
    # el = driver.find_element(By.XPATH, "//button[@aria-label='Search']/span[text()='U']")
    # driver.execute_script("arguments[0].click()", el)

