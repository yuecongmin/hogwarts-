import pytest
import yaml

#数据参数化
# @pytest.mark.parametrize('a', yaml.safe_load(open('./data.yml')))
# @pytest.mark.parametrize('a', file = open('data.yml','r', encoding='UTF-8'))
@pytest.mark.parametrize('a, b',[
    (1,2), (4,3)
])

def test_data1(a, b):
    print(a, b)

