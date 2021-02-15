# *_*coding:utf-8 *_*
from typing import List

import requests

from test_requests.page import url
from test_requests.page.base import Base


class Contact(Base):

    def create_member(self, userid: str, name: str, mobile: str, department: List[int], **kwargs):
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        data.update(kwargs)
        r = self.s.post(url.create, json=data)
        return r.json()

    def find_member(self, userid):
        params = {"userid": userid}
        r = self.s.get(url.get, params=params)
        return r.json()

    def update_member(self, userid: str, name: str, **kwargs):
        data = {
            "userid": userid,
            "name": name,
        }
        data.update(kwargs)
        r = self.s.post(url.update, json=data)
        return r.json()

    def delete_member(self, userid):
        params = {"userid": userid}
        r = self.s.get(url.delete, params=params)
        return r.json()
