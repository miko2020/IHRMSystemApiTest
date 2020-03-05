import unittest

from parameterized import parameterized

from api.login_api import LoginApi
from app import absolute_path
from utils import assert_fn, get_login_data


# 定义测试类
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()

    # 定义测试用例
    login_data = get_login_data(absolute_path + "/data/login.json")

    @parameterized.expand(login_data)
    def test01_login_success(self, mobile, password, status_code, success, code, message):
        response = self.login_api.login(mobile, password)
        # 断言
        assert_fn(self, response, status_code, success, code, message)
        print(response.json())

