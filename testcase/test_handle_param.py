from teststeps.baidu import baidu_index_step, baidu_login_step


class TestBaiduIndex(object):

	def setup_class(self):
		print("setup")

	def teardown_class(self):
		print("teardown_class")

	def test_baidu_index(self):
		baidu_index_step.test_set_param()
		baidu_login_step.test_login()


