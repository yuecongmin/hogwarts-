# *_*coding:utf-8 *_*
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, base_driver=None):
        base_driver: WebDriver  #注解，不是赋值操作，用来做IDE的类型提示
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.get("https://work.weixin.qq.com/")
            self.__cookie_login()
        else:
            self.driver = base_driver

    def __cookie_login(self):

        with open("cookie.yml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def find(self, by, value=None):
        # 封装find_element和解元组操作，直接调用fund即可
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=value)

    def finds(self, by, value=None):
        # 封装find_elements和解元组操作，直接调用funds即可
        if value is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by=by, value=value)

    def wait_click(self, locator):
        # 封装显示等待，使用时可直接调用
        return WebDriverWait(self.driver, 9).until(expected_conditions.
                                            element_to_be_clickable(locator))

    def quit(self):
        # 退出二次封装
        self.driver.quit()
