# *_*coding:utf-8 *_*
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_web_weixin.page.base_page import BasePage
from test_web_weixin.page.contact_page import ContactPage


class AddmemberPage(BasePage):
    _location_username = (By.ID, "username")
    _locationAdd_acctid = (By.ID, "memberAdd_acctid")
    _locationAdd_phone = (By.ID, "memberAdd_phone")
    _locationAdd_save = (By.CSS_SELECTOR, ".js_btn_save")

    def add_member(self):
        # 添加成员操作,然后回到通讯录页面

        self.driver.find_element(*self._location_username).send_keys("你好")
        self.driver.find_element(*self._locationAdd_acctid).send_keys("001")
        self.driver.find_element(*self._locationAdd_phone).send_keys("15500000000")
        self.driver.find_element(*self._locationAdd_save).click()
        return ContactPage(self.driver)

    def add_member_fail(self, acctid, phone):
        # 添加成功失败操作，数据参数化
        self.driver.find_element(*self._location_username).send_keys("你好")
        self.driver.find_element(*self._locationAdd_acctid).send_keys(acctid)
        self.driver.find_element(*self._locationAdd_phone).send_keys(phone)
        self.driver.find_element(*self._locationAdd_save).click()
        # acctid_error_message = self.driver.find_element(By.CSS_SELECTOR, ".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
        # phonr_error_message = self.driver.find_element(By.CSS_SELECTOR, ".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
        # error_list = [acctid_error_message, phonr_error_message]
        # 打印返回的所有错误信息，返回一个列表形式
        res = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        print(res)
        error_list = [i.text for i in res]
        print(error_list)
        return error_list



