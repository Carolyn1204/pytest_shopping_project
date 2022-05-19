from time import sleep

import allure
from selenium.webdriver.common.by import By
from common.yaml_handler import yaml_data
from pages.search_bar import SearchBar
from pages.item_detail_page import ItemDetailPage
from pages.shopping_bag_page import ShoppingBagPage
from pages.item_list_page import ItemListPage
from common.base_page import BasePage


class TestPlaceOrder:

    def test_place_order(self, customer_login):
        driver = customer_login
        # lp = LoginPage(driver)
        # lp.get_url()
        # lp.login(gp.username, gp.password)
        sp = SearchBar(driver)
        sp.search(yaml_data['search_keyword'])
        ilp = ItemListPage(driver)
        ilp.choose_categories_women()
        sleep(3)
        ilp.choose_price_high_to_low()
        sleep(3)
        ilp.choose_item()
        idp = ItemDetailPage(driver)
        idp.choose_color()
        idp.choose_size()
        idp.increase_quantity()
        idp.click_add_to_bag_button()
        sleep(3)
        sb = SearchBar(driver)
        sb.click_view_bag()
        sbp = ShoppingBagPage(driver)
        sbp.click_decrease_item()
        bp = BasePage(driver)
        bp.scroll("scroll(0,300)")
        # sbp.click_include_gift_receipt()
        # sbp.input_gift_message(yaml_data['gift_message'])
        # sbp.click_save_message_button()
        sbp.click_continue_to_checkout()

        xpath = (By.XPATH, "//span[text()=', caro!']")

        result = bp.get_text(xpath)
        expected_result = ', Caro!'
        try:
            assert result == expected_result
        except:
            bp.logger.error('Assert Exception Error')
            bp.save_screenshot('test_01_shopping_error_img')
            allure.attach(driver.get_screenshot_as_png(), name="test_01_shopping_error_img", attachment_type="png")
            raise
        else:
            bp.logger.info('PASS')








