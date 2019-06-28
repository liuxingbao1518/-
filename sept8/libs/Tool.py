import os
import yagmail
import pymysql
import time
import logging
from selenium import webdriver

# 当前文件路径
cur_path = os.path.dirname(os.path.realpath(__file__))

# log_path是存放日志的路径
log_path = os.path.join(os.path.dirname(cur_path), 'log')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):
    os.mkdir(log_path)

class InsertLog(object):
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter(
            '[%(asctime)s - %(funcName)s line: %(lineno)3d] - %(levelname)s: %(message)s')

    def __console(self, level, message,*args):
        # 创建一个FileHandler，用于写到本地
        #fh = logging.FileHandler(self.logname, 'a')  # 追加模式  这个是python2的
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message,*args):
        self.__console('debug', message,args)

    def info(self, message,*args):
        self.__console('info', message,args)

    def warning(self, message,*args):
        self.__console('warning', message,args)

    def error(self, message,*args):
        self.__console('error', message,args)

# 配置浏览器类型
def create_browser_deiver(b='ch'):
    # 抛出异常
    try:
        if b=='ch':
            driver=webdriver.Chrome()
        elif b=='ie':
            driver=webdriver.ie
        elif b=='ff':
            driver=webdriver.firefox
        else:
            pass
        return driver
    # 基本异常
    except BaseException:
        pass
# 数据库的操作
def read_mysql_data(host,port,user,password,db,sql):
    """
    :param host:本地服务
    :param port:
    :param user:
    :param password:
    :param db: 数据库名称
    :param sql:
    :return:
    """
    # 建立链接
    conn = pymysql.Connect(host=host, port=port, user=user, password=password, db=db, )
    # 生成游标
    cur = conn.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 关闭游标
    cur.close()
    # 关闭数据库
    conn.close()
    # 查询sql结果
    d = cur.fetchone()
    return d
# 发送邮件
def send_email(user,password,port,body,subject,report,to_user,host='smtp.163.com'):
    """

    :param user:发送者
    :param password:授权码
    :param port:端口默认为3306
    :param body:主题
    :param subject:标题
    :param report:报告
    :param to_user:接受者账号，默认是字符串，如果传多个请用列表的方式传递
    :param host:邮箱服务
    :return:
    """
    # 生成发送对象
    send = yagmail.SMTP(user=user, password=password, host=host, port=port)
    if type(to_user) is list:
        send.send(to=to_user, cc=user, subject=subject, contents=[body, report])
        flag = '发送给批量用户成功'
    elif type(to_user) is str:
        send.send(to=to_user, cc=user, subject=subject, contents=[body, report])
        flag = '发送个人用户成功'

    else:
        flag = '发送数据错误'
    return flag

FD = "./reports"
# 获取最新的测试报告
def GetNewReport(FileDir=FD):
    # 打印目录所在所有文件名（列表对象）
    l = os.listdir(FileDir)
    # 按时间排序
    l.sort(key=lambda fn: os.path.getmtime(FileDir + "\\" + fn))
    # 获取最新的文件保存到file_new
    f = os.path.join(FileDir, l[-1])
    return f
if __name__ == '__main__':
    pass