# *_*coding:utf-8 *_*
from time import sleep


import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionsChains():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.drive = webdriver.Chrome(options=option)
        self.drive.implicitly_wait(5)

    def teardown(self):
        self.drive.quit()

    @pytest.mark.skip #跳过这条用例，不执行
    def test_actions_click(self):
        self.drive.get("http://sahitest.com/demo/clicks.htm")
        # element = self.drive.find_element(By.CSS_SELECTOR, '.t1')
        # element = self.drive.find_element_by_class_name('t1').click()
        # element = self.drive.find_element_by_xpath("/html/body/form/input[3]")
        element_click = self.drive.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.drive.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.drive.find_element_by_xpath("//input[@value='right click me']")
        element_clearclick = self.drive.find_element_by_xpath("//input[@value='Clear']")

        # 单击，双击，右键单击，清空
        action = ActionChains(self.drive)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        action.click(element_clearclick)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_moveto(self):
        # 鼠标移动，显示菜单栏，将光标移动到某个元素上
        self.drive.get("http://www.baidu.com")
        shezhi = self.drive.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.drive)
        action.move_to_element(shezhi)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        # 移动元素到另一个元素上，drag第一个元素，drop另一个元素
        self.drive.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.drive.find_element_by_id("dragger")
        drop_element = self.drive.find_element_by_xpath("/html/body/div[2]")
        # drop2_element = self.drive.find_element_by_xpath("/html/body/div[3]")

        action = ActionChains(self.drive)
        # 三种移动方法
        action.drag_and_drop(drag_element, drop_element)
        # action.click_and_hold(drag_element).release(drop_element).perform()
        # action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_key(self):
        # 对文本框进行输入、删除
        self.drive.get("http://sahitest.com/demo/label.htm")
        ele = self.drive.find_element_by_xpath("/html/body/label[1]/input")
        action = ActionChains(self.drive)
        action.click(ele)
        action.send_keys("uaername").pause(1) #输入文本
        action.send_keys(Keys.SPACE).pause(1) #输入空格
        action.send_keys("tom").pause(1) #删除文本
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

    @pytest.mark.skip
    def test_touch(self):
        self.drive.get("https://www.baidu.com/")
        baidu = self.drive.find_element_by_id("kw")
        sousuo = self.drive.find_element_by_id("su")
        # xiayiye = self.drive.find_element_by_xpath('//*[@id="page"]/div/a[10]')

        action = TouchActions(self.drive)
        baidu.send_keys("你好")
        action.tap(baidu)
        action.tap(sousuo)
        action.perform()

        action.scroll_from_element(baidu,0,10000).perform()
        # action.tap(xiayiye)
        # action.perform()
        # xiayiye = self.drive.find

        # sleep(3)

    def test_from(self):
        # from表单提交
        self.drive.get("https://testerhome.com/account/sign_in")
        # username = self.drive.find_element_by_id("user_login")
        # password = self.drive.find_element_by_id("user_password")
        # remember = self.drive.find_element_by_id("user_remember_me")
        # login = self.drive.find_element_by_class_name("commit")
        self.drive.find_element_by_id("user_login").send_keys("ruoshui")
        self.drive.find_element_by_id("user_password").send_keys("1111")
        self.drive.find_element_by_id("user_remember_me").click()
        self.drive.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        sleep(2)



