from time import sleep
import allure
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from pages.shopping_bag_page import ShoppingBagPage
from pages.search_bar import SearchBar


class TestEmptyShoppingCart:

    def test_empty_shopping_cart(self, customer_login):
        driver = customer_login
        sb = SearchBar(driver)
        sb.click_bag_icon()
        #sleep(2)
        sb.click_view_bag()
        sbp = ShoppingBagPage(driver)
        sleep(2)
        sbp.click_remove_gift_message()
        sleep(2)
        sbp.click_remove_item()

        bp = BasePage(driver)
        xpath = (By.XPATH, "//span[text()=' No Items in Your Bag']")
        result = bp.get_text(xpath)
        expected_result = 'No Items in Your Bag'
        try:
            assert result == expected_result
        except:
            bp.logger.error('Assert Exception Error')
            bp.save_screenshot('test_02_shopping_error_img')
            allure.attach(driver.get_screenshot_as_png(), name="test_01_shopping_error_img", attachment_type="png")
            raise
        else:
            bp.logger.info('PASS')








