import unittest
import time
# 报告
from HTMLTestReportCN import HTMLTestRunner
# 工具
from libs.Tool import (
    send_email,
    GetNewReport,
)
# 邮件
from config.Secert import (
    email_host,
    email_account,
    email_to_account,
    email_port,
    email_password
)
"""
# 1.把刚才读写数据库，发送邮件，封装工具类
# 2.把一些配置的数据使用文件来管理
# 3.增加一个登陆的测试需求来进行测试
# 4.unittest discover方式来运行我们的脚本并且发送邮件
"""
def run_test():
    # 找到需要执行的脚本的目录
    dirpath='./scripts'
    # 指定运行脚本的目录以及具体的问题 *_tc.py 代表匹配后面的内容
    discover=unittest.defaultTestLoader.discover(dirpath,pattern='*_tc.py')
    #对当前时间戳进行格式化
    currenttime=time.strftime('%y%m%d%H%M%S')
    #生成测试报告名称,先在当前目录中建一个reports,reports是测试报告路径
    filedir='./reports/'+'report'+currenttime+'.html'
    f=open(filedir,'wb')#文件不能加引号

    # 定义一个runner执行对象
    runner=HTMLTestRunner(stream=f,title='Xsmart自动化测试报告'
                                           ,description='测试报告详细内容'
                                           ,tester='刘兴宝'
                                           ,verbosity=2)
    # 执行脚本
    runner.run(discover)
    f.close()
    # 发送邮件
    a=GetNewReport()
    send_email(user=email_account,password=email_password,host=email_host,to_user=email_to_account,
               port=email_port,subject='添加学生自动化测试报告',body='领导这是今天的工作',
               report=a)
    print('自动化测试报告邮件发送成功')

if __name__ == '__main__':
    run_test()
