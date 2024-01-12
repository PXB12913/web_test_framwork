import pytest
from utils.data import *
from pages.login import *

@pytest.mark.parametrize("data", get_data('登录'))
def test_login(data):
    page = LoginPage()
    page.to_page()
    page.act(data)
    assert True
