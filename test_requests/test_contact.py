# *_*coding:utf-8 *_*
import pytest
import requests


def get_token():
    r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww1272a5cfa00103c9&corpsecret=0Xrczy5xw_S4DWeqb6ftCEPSldm5j--Qb67emRiucX4")
    assert 200 == r.status_code
    assert 0 == r.json()['errcode']
    token = r.json()['access_token']
    return token

def test_get_member():
    get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=001'
    r = requests.get(get_member_url)
    assert '你好' == r.json()['name']
    print(r.json())

def test_update_member():
    update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}'
    data = {
        "userid": "002",
        "name": "你好ya",
    }
    r = requests.post(url=update_member_url, json=data)
    assert 0 == r.json()['errcode']
    print(r.json())

def test_create_member():
    create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data = {
        "userid": "003",
        "name": "好呀好呀",
        "mobile": "13800000003",
        "department": [1]
    }
    r = requests.post(url=create_member_url, json=data)
    assert 0 == r.json()['errcode']
    print(r.json())

def test_delete_member():
    delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=002'
    r = requests.get(delete_member_url)
    assert 0 == r.json()['errcode']
    print(r.json())


@pytest.mark.parametrize("left, right", [(1, 9), (4, 19)])
def test_qidianfa(left, right, pre=1):
    """七点法数据生产"""
    result = []
    # 提取左边界三个值
    lefts = [left - pre, left, left + pre]
    # 提取右边界三个值
    rights = [right - pre, right, right + pre]
    # 提取中间值
    mid = (left + right) // 2
    # 将三组数据组合
    result += lefts
    result.append(mid)
    result += rights
    print(result)
