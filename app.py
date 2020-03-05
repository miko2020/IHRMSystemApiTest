# app.py文件存放全局变量,公有的配置函数或者类
import logging
import os
from logging import handlers
# 设置项目的绝对路径
absolute_path = os.path.dirname(os.path.abspath(__file__))

# 定义全局变量 --在测试用例中可以调用
Header = None
# 员工id
Emp_id = None
# 部门id
depart_id = None




# 定义一个初始化日志 配置函数:初始化日志的输出路径(控制台/日志文件)
def init_logging():
    # 1.创建日志器
    logger = logging.getLogger()
    # 2.设置日志等级
    logger.setLevel(logging.INFO)
    # 3.创建处理器
    sh = logging.StreamHandler()  # 控制台处理器
    fh = logging.handlers.TimedRotatingFileHandler(absolute_path+"\\log\\ihrm.log",
                                                                    when ='S',
                                                                    interval=10,
                                                                    backupCount=3,
                                                                    encoding='utf-8'
                                                            )
    # 4.设置格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 5.将格式化器添加到处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 6.将处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)


# 只在本文件能执行,引用到其他文件不能被执行
if __name__ == "__main__":
    init_logging()
    logging.info("测试日志会不会打印")