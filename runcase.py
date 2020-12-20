# 实现所有的测试用例，都从入口执行，而不是单个执行

import unittest
from HTMLTestRunner import HTMLTestRunner
from setting import TEST_REPORT_PATH,LOGIN_INFO
from api.user_manager import UserManager

if __name__ == '__main__':
    user = UserManager()
    user.login(LOGIN_INFO.get('username'),LOGIN_INFO.get('password'))


    suite = unittest.TestLoader().discover('./cases','test*.py')
    # 创建测试套件
    # 输出路径在setting里写
    with open(TEST_REPORT_PATH,'wb') as f:
        runner = HTMLTestRunner(f,title='测试报告')
        runner.run(suite)
