import pytest

def test_search1(open):
    print("test_search1")
    pass

def test_search2(open):
    print("test_search2")
    pass

def test_search3(open):
    print("test_search3")
    pass

# 快捷运行方式，独立的运行入口，当用python运行该文件时，直接运行当前文件框架的测试用例
#判断当前文件是否被直接运行
if __name__ == '_main_':
    # 运行当前文件pytest框架的所有测试用例
    pytest.main()