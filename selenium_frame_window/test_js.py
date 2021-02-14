# *_*coding:utf-8 *_*
from time import sleep
import pytest

from selenium_frame_window.base import Base


class TestJs(Base):
    @pytest.mark.skip
    def test_js(self):
        # 百度输入你好，下滑到最后，点击下一页
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("你好")
        self.driver.find_element_by_id("su").click()
        # 下滑到最后
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        # 点击下一页
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(3)

    def test_time(self):
        # 修改时间控件并返回日期
        self.driver.get("https://www.12306.cn/index/")
        sleep(2)
        # 找到元素并移除属性
        self.driver.execute_script("a = document.getElementById('train_date'); a.removeAttribute('readonly')")
        # 找到元素并赋值
        self.driver.execute_script("document.getElementById('train_date').value='2020-11-11'")
        sleep(3)
        # 返回给元素的赋值
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
