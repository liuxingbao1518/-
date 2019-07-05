import unittest
from libs.Tool import VerifyClass
from po.huiyuanzhongxing.teacher_list.teacher import Add_teacher_center

class TestAddTeacher(VerifyClass):
    def setUp(self):
        self.a=Add_teacher_center()
    def test_addteacher(self):
        result,result1=self.a.apiaddteacher('13699854295', '刘老师', 'liu123', 0, 6, '123', '13699854295@163.com', '13699854295',
                                         '广东省', '深圳市', '龙岗区', '四川省达州市北外悦城怡景', '中华第四帝国创建者')
        self.verify_code(result,200)
        self.verify_html(result1,13699854295)
if __name__ == '__main__':
     unittest.main(verbosity=2)