import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys, ActionChains, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from common.logger import LogUtil
from config import path
from common import util


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.logger = LogUtil()

    def open_url(self, url):
        try:
            self.driver.get(url)
            self.logger.info("open url:" + str(url))
        except:
            self.logger.error("cannot open the webpage:"+ str(url))

    # def wait_clickable(self, loc, timeout=10, poll=0.2):
    #     try:
    #         wait = WebDriverWait(self.driver, timeout=timeout, poll_frenquency=poll)
    #         element = wait.until(expected_conditions.presence_of_element_located(loc))
    #         return element
    #     except:
    #         self.logger.error("presence cannot find the element" + str(loc))

    def wait_presence(self, loc, timeout=30):
        WebDriverWait(self.driver, timeout=timeout).until(expected_conditions.presence_of_element_located(loc))

    def wait_visible(self, loc, timeout=30):
        WebDriverWait(self.driver, timeout=timeout).until(expected_conditions.visibility_of_element_located(loc))

    def wait_clickable(self, loc, timeout=30):
        WebDriverWait(self.driver, timeout=timeout).until(expected_conditions.element_to_be_clickable(loc))

    def locator(self, loc):
        try:
            element = self.driver.find_element(*loc)
            self.logger.info("locate the element:" + str(loc))
        except:
            self.logger.error('cannot find the element:' + str(loc))
            raise
        return element

    # def locators(self, loc):
    #     try:
    #         elements = self.driver.find_elements(*loc)
    #         self.logger.info("locate the elements:" + str(loc))
    #     except:
    #         self.logger.error('cannot find the elements:' + str(loc))
    #         raise
    #     return elements

    def click(self, loc):
        try:
            # self.wait_visible(loc)
            el = self.locator(loc)
            self.driver.execute_script("arguments[0].click()", el)
            self.logger.info("click the element:" + str(loc))
        except:
            self.logger.error('cannot click the element:' + str(loc))
            raise

    def get_text(self, loc):
        try:
            #self.wait_presence(loc)
            text = self.locator(loc).text
            self.logger.info('get text:' + text)
            return text
        except:
            self.logger.error('cannot get the text')
            raise

    def input(self, loc, txt):
        try:
            self.wait_clickable(loc)
            self.locator(loc).send_keys(txt)
            self.logger.info("input the text:" + txt)
        except:
            self.logger.error('cannot input the txt:' + txt)
            raise

    def clear(self, loc):
        try:
            self.wait_clickable(loc)
            self.locator(loc).clear()
            self.logger.info("clear the element:" + str(loc))
        except:
            self.logger.error('the elements cannot be cleared:' + str(loc))

    def scroll(self, scroll_range):
        self.driver.execute_script(scroll_range)
        self.logger.info("scroll the window:")

    def key_enter(self, loc):
        try:
            self.wait_clickable(loc)
            self.locator(loc).send_keys(Keys.ENTER)
            self.logger.info("enter key in the element of:" + str(loc))
        except:
            self.logger.error("cannot enter key:" + str(loc))
            raise

    def get_attribute(self, loc, attribute_name):
        try:
            self.wait_clickable(loc)
            attri_value = self.locator(loc).get_attribute(attribute_name)
            self.logger.info("get the" + attribute_name + " of:" + str(loc))
            return attri_value
        except:
            self.logger.error("cannot get the" + attribute_name + " of:" + str(loc))
            raise

    def double_click(self, loc):
        try:
            self.wait_clickable(loc)
            element = self.locator(loc)
            action = ActionChains(self.driver)
            action.double_click(element).perform()
        except:
            self.logger.error("cannot double click the element:" + str(loc))

    def drag_and_drop(self, start_loc, end_loc):
        try:
            self.wait_clickable(start_loc)
            start_element = self.locator(start_loc)
            self.wait_clickable(end_loc)
            end_element = self.locator(end_loc)
            action = ActionChains(self.driver)
            action.drag_and_drop(start_element, end_element).perform()
        except:
            self.logger.error("cannot drag from" +str(start_loc)+ " and drop to" +str(end_loc))

    def hover(self, loc):
        try:
            self.wait_presence(loc)
            element = self.locator(loc)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
        except:
            self.logger.error("cannot hover on the element:" + str(loc))

    # def wait_presence(self, loc, timeout=10, poll=0.2):
    #     by = loc.split(",")[0].strip()
    #     by_value = loc.split(",")[1].strip()
    #     if by == "By.ID":

    def switch_to_frame(self, reference, timeout=10, poll=0.2):
        """reference could be name, id, element object, index, locator of the frame"""
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frenquency=poll)
            element = wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(reference))
            return element
        except:
            self.logger.error('cannot switch to the frame:' + reference)
            raise

    def save_screenshot(self, img_name):
        try:
            img_name = img_name + "_" + util.current_time() + ".png"
            img_path = os.path.join(path.img_dir, img_name)
            self.driver.get_screenshot_as_file(img_path)
        except:
            self.logger.error('fail to take a screenshot:' + img_name)

    # def wait_visible(self, loc, timeout=10, poll=0.2):
    #     wait = WebDriverWait(self.driver, timeout=timeout, poll_frenquency=poll)
    #     element = wait.until(expected_conditions.visibility_of_element_located(loc))
    #     return element


if __name__ == '__main__':
    bp = BasePage(webdriver.Chrome())
