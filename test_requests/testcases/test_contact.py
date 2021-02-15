# *_*coding:utf-8 *_*
import pytest
import yaml

from test_requests.page.contact_page import Contact


class TestContact:
    def setup_class(self):
        self.contact = Contact()
        self.name = "创建接口"
        self.userid = "005"
        self.upname = "更新接口"

    @pytest.mark.parametrize("corpid,corpsecret,result",
                             [(None, None, 0), ('999', None, 40013)])
    def test_token(self, corpid, corpsecret, result):
        r = self.contact.get_token(corpid, corpsecret)
        assert r.get("errcode") == result
        print(r)

    def test_create(self):
        r = self.contact.create_member(userid=self.userid, name=self.name, mobile="15500000001", department=[1])
        try:
            find_result = self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(userid=self.userid)
        # find_result = self.contact.find_member(self.userid)
        assert r.get("errcode") == 0
        assert find_result["name"] == self.name
        print(r)

    def test_find(self):
        r = self.contact.find_member(userid=self.userid)
        assert r.get("errcode") == 0
        assert r.get("name") == self.name
        print(r)

    def test_update(self):
        r = self.contact.update_member(userid=self.userid, name=self.upname)
        try:
            find_result = self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(self.userid)
        # find_result = self.contact.find_member(self.userid)
        assert r.get("errcode") == 0
        assert find_result["name"] == self.upname
        print(r)

    def test_delete(self):
        r = self.contact.delete_member(userid=self.userid)
        assert r.get("errcode") == 0
        print(r)
