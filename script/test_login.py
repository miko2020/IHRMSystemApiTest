import unittest
from api.login_api import LoginApi
import requests
from utils import assert_fn


# 定义测试类
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 定义测试用例
    # 登录成功
    def test01_login_success(self):
        response = self.login_api.login("13800000002", "123456")
        # 断言
        assert_fn(self, response, 200, True, 10000, "操作成功")
        print(response.json())

    # 用户名不存在
    def test02_login_errorMobile(self):
        response = self.login_api.login("13900000002", "123456")
        assert_fn(self, response, 200, False, 20001, "用户名或密码错误")
        print(response.json())

    # 用户名为空
    def test03_login_nullMobile(self):
        response = self.login_api.login("", "123456")
        assert_fn(self, response, 200, False, 20001, "用户名或密码错误")
        print(response.json())

    # 密码错误
    def test04_login_errorPwd(self):
        response = self.login_api.login("13800000002", "12312")
        assert_fn(self, response, 200, False, 20001, "用户名或密码错误")
        print(response.json())

    # 密码为空
    def test05_login_nullPwd(self):
        response = self.login_api.login("13800000002", "")
        assert_fn(self, response, 200, False, 20001, "用户名或密码错误")
        print(response.json())

    # 无参--特殊处理
    def test06_login_noParams(self):
        response = requests.post("http://182.92.81.159/api/sys/login")
        assert_fn(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！")
        print(response.json())

    # 少参--mobile--特殊处理
    def test07_login_lackMobile(self):
        response = requests.post("http://182.92.81.159/api/sys/login", json={"password": "123456"})
        assert_fn(self, response, 200, False, 20001, "用户名或密码错误")
        print(response.json())

    # 少参--password--特殊处理
    def test08_login_lockPwd(self):
        response = requests.post("http://182.92.81.159/api/sys/login", json={"mobile": "13800000002"})
        assert_fn(self, response, 200, False, 20001, "用户名或密码错误")
        print(response.json())

    # 多参
    def test09_login_moreParams(self):
        response = requests.post("http://182.92.81.159/api/sys/login",
                                 json={"mobile": "13800000002", "password": "123456", "add": "123"})
        assert_fn(self, response, 200, True, 10000, "操作成功！")
        print(response.json())

    # 错误参数
    def test10_login_errorParams(self):
        response = requests.post("http://182.92.81.159/api/sys/login",
                                 json={"mbile": "13800000002", "password": "123456"})
        assert_fn(self, response, 200, False, 20001, "用户名或密码错误")
        print(response.json())


