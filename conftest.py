import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from common import logger
from config import global_parameters as gp


@pytest.fixture()
def get_driver():
    l = logger.LogUtil()
    l.info('******************************** START *******************************')
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()
    l.info('******************************** END **********************************')


@pytest.fixture()
def customer_login(get_driver):
    lp = LoginPage(get_driver)
    lp.get_url()
    lp.login(gp.username, gp.password)
    return get_driver



# if __name__ == '__main__':
#     driver = customer_login

