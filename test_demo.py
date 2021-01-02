import pytest
import yaml


def add_fun(a, b):
    return a + b


class Test_demo():
    # 数据参数化，数据直接写在参数后面，ids可以给运行数据组起别名，容易看
    @pytest.mark.parametrize("a,b", [
        (3, 5), (-20, 10)
    ], ids=["int", "minus"])
    # 使用yaml打开文件，加载参数,语法：yaml.safe_load(open("文件名"))
    # @pytest.mark.parametrize("a, b", yaml.safe_load(open("./demo.yaml")),ids = ["int", "fushu"])
    def test_case1(self, a, b):
        print("a+b=", a + b)

    # 参数组合生成测试用例
    @pytest.mark.parametrize("a", [1, 2])
    @pytest.mark.parametrize("b", [4, 5])
    def test_case2(self, a, b):
        print(f"测试数据组合：a->{a},b->{b}")
