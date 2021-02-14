# *_*coding:utf-8 *_*
from qiyewx.page.index_page import IndexPage


class TestIndex:
    def setup_class(self):
        # 加self实例变量可以在类的其他地方使用
        self.index_page = IndexPage()



    def test_login(self):
        # 1.跳转到登录页面,2.引用登录页面，在登录页面扫码登录
        self.index_page.goto_login().login_scanf()




    def test_register(self):
        # 1.跳转到注册页面，2.在注册页面进行注册
        self.index_page.goto_register().register()