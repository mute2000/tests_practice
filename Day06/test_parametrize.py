# 参数化：把不同的参数写到一个集合里，然后程序自动取值运行用例，直到集合为空。pytest框架使用@pytest.mark.parametrize()
# 使用parametrize实现参数化
import pytest
#把多组测试数据给同一个测试函数，让函数自动循环多次，每次用一组数据
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 5), ("6*9", 54)])  
def test_eval(test_input, expected):
    # eval()函数用来执行一个字符串表达式，并返回表达式的值
    assert eval(test_input) == expected

if __name__ == "__main__":
    pytest.main()  