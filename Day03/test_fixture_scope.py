# @pytest_fixture装饰符中的scope参数
import pytest   

# 该模块这个操作只需要执行一次，使用这个参数后只会进行一次操作，避免了占用系统资源
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    # fixture的分隔符，yield之前的是前置操作，测试用例执行前执行，yield之后的是后置操作
    yield

    print("执行teardown !")
    print("最后关闭浏览器")

# 装饰符触发fixture
@pytest.mark.usefixtures("open")
def test_search1():
    print("test_search1")
    # 模拟测试用例失败的场景
    raise NameError
    pass
# 参数触发fixture
def test_search2(open):
    print("test_search2")
    pass

def test_search3(open):
    print("test_search3")
    pass