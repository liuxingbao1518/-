from po.Common_login import Common_login_L

def admin_login(username='admin',password='admin'):
    # 实例化
    obj=Common_login_L()
    obj.open_url()
    # 必须要加上
    obj.driver.implicitly_wait(10)
    obj.ipt_username002(username)
    obj.ipt_password002(password)
    obj.click_button_login002()
    # 最开始实例化时必须传driver
    return obj.driver

if __name__ == '__main__':
    admin_login('admin','admin')