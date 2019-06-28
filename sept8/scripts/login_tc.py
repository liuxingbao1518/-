import time
import unittest
import sys
from libs.Base_work import admin_login
from po.Common_login import Common_login_L
from po.huiyuanzhongxing.click_number_center import Click_number_center
from po.huiyuanzhongxing.student_list.add_student_list import AddStudentPage

class loginTest(unittest.TestCase):

    def setUp(self):
        self.obj=Common_login_L()
        self.obj.open_url()

    def tearDown(self):
        self.obj.close_url()

    # 测试用例
    # 登录成功
    def test_login_success_001(self):
        # 登录业务层
        self.obj.login_system('admin','admin')
        r=self.obj.get_success_yz()
        self.assertEqual(r,'欢迎回来：admin',)
    # 用户名为空
    def test_login_error_001(self):
        self.obj.login_system('','admin')
        time.sleep(5)
        r=self.obj.get_username_error()
        self.assertEqual(r,'帐号或密码不能为空')
    # 密码错误
    def test_password_error_001(self):
        self.obj.login_system('admin','admin12')
        time.sleep(5)
        r=self.obj.get_password_error()
        self.assertEqual(r,'密码错误')

    # 密码为空
    #