import pymysql

# 建立数据库对象
host = 'localhost'
port=3306
user='root'
password='root'
db='edu'
# 查询语法
select_sql='select * from xsmart_users '
# 建立链接
conn=pymysql.Connect(host=host,port=port,user=user,password=password,db=db,)
# 生成游标
cur=conn.cursor()
# 执行sql语句
cur.execute(select_sql)
# 查询sql结果
d=cur.fetchone()
print(d)




