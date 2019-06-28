from time import sleep
from po.Common_open_url import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

class Common_login_L(Page):

    # 对象层
    ipt_username=(By.ID,'username')
    ipt_password=(By.ID,'password')
    click_button_login=(By.XPATH,'//*[@id="loginFrm"]/input')
    yz_login_success=(By.XPATH,'//*[@id="header"]/p/span[1]')
    ipt_username_error=(By.ID,'username_msg')
    ipt_password_error=(By.ID,'password_msg')
    # 操作层
    # 登录
    def ipt_username002(self,username):
        self.driver.find_element(*self.ipt_username).send_keys(username)

    def ipt_password002(self,password):
        self.driver.find_element(*self.ipt_password).send_keys(password)

    def click_button_login002(self):
        self.driver.find_element(*self.click_button_login).click()
    # 验证登录成功
    def get_success_yz(self):
        rustle=self.driver.find_element(*self.yz_login_success).text
        return rustle
    # 用户名为空
    def get_username_error(self):
        WebDriverWait(self.driver,10,0.5).until(ES.text_to_be_present_in_element(self.ipt_username_error,u'帐号或密码不能为空'))
        rustle=self.driver.find_element(*self.ipt_username_error).text
        return rustle

    # 用密码错误
    def get_password_error(self):
        WebDriverWait(self.driver, 10,0.5).until(ES.text_to_be_present_in_element(self.ipt_password_error, u'密码错误'))
        rustle = self.driver.find_element(*self.ipt_password_error).text
        return rustle

    # 业务层
    def login_system(self,username,password):
        self.ipt_username002(username)
        self.ipt_password002(password)
        self.click_button_login002()
    # def verify_login_succecc(self,driver):
    #     pass
if __name__ == '__main__':
    run=Common_login_L()
    run.login_system('admin','admin')
