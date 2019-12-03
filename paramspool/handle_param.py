'''
处理上下游数据依赖
'''


class ParamPool:

	def __init__(self):
		pass

	def get_param(self, param_key):
		"""
		:param param_key:
		:return:
		"""
		return globals()[param_key]

	def set_param(self, param_key, param_data):
		"""
		:param param_key:
		:param param_data:
		:return:
		"""
		globals()[param_key] = param_data
