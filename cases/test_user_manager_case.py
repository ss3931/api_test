import unittest
from api.user_manager import UserManager


class TestUserManagerCase(unittest.TestCase):

    user_id = None
    # 根据case1 返回的结果的id 赋值给user_id user_id 是类变量

    # 初始化方法,初始化之后才能调用
    # 需要加一个装饰器，才能调用unnitest
    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManager() #丢了括号会报错就不是一个类了
        # cls.user.login( 'admin123', 'admin123') 登录写在了runcase里

        cls.username = cls.password = 'test020'
        cls.new_username = cls.new_password = 'xxx010'
    # case1:只输入用户名和密码进行添加管理员
    def test01_normal_add(self):
        # 定义测试用例数据
        # username = 'test018'
        # password = 'test018'

        # 对接口的返回的结果进行校验

        # 1 ) 请求添加管理员接口
        actual_result = self.user.add_user(self.username, self.password)
        print(actual_result)
        data = actual_result.get('data')
        if data:
            TestUserManagerCase.user_id = data.get('id')
            # 赋值结果给类变量
            # 只有data里面有值，我们会赋值给这个类变量，如果没有就不赋值，否则会报错

        # 2 ) 对返回结果数据校验

        self.assertEqual(0, actual_result['errno'])
        self.assertEqual(self.username,actual_result.get('data').get('username'))

    # case2:编辑用户
    def test02_edit(self):
        # new_user_name = 'xxxx007'
        # new_user_password = 'xxxx007'
        actual_result = self.user.edit_user(TestUserManagerCase.user_id, self.new_username, password = self.new_password)
        self.assertEqual(0, actual_result['errno'])
        self.assertEqual(self.new_username, actual_result['data']['username'])

    # case3:查询用户
    def test03_search(self):

        actual_result = self.user.search_user()
        self.assertEqual(0, actual_result['errno'])
        self.assertEqual(self.new_username,actual_result.get('data').get('list')[0].get('username'))

    # case4:删除用户
    def test04_delete(self):
        # 根据id来进行删除用户  也可以定义类变量 在下面的任何方法都可以使用

        # 1 ) 定义测试用例中的数据

        # 2 ） 调用被测接口
        actual_result = self.user.del_user(TestUserManagerCase.user_id)
        # 3 ） 断言
        self.assertEqual(0, actual_result['errno'])


if __name__ == '__main__':
    unittest.main()
