from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class ItemListPage(BasePage):
    url = "https://www.roots.com/on/demandware.store/Sites-RootsCA-Site/en_CA/Search-Show?q=sweater"
    # page elements
    categories = (
        By.XPATH, "//div[contains(@class,'desktopRefinements')]//div[contains(@class,'categoryrefinement')]/h3/span")
    categories_women = (By.XPATH, "//li[@class='expandable']/a[text()='Women']")
    personalized = (By.XPATH, "//span[text()='Personalized']")
    price_high_to_low = (By.XPATH, "//div[@class='selectric-scroll']//li[text()='Price High to Low']")
    first_item = (By.XPATH, "//a[@class='name-link']//h2[text()='Snowy Fox Open Collar Cardigan']")
    #adver_close = (By.XPATH, "//span[@class='ui-icon ui-icon-closethick']")

    # elements operations
    def choose_categories_women(self):

        # self.open_url(self.url)
        # sleep(3)
        #self.close_popup(self.adver_close)
        self.click(self.categories)
        self.click(self.categories_women)

    def choose_price_high_to_low(self):
        self.click(self.personalized)
        self.click(self.price_high_to_low)

    def choose_item(self):
        self.click(self.first_item)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    il = ItemListPage(driver)
    il.choose_categories_women()
    sleep(3)
    il.choose_price_high_to_low()
    sleep(3)
    il.choose_item()
