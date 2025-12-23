# fixture的params参数
import pytest

@pytest.fixture(params=[1,2,3])
def data(request):
    # 返回当前fixture的params的迭代值
    return request.param

def test_params(data):
    # f_string语法
    print(f"测试数据：{data}")
    assert data < 3