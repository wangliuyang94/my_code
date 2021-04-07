"""
    登陆页面对象：实现系统登陆流程

    黑心操作流程：
            登陆
    关联元素：
            账号
            密码
            登陆按钮
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginTest(BasePage):

    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    user_input = (By.XPATH, "//*[@name='accounts']")
    pwd_input = (By.XPATH, "//*[@name='pwd']")
    login_buttun = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')

    def login_right(self, username, password):
        self.open(self.url)
        self.input(self.user_input, username)
        self.input(self.pwd_input, password)
        self.wait(3)
        self.click(self.login_buttun)
        self.wait(3)


if __name__ == '__main__':
    LoginTest().login_right('666666', '111111')
