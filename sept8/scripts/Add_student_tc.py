import time
import unittest
from libs.Base_work import admin_login
from selenium import webdriver
from po.Common_open_url import Page
# from po.Common_login import Common_login_L
from po.huiyuanzhongxing.click_number_center import Click_number_center
from po.huiyuanzhongxing.student_list.add_student_list import AddStudentPage

# 测试类
class TestEdu(unittest.TestCase):
    def setUp(self):
        # 实例化Page获取驱动
        # 首次实例化父类的Driver在Admin login
        self.driver=admin_login()
        # 实例化会员中心 #self.driver是最开始实例化时开始传参
        self.hy = Click_number_center(self.driver)
        # 实例化添加学生
        self.xs = AddStudentPage(self.driver)

    def tearDown(self):
        self.xs.close_url()
    # 测试步骤
    def add_student_lc(self):
        # # 打开浏览器
        # self.obj.open_url()
        # # 登录
        # self.dl.login_system('admin','admin')
        # # 点击会员中心
        self.hy.create_run_center()
        # 添加学生
        self.xs.add_student('15013444227','刘星雨','liu12345','优秀学生','2019-6-18','汉语',
                            '15013444227@163.com', '15013444227','四川省达州市北外悦城怡景','高才生')

        # 校验学生
        result = self.xs.return_value002()
        return result

    def test_add_student_success(self):
        result = self.add_student_lc()
        self.assertAlmostEqual(result, '15013444227')

if __name__ == '__main__':
    unittest.main(verbosity=2)
# verbosity
# 0:代表只显示结果
# 1:默认值 .. .f之类
# 2.显示详细的用例执行信息
