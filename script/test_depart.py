import unittest
from api.depart_api import DepartApi
import app
from utils import assert_fn, DbUtils


# 定义测试类
class TestDepart(unittest.TestCase):
    def setUp(self):
        # 实例化
        self.depart_api = DepartApi()

    # 定义测试用例
    # 登录
    def test01_login_success(self):
        response = self.depart_api.login("13800000002", "123456")
        print(response.json())
        # 获取令牌
        token = "Bearer " + response.json().get("data")
        # 设置请求头,将令牌放入请求头中
        headers = {"Content-Type": "application/json", "Authorization": token}
        app.Header = headers
        # 断言
        assert_fn(self, response, 200, True, 10000, "操作成功")

    # 新增部门
    def test02_add_depart(self):
        response = self.depart_api.add_depart("挖坑1部", "1320", app.Header)
        # 断言
        assert_fn(self, response, 200, True, 10000, "操作成功")
        print(response.json())
        # 连接数据库,获取新增部门id
        with DbUtils("182.92.81.159", "readuser", "iHRM_user_2019", "ihrm") as db:
            sql = "select id from co_department where name = '挖坑1部'"
            db.execute(sql)
            depart_id = db.fetchone()
        app.depart_id = depart_id[0]

    # 查询部门
    def test03_search_depart(self):
        response = self.depart_api.search_depart(app.depart_id, app.Header)
        assert_fn(self, response, 200, True, 10000, "操作成功")
        print(response.json())

    # 修改部门
    def test04_modify_depart(self):
        response = self.depart_api.modify_depart("填坑1部", app.depart_id, app.Header)
        assert_fn(self, response, 200, True, 10000, "操作成功")
        print(response.json())

    # 删除部门
    def test05_delete_depart(self):
        response = self.depart_api.delete_depart(app.depart_id, app.Header)
        assert_fn(self, response, 200, True, 10000, "操作成功")
        print(response.json())
