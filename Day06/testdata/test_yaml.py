# 数据驱动
# 当数据量很大的时候，可以将数据放到yaml文件中，然后读取yaml文件中的数据
# pytest结合yaml实现数据驱动
import pytest
import yaml

@pytest.mark.parametrize("a,b", yaml.safe_load(open("data.yaml",encoding="utf-8")))
def test_add(a,b):
    print(f"a + b = {a + b}")