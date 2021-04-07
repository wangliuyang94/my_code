"""
    基类：将常用的、项目使用频率高的函数，进行二次封装，设计成自定义方法，便于使用

    常永祥：
        元素定位
        输入
        点击
        退出
        等待
        。。。
"""
from time import sleep


# 创建基类
class BasePage:

    # 初始化一个driver对象
    def __init__(self, driver):
        self.driver = driver

    # 打开网址
    def open(self, url):
        self.driver.get(url)

    # 定位元素
    def find(self, loc):
        return self.driver.find_element(*loc)

    # 输入内容
    def input(self, loc, txt):
        self.find(loc).send_keys(txt)

    # 点击元素
    def click(self, loc):
        self.find(loc).click()

    # 等待时间
    def wait(self, time):
        sleep(time)
