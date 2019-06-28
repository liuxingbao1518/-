import time
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from po.Common_open_url import Page


# 添加学生类
class AddStudentPage(Page):
    # 对象层(定位元素)
    # 点击学生列表
    click_student_list001 = (By.LINK_TEXT, '学生列表')
    # 切换进入表单
    change_frame = (By.ID, 'mainframe')
    # 点击添加学生
    click_add_student001 = (By.XPATH, '/html/body/div[2]/h3/a[2]/span')
    # 进入页面操作,输入用户账号
    user_name = (By.ID, 'username')
    # 输入称呼
    chenghu = (By.NAME, 'realname')
    # 输入密码
    user_psw = (By.NAME, 'password')
    # 选择性别
    click_sex = (By.XPATH, '//*[@id="form"]/div/div[4]/div/label[3]')
    # 选择角色
    select_jiaose = (By.NAME, 'roleid')
    # 选择明星学员
    click_Star_Student = (By.NAME, 'isstart')
    # 点击上传图片
    sctp = (By.XPATH, '//*[@id="form"]/div/div[7]/div/a/span')
    # 选择本地图片
    benditupain = (By.XPATH, '/html/body/div[3]/div[1]/div[2]/div/div[1]/ul/li[2]')
    # 预览
    preview = (By.XPATH, '/html/body/div[3]/div[1]/div[2]/div/div[3]/form/div/div')
    # 点击确定
    Click_OK = (By.XPATH, '/html/body/div[3]/div[1]/div[3]/span[1]/input')
    # 学员类型
    Types_of_trainees = (By.ID, 'startname')
    # driver.find_element_by_id('startname').send_keys('华为')
    # 学习时间
    learning_time = (By.ID, 'studytime')
    # 报名课程数
    Enrollment_Course = (By.NAME, 'studynum')
    # 选择机构
    Selection_mechanism = (By.ID, 'oneCategory')
    # 选择邮箱
    Selection_email = (By.ID, 'email')
    # 选择手机
    Selection_Phone = (By.ID, 'phone')
    # 省份
    province = (By.NAME, 'location_p')
    # 市
    city = (By.NAME, 'location_c')
    # 区
    area = (By.NAME, 'location_a')
    # 输入详细地址
    Address = (By.ID, 'address')
    # 个人简历
    Curriculum_vitae = (By.ID, 'introduce')
    # 保存
    save = (By.ID, 'btn_sub')
    # 验证是否成功(定位坐标)
    verify_success = (By.XPATH, '/html/body/div[2]/h3/a/span')
    # 返回值
    return_value = (By.XPATH, '//*[@id="recordList"]/tr[1]/td[6]')

    # 操作层(对元素进行操作)
    # 点击学生列表
    def click_student_list002(self):
        self.driver.find_element(*self.click_student_list001).click()

    # 切换进入表单
    def change_frame002(self):
        a = self.driver.find_element(*self.change_frame)
        self.driver.switch_to.frame(a)

    # 点击添加学生
    def click_add_student002(self):
        self.driver.find_element(*self.click_add_student001).click()

    # 进入页面操作,输入用户账号
    def user_name002(self, value):
        self.driver.find_element(*self.user_name).send_keys(value)

    # 输入称呼
    def chenghu002(self, value):
        self.driver.find_element(*self.chenghu).send_keys(value)

    # 输入密码
    def password002(self, value):
        self.driver.find_element(*self.user_psw).send_keys(value)

    # 选择性别
    def click_sex002(self):
        self.driver.find_element(*self.click_sex).click()

    # 选择角色
    def click_jiaose002(self):
        a = self.driver.find_element(*self.select_jiaose)
        Select(a).select_by_value('8')

    # 选择明星学员
    def click_Star_Student002(self):
        self.driver.find_element(*self.click_Star_Student).click()

    # 点击上传图片
    def sctp002(self):
        self.driver.find_element(*self.sctp).click()

    # 选择本地图片
    def benditupian002(self):
        self.driver.find_element(*self.benditupain).click()

    # 预览
    def preview002(self):
        self.driver.find_element(*self.preview).click()
        time.sleep(2)
        os.system('C:/Users/Administrator/Desktop/liuxingbao/自动化安装包文件/uploadFile.exe')
        time.sleep(3)

    # 点击确定
    def click_ok002(self):
        self.driver.find_element(*self.Click_OK).click()

    # 学员类型
    def types_of_trainees002(self, value):
        self.driver.find_element(*self.Types_of_trainees).send_keys(value)

    # 学习时间
    def learning_time002(self, value):
        self.driver.find_element(*self.learning_time).send_keys(value)

    # 报名课程数
    def enrollment_Course002(self, value):
        self.driver.find_element(*self.Enrollment_Course).send_keys(value)

    # 选择机构
    def selection_mechanism002(self):
        a = self.driver.find_element(*self.Selection_mechanism)
        Select(a).select_by_visible_text('北京科技大学')

    # 选择邮箱
    def selection_email002(self, value):
        self.driver.find_element(*self.Selection_email).send_keys(value)

    # 选择手机
    def selection_phone002(self, value):
        self.driver.find_element(*self.Selection_Phone).send_keys(value)

    # 选择省份
    def province002(self):
        a = self.driver.find_element(*self.province)
        Select(a).select_by_value('四川省')

    # 选择市
    def city002(self):
        b = self.driver.find_element(*self.city)
        Select(b).select_by_visible_text('达州市')

    # 选择区
    def area002(self):
        c = self.driver.find_element(*self.area)
        Select(c).select_by_index('1')

    # 输入详细地址
    def address002(self, value):
        self.driver.find_element(*self.Address).send_keys(value)

    # 个人简历
    def curriculum_vitae002(self, value):
        self.driver.find_element(*self.Curriculum_vitae).send_keys(value)

    def save002(self):
        self.driver.find_element(*self.save).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)

    # 点击返回列表(定位坐标)
    def verify_success002(self):
        self.driver.find_element(*self.verify_success).click()

    # 返回值
    def return_value002(self):
        resutl = self.driver.find_element(*self.return_value).text
        return resutl

    # 业务层(对操作层进行拼接)
    def add_student(self, username, realname, password, startname, studytime, studynum, email, phone, address,
                    introduce):
        self.click_student_list002()
        self.change_frame002()
        self.click_add_student002()
        self.user_name002(username)
        self.chenghu002(realname)
        self.password002(password)
        self.click_sex002()
        self.click_jiaose002()
        self.click_Star_Student002()
        self.sctp002()
        self.benditupian002()
        self.preview002()
        self.click_ok002()
        self.types_of_trainees002(startname)
        self.learning_time002(studytime)
        self.enrollment_Course002(studynum)
        self.selection_mechanism002()
        self.selection_email002(email)
        self.selection_phone002(phone)
        self.province002()
        self.city002()
        self.area002()
        self.address002(address)
        self.curriculum_vitae002(introduce)
        self.save002()
        self.verify_success002()
        self.return_value002()


if __name__ == '__main__':
    pass
