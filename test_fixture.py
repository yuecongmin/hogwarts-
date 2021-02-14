import pytest


@pytest.fixture()
def myfixture():
    print("执行我的fixture")

class Test_fixture():
    def test_one(self):
        print("nihao")