import unittest

import requests



# 创建测试类
class TestTpshopLogin(unittest.TestCase):
    session = None


    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取session对象
        cls.session = requests.session()
        # 定义url
        cls.url_code = "http://localhost/index.php?m=Home&c=User&a=verify"
        cls.url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"
    # 关闭session对话
    @classmethod
    def tearDownClass(cls):
        cls.session.close()

     # 登陆成功
    def test01_login_success(self):
        # 请求验证码
        self.session.get(self.url_code)
        # 请求登录
        data = {"username":"15848681858","password":"123456","verify_code":"8888"}
        r = self.session.post(url= self.url_login, data=data)
        # 断言
        self.assertEqual(1, r.json().get("status"))
        print(r.json())

    # 账号不存在
    def test02_user_not_exites(self):
        # 请求验证码
        self.session.get(self.url_code)
        # 请求登录
        data = {"username":"15848681888","password":"123456","verify_code":"8888"}
        r = self.session.post(url=self.url_login, data=data)
        # 断言
        self.assertEqual(-1,r.json().get("status"))
        print(r.json())

    # 密码错误
    def test03_pwd_err(self):
        # 请求验证码
        self.session.get(self.url_code)
        # 请求登录
        data = {"username":"15848681858","password":"1234567","verify_code":"8888"}
        r = self.session.post(url=self.url_login, data=data)
        # 断言
        self.assertEqual(-2,r.json().get("status"))
        print(r.json())

