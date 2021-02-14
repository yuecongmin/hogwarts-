# *_*coding:utf-8 *_*
from time import sleep

from selenium_frame_window.base import Base

class Testfile(Base):
    def test_file(self):
        # 文件上传用send_keys可以实现
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys("E:\图片\微信图片_20201212213922.jpg")
        sleep(5)