import requests


class EmployeeApi:
    def __init__(self):
        pass

    # 登录接口
    def login(self, mobile, password):
        login_url = "http://182.92.81.159/api/sys/login"
        jsonData = {"mobile": mobile, "password": password}
        return requests.post(login_url, json=jsonData)

    # 新增员工
    def add_emp(self, username, mobile, headers):
        add_emp_url = "http://182.92.81.159/api/sys/user"
        jsonData = {"username": username,
                    "mobile": mobile,
                    "timeOfEntry": "2020-02-01",
                    "formOfEmployment": 1,
                    "departmentName": "酱油2部",
                    "departmentId": "1205026005332635648",
                    "correctionTime": "2020-02-03T16:00:00.000Z"}
        return requests.post(add_emp_url, json=jsonData, headers=headers)

    # 查询员工
    def search_emp(self, emp_id, headers):
        search_emp_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        return requests.get(search_emp_url, headers=headers)

    # 修改员工
    def modify_emp(self, emp_id, username, headers):
        modify_emp_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        jsonData = {"username": username}
        return requests.put(modify_emp_url, json=jsonData, headers=headers)

    # 删除员工
    def delete_emp(self, emp_id, headers):
        delete_emp_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        return requests.delete(delete_emp_url, headers=headers)