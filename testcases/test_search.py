import pytest
from utils.data import *
from pages.search import *

@pytest.mark.parametrize("data", get_data('搜索'))
def test_search(data):
    page = SearchPage()
    page.to_page()
    page.act(data)
    assert True