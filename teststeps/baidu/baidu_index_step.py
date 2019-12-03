from paramspool.handle_param import ParamPool
import allure
import requests


def test_set_param():
	param_pool = ParamPool()
	res = requests.get("https://www.baidu.com/")
	param_pool.set_param('aaa', res)
	param_pool.set_param('bbb', res.headers)
	param_pool.set_param('ccc', 'hello')
	assert res.headers == ParamPool().get_param('bbb')
