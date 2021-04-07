import unittest
from page_object.login_page import LoginTest
from page_object.product import Product
from selenium import webdriver
from ddt import file_data, ddt
from log.log import DemoLog


@ddt
class Cases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.login = LoginTest(cls.driver)
        cls.buy = Product(cls.driver)
        cls.log = DemoLog().log()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @file_data('../data/user_data.yaml')
    def test_01(self, **loc):
        username = loc.get('user')
        password = loc.get('pwd')

        self.login.login_right(username, password)
        self.log.info('登陆账号')

        self.buy.buy()
        self.log.info('购买商品')


if __name__ == '__main__':
    unittest.main()