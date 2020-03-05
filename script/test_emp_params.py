import unittest

from parameterized import parameterized

from api.emp_api import EmployeeApi
from utils import assert_fn, DbUtils, read_add_emp, read_search_emp, read_modify_emp, read_delete_emp
import app


# 定义测试类
class TestEmployee(unittest.TestCase):
    def setUp(self):
        # 实例化对象
        self.emp_api = EmployeeApi()

    # 1.登录
    def test01_login_success(self):
        response = self.emp_api.login("13800000002", "123456")
        # 获取令牌
        token = "Bearer " + response.json().get("data")
        # 设置请求头,令牌放入请求头中
        headers = {"Content-Type": "application/json", "Authorization": token}
        app.Header = headers

    # 1. 添加员工
    # 数据驱动
    emp_data = read_add_emp(app.absolute_path + "/data/emp.json")

    @parameterized.expand(emp_data)
    def test02_add_emp(self, username, mobile, status_code, success, code, message):
        add_emp_info = [username, mobile]
        response_add = self.emp_api.add_emp(add_emp_info[0], add_emp_info[1], app.Header)
        # 断言
        assert_fn(self, response_add, status_code, success, code, message)
        print(response_add.json())
        # 获取新增员工ID
        emp_id = response_add.json().get("data").get("id")
        app.Emp_id = emp_id

    # 2. 查询员工
    emp_data = read_search_emp(app.absolute_path + "/data/emp.json")

    @parameterized.expand(emp_data)
    def test03_search_emp(self, status_code, success, code, message):
        response_search = self.emp_api.search_emp(app.Emp_id, app.Header)
        # 断言
        assert_fn(self, response_search, status_code, success, code, message)
        print(response_search.json())
        # 与数据库比对--调用utils里面的方法
        with DbUtils("182.92.81.159", "readuser", "iHRM_user_2019", "ihrm") as db:
            sql = "select username from bs_user where id = {}".format(app.Emp_id)
            db.execute(sql)
            result = db.fetchone()
            self.assertEqual("jojo", result[0])

    # 3.修改员工
    emp_data = read_modify_emp(app.absolute_path + "/data/emp.json")

    @parameterized.expand(emp_data)
    def test04_modify_emp(self, username, status_code, success, code, message):
        response_modify = self.emp_api.modify_emp(app.Emp_id, username, app.Header)
        # 断言
        assert_fn(self, response_modify, status_code, success, code, message)
        print(response_modify.json())
        # 与数据库比对
        with DbUtils("182.92.81.159", "readuser", "iHRM_user_2019", "ihrm") as db:
            sql = "select username from bs_user where id = {}".format(app.Emp_id)
            db.execute(sql)
            result = db.fetchone()
            self.assertEqual("new_jojo", result[0])

    # 4.删除员工
    emp_data = read_delete_emp(app.absolute_path + "/data/emp.json")

    @parameterized.expand(emp_data)
    def test05_delete_emp(self, status_code, success, code, message):
        response_delete = self.emp_api.delete_emp(app.Emp_id, app.Header)
        # 断言
        assert_fn(self, response_delete, status_code, success, code, message)
        print(response_delete.json())
        # 与数据库比对
        with DbUtils("182.92.81.159", "readuser", "iHRM_user_2019", "ihrm") as db:
            sql = "select * from bs_user where id = {}".format(app.Emp_id)
            db.execute(sql)
            result = db.fetchone()
            self.assertEqual(None, result)
