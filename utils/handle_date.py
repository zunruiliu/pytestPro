"""
时间日期
"""
import time
import datetime


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

	def get_now_formatter(self, formatter_str):
		"""
		:param formatter_str:时间的格式
		:return:
		"""
		return time.strftime(formatter_str, time.localtime())

	def get_before_date(self, num, formatter_str):
		"""
		:param num: 几天之前
		:param formatter_str:时间格式
		:return:
		"""
		today = datetime.datetime.now()
		offset = datetime.timedelta(days=-num)
		before_date = (today + offset).strftime(formatter_str)
		return before_date


if __name__ == '__main__':
	data_handle = DateHandler()
	print(data_handle.get_timestamps_str())
	print(data_handle.get_now_formatter('%Y-%m-%d'))
	print(data_handle.get_now_formatter('%Y-%m-%d %H:%M:%S'))
	print(data_handle.get_before_date(1, '%Y-%m-%d %H:%M:%S'))



