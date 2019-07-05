import json
from libs.Base_work import LoginClass


class Add_teacher_center(LoginClass):
    def apiaddteacher(self,username,realname,password,sex,roleid,orid1,email,phone,
                      location_p,location_c,location_a,address,introduce,type=1):
        add_teacher_url='/admin.php?m=mgr/member2.saveMemberInfo&id='
        add_teacher_data={
            'username':username,
            'realname':realname,
            'password':password,
            'sex':sex,
            'roleid':roleid,
            'orid1':orid1,
            'email':email,
            'phone':phone,
            'location_p':location_p,
            'location_c':location_c,
            'location_a':location_a,
            'address':address,
            'introduce':introduce
        }
        # 实例化登录
        run=LoginClass()
        run.apiLogin('admin','admin')
        # 添加教师接口请求
        result=self.http_send(url=add_teacher_url,data=add_teacher_data,cookies=self.cookies)
        # 校验是否添加成功
        veriy_add_teacher_url='/admin.php?m=mgr/member2.memberlist&type=1'
        result1=self.http_send(url=veriy_add_teacher_url,method='get',cookies=self.cookies)
        return result,result1



if __name__ == '__main__':
    run = Add_teacher_center()
    result, result1 = run.apiaddteacher('13430120569', 'Angle', '123456', 0, 5, '123', '131666@163.com', '13430120565',
                                         '广东省', '深圳市', '龙岗区', '这是详细地址', '这是个人简介信息')
    print(result.status_code)
    data=result.json()
    print(data.post('info'))
    print(result1.text)
