# 多次使用parametrize
import pytest
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[3,4])
# 运行时离的近的先遍历
def test_data(x,y):
    print(f"测试数据组合x:{x},y:{y}")
    