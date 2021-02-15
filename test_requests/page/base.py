# *_*coding:utf-8 *_*
import requests
from requests import Session

from test_requests.page import url


class Base:
    def __init__(self):
        self.s = Session()
        self.corpid = 'ww1272a5cfa00103c9'
        self.corpsecret = '0Xrczy5xw_S4DWeqb6ftCEPSldm5j--Qb67emRiucX4'
        self.s.params["access_token"] = self.get_token().get("access_token")

    def get_token(self, corpid=None, corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret

        params = {"corpid": corpid, "corpsecret": corpsecret}
        # r = self.s.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        r = self.s.get(url.gettoken, params=params)
        return r.json()
