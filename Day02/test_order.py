# 导入pytest
import pytest
class TestPytest(object):

    @pytest.mark.order(0)
    def test_one(self):
        print("运行test_one")

    @pytest.mark.order(3)
    def test_two(self):
        print("运行test_two")
    
    # 无标记
    def test_zero(self):
        print("无标记")
    
    @pytest.mark.order(1)
    def test_three(self):
        print("\n运行test_three")


    