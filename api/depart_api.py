import requests


class DepartApi:
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"
        self.depart_url = "http://182.92.81.159/api/company/department"

    # 登录接口
    def login(self, mobile, password):
        jsonData = {"mobile": mobile, "password": password}
        return requests.post(self.login_url, json=jsonData)

    # 增加部门
    def add_depart(self, name, code, headers):
        jsonData = {
            "name": name,
            "code": code,
            "manager": "咸鱼",
            "introduce": "这是个与众不同的咸鱼",
            "pid": ""
        }
        return requests.post(self.depart_url, json=jsonData, headers=headers)

    # 查询部门
    def search_depart(self, depart_id, headers):
        return requests.get(self.depart_url + "/" + depart_id, headers=headers)

    # 修改部门
    def modify_depart(self, name, depart_id, headers):
        jsonData = {"name": name}
        return requests.put(self.depart_url + "/" + depart_id, json=jsonData, headers=headers)

    # 删除部门
    def delete_depart(self, depart_id, headers):
        return requests.delete(self.depart_url + "/" + depart_id, headers=headers)


