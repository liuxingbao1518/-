from libs.Tool import InsertLog
from po.Common_open_url import Page
from po.Common_login import Common_login_L
from selenium.webdriver.common.by import By



class Click_number_center(Page):
    # 对象层
    click_on_number_center=(By.XPATH,'//*[@id="header"]/ul/li[3]/a')
    # 操作层
    def create_run_center(self):
        # 点击会员中心
        self.driver.find_element(*self.click_on_number_center).click()
    # 业务层
    def click_on_the_Membership_Center(self):
       try:
            self.create_run_center()
       except BaseException as abc:
           daily=InsertLog()
           daily.error('找不到会员中心',abc)
           self.driver.get_screenshot_as_file('找不到截图')

if __name__ == '__main__':
    obj = Page()
    obj.open_url()
    lp = Common_login_L(obj.driver)
    lp.login_system('admin','admin')
    run=Click_number_center(obj.driver)
    run.click_on_the_Membership_Center()


