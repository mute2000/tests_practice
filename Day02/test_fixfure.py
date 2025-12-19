import pytest

@pytest.fixture()
def login():
    print("登录")
    return('tom','123')

@pytest.fixture()
def operator():
    print("登录后操作")

def test_case1(login,operator):
    print(login)
    print("case1需要登录")

def test_case2():
    print("无需登录")

def test_case3(login):
    print(login)
    print("case3需要登录") 