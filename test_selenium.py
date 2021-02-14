# *_*coding:utf-8 *_*

# 导入需要依赖的模块
from time import sleep
import selenium
from selenium import webdriver

# 创建测试类和测试方法
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwards():
    def setup(self):
        # 预置条件，初始化测试环境：浏览器，窗口最大化，隐式等待等
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        # 结束之后回收测试环境，关闭浏览器
        self.driver.quit()

    def test_hogwards(self):
        # 编写测试用例：
        # 打开被测网址、点击或者输入等操作，测试场景等
        # self.driver.get("https://ceshiren.com/")
        # self.driver.find_element_by_link_text("开源项目").click()
        # self.driver.find_element_by_link_text("测试答疑").click()
        # 显示等待的两种方式
        # 1、显示等待，需要定义一个函数，然后传入定义的函数，看是否能通过显示等待的条件
        # 自定义函数需要有参数，x用不上也要写，一定要写给一个参数
        # python传参时不要加()，否则就变成了调用
        # def wait(x):
        #     # len长度是多少个，用find_elements
        #     return len(self.driver.find_elements_by_link_text("最新")) >= 1
        # # python传参时不要加()，否则就变成了调用，wait后面不要写(),需要去掉
        # WebDriverWait(self.driver, 10).until(wait)
        # 2、不用每次都写等待函数，可以用selenium自带的expected_conditions，内置了很多条件可以用
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(By.XPATH,'//*[@class="category-heading"]'))
        # self.driver.find_element_by_link_text("关于“霍格沃兹答疑区”分类").click()
        # 定位元素
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("你好")
        self.driver.find_element(By.CSS_SELECTOR, '[id=su]').click()
        sleep(2)
        # self.driver.close()


