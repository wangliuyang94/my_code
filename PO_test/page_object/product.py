from selenium.webdriver.common.by import By
from base.base_page import BasePage


class Product(BasePage):
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/8.html'
    button = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[2]/div/button')

    def buy(self):
        self.open(self.url)
        self.click(self.button)
        self.wait(2)


if __name__ == '__main__':
    Product().buy()