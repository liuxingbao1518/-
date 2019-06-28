from selenium import webdriver
from libs.Tool import create_browser_deiver

edu_url='http://localhost/admin.php'
class Page(object):

    # 生成浏览器驱动
    def __init__(self,driver=''):

        # 判断是否有浏览器启动
        b=driver
        if b=='':
            self.driver=create_browser_deiver()
        else:
            self.driver=b
        self.driver.maximize_window()
        # 全局等待
        self.driver.implicitly_wait(10)

    # 在case中实例化时，都会调用它，导致启动多个浏览器
    # self.driver= create_browser_deiver()

    # def create_driver(self):
    #     driver = webdriver.Chrome()
    #     return driver
    # 打开浏览器
    def open_url(self,url=edu_url):
        # 获取本地文件
        self.driver.get(url)


    # 关闭浏览器
    def close_url(self):
       self.driver.close()