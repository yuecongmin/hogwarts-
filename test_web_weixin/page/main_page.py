# *_*coding:utf-8 *_*
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_web_weixin.page.add_member import AddmemberPage
from test_web_weixin.page.base_page import BasePage
from test_web_weixin.page.contact_page import ContactPage


class MainPage(BasePage):
    _location_AddMember = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")
    def goto_add_member(self):
        # 跳转到添加成员页面
        # self前面加上*号，是解元组操作，把元祖内的元素拆分作为不同的参数传入
        # 封装了解元组，可不加*号
        self.find(self._location_AddMember).click()

        return AddmemberPage(self.driver)

    def goto_contact(self):
        # 跳转到通讯录页面
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)


    # def back_main(self):
    #     self.find(By.ID, "menu_index").click()
    #     self.find(By.CSS_SELECTOR, "a[node-type='cancel']").click()