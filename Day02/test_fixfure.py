import pytest

# @pytest.fixture()   //这个装饰符可以以参数的形式传入到方法里执行。
@pytest.fixture()
def login():
    print("登录")
    return('tom','123')

@pytest.fixture()
def operator():
    print("登录后操作")

# 以参数形式传入，运行后先执行login和operator函数，在执行test_case1，之后是test_case2,最后是login函数，再执行test_case3
def test_case1(login,operator):
    print(login)
    print("case1需要登录")

def test_case2():
    print("无需登录")

def test_case3(login):
    print(login)
    print("case3需要登录") 


# pytest test_fixfure.py -s  //自动识别并执行所有的test_开头的函数
