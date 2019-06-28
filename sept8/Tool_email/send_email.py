import yagmail

user= 'xingbao021518@163.com'
# 这是你刚刚配置的授权码
pwd = 'lxb1518'
host = 'smtp.163.com'
# https协议端口就是465,964 http 25端口
port = '465'
to_user = 'xiaoxiaohua620@163.com'
to_user2 = '13699854295@163.com'

body = '老板，这是我的自动化测试报告'

# 生成发送对象
send = yagmail.SMTP(user=user,password=pwd,host=host,port=port)
# 发送邮件
# 常规发送方式
# send.send(to=to_user,subject='这是一份测试报告',contents=body)

# 发送给多个人，to变成列表的形式传出去
# send.send(to=[to_user,to_user2],subject='这是一份测试报告',contents=body)

# cc抄送给自己
# send.send(to=[to_user,to_user2],cc=user,subject='这是一份测试报告',contents=body)

# 传送附件
send.send(to=[to_user,to_user2],cc=user,subject='这是一份测试报告',contents=[body,'./代码库.txt'])

print('发送成功')