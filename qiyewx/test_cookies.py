# *_*coding:utf-8 *_*
from time import sleep

import pytest
import yaml
from selenium import webdriver

from qiyewx.base import Base


class TestWework(Base):

    @pytest.mark.skip
    def test_fuyong(self):
        # 复用浏览器
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_id("menu_contacts").click()
        print(driver.get_cookies())

    @pytest.mark.skip
    def test_cookie(self):
        # 使用cookie登录,手动复制cookie信息进行登录
        # driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850384791031'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'gRabtrN0WyLCobq9E_wB0X_ADI5oNjdO0DAhEvNChUIyOS3IqrVWUzZKSZxM4QTKNOYSw6e5bd-CTIO6CIG9oX7gZSWV_zulcpbcsqI_zNkt_MxipSGnaIYODsMjUUlALTAMxEfJxviMfdXpmsZelvCmDlEE9yvT2_BEgdLFeFIGJbi2aa1DsrT_Wn-Qr3O2UM2grmMW2TyNfMFQOTyKSFT5tnH4jcIwTCmAenKj335xycDg5ihGpsKBqiyX-TQojp5sHoHNBsnX0mZIUJKd5g'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850384791031'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324966252453'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s6816612638'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'CcDa2qZfz5UMknEwxEzhF3iqfc6yiPPSW2gqyLoy5OIyps8SToK3SEnNdemExLkM'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7643414'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1610463047'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '23902691113045616'}, {'domain': 'work.weixin.qq.com', 'expiry': 1610493532, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '6i61gqb'}, {'domain': '.qq.com', 'expiry': 1610549636, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1641232195.1610461998'}, {'domain': '.qq.com', 'expiry': 1673535236, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2011130803.1610255228'}, {'domain': '.work.weixin.qq.com', 'expiry': 1641791226, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147483650, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'd60647567112d656b1128114e93e2173360ed2040745d030a66553bffd0ba88d'}, {'domain': '.qq.com', 'expiry': 1922872711, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '3d5ef5aa678c2f65'}, {'domain': '.qq.com', 'expiry': 1610463339, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '1821528064'}, {'domain': '.work.weixin.qq.com', 'expiry': 1613055239, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1641999046, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1610255228,1610461998,1610462573,1610463047'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '7452583749'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483657, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'kYp9KAGGHq'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id("menu_contacts").click()
        print(self.driver.get_cookies())
        sleep(3)

    def test_get_cookie(self):
        opt = webdriver.ChromeOptions()
        # 获取cookie存储到yml文件中
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookie = self.driver.get_cookies()
        print(cookie)
        with open("cookie.yml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)

    def test_login(self):
        # 使用序列化cookie的方法进行登录
        self.driver.get("https://work.weixin.qq.com/")
        with open("cookie.yml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id("menu_contacts").click()
        print(self.driver.get_cookies())
        sleep(3)




