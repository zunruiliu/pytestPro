
from utils.handle_param import ParamPool
from utils.handle_data import DataHandler


def test_login():
	data_handler = DataHandler('../../datasource/data/testdata.json')
	json_data = data_handler.get_data_form_json()

	data_param = ParamPool().get_param('ccc')
	assert 'hello' == data_param


if __name__ == '__main__':
	test_login()