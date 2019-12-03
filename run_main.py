"""
入口
"""
import pytest
import time

if __name__ == '__main__':
	pytest.main(['-s', "-v", "--html=./report/report+" + str(time.time()) + ".html", "--reruns=3"])

