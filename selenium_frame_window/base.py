# *_*coding:utf-8 *_*
import os

from selenium import webdriver

class Base():
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()