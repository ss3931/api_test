from api.base import Base

# 导入Base对象 才能被调用

# 作用: 主要使用关于系统管理员的接口


class UserManager(Base):
    # 传入父类 Base

    def __init__(self):
        self.add_user_path = '/admin/admin/create'
        self.edit_user_path = '/admin/admin/edit'
        self.del_user_path = '/admin/admin/delete'
        self.search_user_path = '/admin/admin/list?page=1&limit=20&sort=add_time&order=desc'

    # 添加管理员
    def add_user(self, username, password, **kwargs):
        """

        :param username: 用户名
        :param password: 密码
        :param kwargs: 可选参数
        :return: 返回请求添加管理员的接口
        """
        user_data = {
            'username': username,
            'password': password,
        }
        if kwargs:
            user_data.update(**kwargs)
        user_url = self.get_url(self.add_user_path)
        return self.post(user_url, user_data)

    # 修改管理员
    def edit_user(self, id, username, **kwargs):
        user_data = {'id': id, 'username': username}
        if kwargs:
            user_data.update(**kwargs)
        user_url = self.get_url(self.edit_user_path)
        return self.post(user_url, user_data)

    # 删除管理员
    def del_user(self, id, **kwargs):
        user_data = {'id': id}
        if kwargs:
            user_data.update(**kwargs)
        user_url = self.get_url(self.del_user_path)
        return self.post(user_url, user_data)

    # 查询管理员
    def search_user(self):
        user_url = self.get_url(self.search_user_path)
        return self.get(user_url)
