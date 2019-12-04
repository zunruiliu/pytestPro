"""
根据数据文件获取数据
"""

import json


class DataHandler:
	def __init__(self, filepath):
		self.filepath = filepath

	def read_file(self):
		with open(self.filepath) as fp:
			return fp.read()

	def get_data_form_json(self):
		json_data = json.loads(self.read_file())
		return json_data


if __name__ == '__main__':
	data_handler = DataHandler('data/testdata.json')
	print(data_handler.get_data_form_json())