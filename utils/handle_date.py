"""
时间日期
"""
import time


class DateHandler:
	def __init__(self):
		pass

	def get_timestamps_millions_str(self):
		"""
		获取当前时间的时间戳字符串(毫秒)
		:param self:
		:return:
		"""
		return str(time.time()*1000).split('.')[0]

	def get_timestamps_str(self):
		"""
		获取当前时间的时间戳字符串(秒)
		:return:
		"""
		return str(time.time()).split('.')[0]

	def get_before_date(self, num):
		"""

		:param num: 几天之前
		:return:
		"""
		pass


if __name__ == '__main__':
	data_handle = DateHandler()
	print(data_handle.get_timestamps_str())



