# @pytest.fixture与@pytest.mark.parametrize结合实现参数化
import pytest
test_data = [("tom","123"),("jerry","456")]
@pytest.fixture()
def login(request):
    user = request.param
    # \n 换行符
    print(f"\n 登录:{user}")
    return "登录成功"

# indirext=True
@pytest.mark.parametrize("login",test_data, indirect=True)
def test_login(login):
    a = login
    print(f"测试数据:{a}")
    assert a != ""
