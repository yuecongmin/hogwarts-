# *_*coding:utf-8 *_*
from time import sleep

import pytest

from test_web_weixin.page.main_page import MainPage


class TestAddmember:

    def setup_class(self):
        # 第一次实例化
        self.main = MainPage()

    def teardown_class(self):
        self.main.quit()


    def test_add_member(self):
        # 通过首页添加成员测试用例
        # 1.跳转到添加成功页面，2.添加成员，3.自动跳转到通讯录列表
        res = self.main.goto_add_member().add_member().get_member()
        sleep(3)
        assert "你好" in res


    @pytest.mark.parametrize("acctid, phone, expect_res",
                             [("YueCongMin", "15500000000", "该帐号已被“岳聪敏”占有"),
                              ("001", "15518351120", "该手机号已被“岳聪敏”占有")])
    def test_add_member_fail(self, acctid, phone, expect_res):
        """
        :param acctid: id信息
        :param phone: 手机号信息
        :return:
        """
        # 添加测试用例，当账户存在时判断是否添加成功
        # 第一次参数化，传入重复的acctid,正确的手机号，断言信息
        res = self.main.goto_add_member().add_member_fail(acctid, phone)
        assert expect_res in res

    # def teardown(self):
    #     self.main.back_main()

    def test_add_member_by_contact(self):
        # 通过通讯录页面添加成功
        # 1.跳转到通讯录页面，2.添加成员
        res = self.main.goto_contact().goto_add_member().add_member().get_member()
        sleep(3)
        assert "你好" in res