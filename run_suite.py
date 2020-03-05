import unittest
import time
from HTMLTestRunner_PY3 import HTMLTestRunner
from app import absolute_path
from script.test_depart_params import TestDepart
from script.test_emp_params import TestEmployee
from script.test_login import TestLogin

# 方法1 --添加测试用例到测试套件
# 1.创建测试套件
suite = unittest.TestSuite()
# 2.添加测试用例到测试套件
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmployee))
suite.addTest(unittest.makeSuite(TestDepart))
# 3.定义测试报告的路径和名称
filename = absolute_path + '/report/{}.html'.format(time.strftime("%Y%m%d%H%M%S"))
# 4.打开报告，使用HTMLTestRunner_PY3执行测试套件，生成测试报告
with open(filename, "wb") as f:
    runner = HTMLTestRunner(stream=f, verbosity=2, title="IHRM系统接口测试报告")
    # 5.执行测试套件
    runner.run(suite)

# 方法2 --执行script目录下所有测试用例
# suite = unittest.TestLoader().discover(absolute_path + '/script', pattern='test*.py')
# filename = absolute_path + '/report/{}.html'.format(time.strftime("%Y%m%d%H%M%S"))
# # 4.打开报告，使用HTMLTestRunner_PY3执行测试套件，生成测试报告
# with open(filename, "wb") as f:
#     runner = HTMLTestRunner(stream=f, verbosity=2, title="IHRM系统接口测试报告")
#     # 5.执行测试套件
#     runner.run(suite)



