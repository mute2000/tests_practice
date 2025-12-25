import pytest
import yaml

@pytest.mark.parametrize("a,b", yaml.safe_load(open("data.yaml",encoding="utf-8")))
def test_add(a,b):
    print(f"a + b = {a + b}")