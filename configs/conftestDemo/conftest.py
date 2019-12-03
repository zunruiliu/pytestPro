import pytest

import requests
requests.get("http://www.baidu.com/")

@pytest.fixture()
def login():
    print("登录")