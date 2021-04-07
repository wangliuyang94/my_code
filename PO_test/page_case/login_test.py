import unittest
from page_object.login_page import LoginTest
from selenium import webdriver
from ddt import file_data, ddt
from log.log import DemoLog
from selenium.webdriver.common.by import By


@ddt
class Cases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = DemoLog().log()

    @classmethod
    def tearDownClass(cls):
        cls.log.info('登陆功能测试结束')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login = LoginTest(self.driver)

    def tearDown(self):
        self.driver.quit()

    @file_data('../data/user_data.yaml')
    def test_01(self, **loc):
        username = loc.get('user')
        password = loc.get('pwd')

        self.login.login_right(username, password)
        key = self.login.find((By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/em[2]')).text
        self.assertEqual('666666，欢迎来到', key, msg='登陆失败')
        self.log.info('登陆成功了')


if __name__ == '__main__':
    unittest.main()