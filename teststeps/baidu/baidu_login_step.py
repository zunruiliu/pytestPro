
from paramspool.handle_param import ParamPool


def test_login():
	data_param = ParamPool().get_param('ccc')
	assert 'hello' == data_param