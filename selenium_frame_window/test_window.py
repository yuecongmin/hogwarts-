# *_*coding:utf-8 *_*
from time import sleep

from selenium import webdriver
from selenium_frame_window.base import Base
import pytest


class TestWindows(Base):

    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        # print(self.driver.current_window_handle) #打印当前窗口
        # print(self.driver.window_handles)  # 打印所有窗口
        self.driver.find_element_by_link_text("立即注册").click()
        # print(self.driver.current_window_handle) #打印当前窗口
        # print(self.driver.window_handles) #打印所有窗口
        windows = self.driver.window_handles #定义所有窗口
        self.driver.switch_to_window(windows[-1]) #选择最后一个窗口
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("name")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("1550000000")

        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("ruoshui")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("111111")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        # print(self.driver.current_window_handle)  # 打印当前窗口

        sleep(5)
