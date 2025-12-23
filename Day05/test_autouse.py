# 自动执行fixture
import pytest

@pytest.fixture(autouse=True)
def login():
    print("登录")
    # 这个参数下没有办法返回值给测试用例
    # return('tom','123')class TestAutouse:
    def test_case1(self):
        print("执行test_case1")
        assert 1 + 2 == 3
    
    def test_case2(self):
        print("执行test_case2")
        assert 1 == 4

    def test_case3(self):
        print("执行test_case3")
        assert 1 + 2 < 5