# @pytest_fixture装饰符中的scope参数
import pytest   

@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield

    print("执行teardown !")
    print("最后关闭浏览器")

@pytest.mark.usefixtures("open")
def test_search1():
    print("test_search1")
    raise NameError
    pass

def test_search2():
    print("test_search2")
    pass

def test_search3():
    print("test_search3")
    pass