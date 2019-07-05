from libs.Tool import BaseHttp

# 创建类进行继承
#继承BaseHttp
class LoginClass(BaseHttp):
    cookies={'PHPSESSID':''}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    # 共享的登录函数
    def apiLogin(self,username,password):
        # 将接口url拆分成了host和url，host封装在tools里
        url = '/admin.php?m=mgr/admin.chklogin&ajax=1'
        # 登录传参
        login_data={
           'username':username,
           'password':password
        }
        reslut=self.http_send(url=url,data=login_data)
        # 获取cookiesbin并传给需要的业务
        pid=reslut.cookies['PHPSESSID']
        # 将pid的值付给前面类变量cookies
        self.cookies['PHPSESSID']=pid
        print(pid)
        return reslut

if __name__ == '__main__':
    run=LoginClass()
    ele=run.apiLogin('admin','admin')
    print(ele.text)
