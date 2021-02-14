# *_*coding:utf-8 *_*
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_web_weixin.page.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")

    def goto_add_member(self):
        # 解决循环导入的问题
        from test_web_weixin.page.add_member import AddmemberPage
        # 在通讯录页面添加成员
        # 添加显式等待9秒，保证按钮能被点击，显示等待已封装
        self.wait_click(self._location_add_member)
        self.find(self._location_add_member).click()
        return AddmemberPage(self.driver)

    def get_member(self):
        # 获取成功列表,用来做断言信息，
        # 一条用例的结束代表做断言，看是否正确
        sleep(1)
        member_list = self.finds(self._location_member_list)
        print(member_list)
        # 列表推导式，来判断是否在通讯录列表中
        member_list_res = [i.text for i in member_list]
        # member_list_res = []
        # for i in member_list_res:
        #     return i.text
        print("获取通讯录列表", member_list_res)
        return member_list_res
