import pytest
import yaml
import allure


def add_fun(a, b):
    return a + b

# 把yaml文件封装起来，使用时直接调用函数
# def get_datas():
#     with open("./demo.yml") as f:
#         datas = yaml.safe_load(f)
#         print(datas)
#         add_datas = datas["datas"]
#         add_ids = datas["myid"]
#         return  [add_datas,add_ids]

class Test_demo():

    # make标签，运行指定的用例,语法：pytest -m "标记名" 文件名 -vs
    @pytest.mark.demo
    # 数据参数化的三种方式
    # 1、数据参数化，数据直接写在参数后面，ids可以给运行数据组起别名，测试数据清晰明了
    # @pytest.mark.parametrize("a, b, expected", [
    #     (3, 5, 8), (-20, 10, -10)
    # ], ids=["int", "minus"])
    # 2、使用yaml打开文件，加载参数,语法：yaml.safe_load(open("文件名"))
    @pytest.mark.parametrize("a, b, expected", yaml.safe_load(open("./demo.yml"))["datas"], ids = yaml.safe_load(open("./demo.yml"))["myid"])
    # 3、封装yaml数据，使用时直接调用，数组需要加上索引，以上三种方式哪种都可以使用
    # @pytest.mark.parametrize("a, b, expected", get_datas()[0], ids = get_datas()[1])
    def test_case1(self, a, b, expected):
        # assert 断言是否成立
        assert add_fun(a, b) == expected

   # make标签，运行指定的用例,语法：pytest -m "标记名" 文件名 -vs
   #  两个标签可以同时使用
   #  @pytest.mark.demo
    @pytest.mark.case
    # 参数组合生成测试用例
    @pytest.mark.parametrize("a", [1, 2])
    @pytest.mark.parametrize("b", [4, 5])
    def test_case2(self, a, b):
        print(f"测试数据组合：a->{a},b->{b}")



