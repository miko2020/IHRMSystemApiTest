# 自定义工具类
import json
import os

import pymysql


# 定义断言函数
def assert_fn(self, response, status_code, success,  code, msg):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(msg, response.json().get("message"))


# 数据库
class DbUtils:
    # 实例化对象时,自动执行
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # 使用with语法,进入函数时会先运行enter语句
    def __enter__(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database)
        self.cursor = self.conn.cursor()
        return self.cursor

    # 退出with语句时,会执行exit语句
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


# 员工增删改查--参数化
# 读取添加员工的数据
def read_add_emp(filename):
    with open(filename, encoding="utf8") as f:
        jsonData = json.load(f)
        result_list = list()
        # add_emp_data = jsonData.get("add_emp")
        # username = add_emp_data.get("username")
        # mobile = add_emp_data.get("mobile")
        # status_code = add_emp_data.get("status_code")
        # success = add_emp_data.get("success")
        # code = add_emp_data.get("code")
        # message = add_emp_data.get("message")
        # result_list.append((username, mobile, status_code, success, code, message))
        add_emp_data = jsonData.get("add_emp")  # type dict
        result_list.append(tuple(add_emp_data.values()))   # 获取字典所有value值,放入tuple里,添加到列表中
    return result_list


# 读取查询员工的数据
def read_search_emp(filename):
    with open(filename, encoding="utf8") as f:
        jsonData = json.load(f)
        result_list = list()
        search_emp_data = jsonData.get("search_emp")
        result_list.append(tuple(search_emp_data.values()))
    return result_list


# 读取修改员工的数据
def read_modify_emp(filename):
    with open(filename, encoding="utf8") as f:
        jsonData = json.load(f)
        result_list = list()
        search_emp_data = jsonData.get("modify_emp")
        result_list.append(tuple(search_emp_data.values()))
    return result_list


# 读取删除员工的数据
def read_delete_emp(filename):
    with open(filename, encoding="utf8") as f:
        jsonData = json.load(f)
        result_list = list()
        delete_emp_data = jsonData.get("delete_emp")
        result_list.append(tuple(delete_emp_data.values()))
    return result_list


# 登录参数化
def get_login_data(filename):
    with open(filename, encoding="utf8") as f:
        jsonData = json.load(f)
        result_list = list()
        for data in jsonData.values():
            result_list.append(tuple(data.values()))
    return result_list


# 读取部门数据--参数化
def get_add_depart_data(filename):
    with open(filename, encoding="utf8") as f:
        jsonData = json.load(f)
        result_list = list()
        add_depart_data = jsonData.get("add_depart")
        result_list.append(tuple(add_depart_data.values()))
    return result_list


def get_search_depart_data(filename):
    with open(filename, encoding="utf8") as f:
        jsonData = json.load(f)
        result_list = list()
        add_depart_data = jsonData.get("search_depart")
        result_list.append(tuple(add_depart_data.values()))
    return result_list


def get_modify_depart_data(filename):
    with open(filename, encoding="utf8") as f:
        jsonData = json.load(f)
        result_list = list()
        add_depart_data = jsonData.get("modify_depart")
        result_list.append(tuple(add_depart_data.values()))
    return result_list


def get_delete_depart_data(filename):
    with open(filename, encoding="utf8") as f:
        jsonData = json.load(f)
        result_list = list()
        add_depart_data = jsonData.get("delete_depart")
        result_list.append(tuple(add_depart_data.values()))
    return result_list




# 只在本文件调试用
if __name__ == '__main__':
    filename = os.path.dirname(os.path.abspath(__file__)) + "/data/depart.json"
    print(get_delete_depart_data(filename))








