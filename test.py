import pymysql

db = pymysql.connect(host="localhost", user="root",password="sasa", db="test", port=3306)
cur = db.cursor()
sql = "select * from user"
try:
	cur.execute(sql)#执行sql语句  

	results = cur.fetchall()#获取查询的所有记录  
	print("id","name","password")
	#遍历结果  
	for row in results :
		id = row[0]
		name = row[1]
		password = row[2]
		print(id,name,password)
except Exception as e:
	raise e
finally:
	db.close()#关闭连接  

import pymysql
#2.插入操作  
db= pymysql.connect(host="localhost",user="root",
	password="sasa",db="test",port=3306)

# 使用cursor()方法获取操作游标  
cur = db.cursor()

sql_insert ="""insert into user(id,username,password) values(4,'liu','1234')"""

try:
	cur.execute(sql_insert)
	#提交  
	db.commit()
except Exception as e:
	#错误回滚  
	db.rollback()
finally:
	db.close()

import pymysql
#3.更新操作  
db= pymysql.connect(host="localhost",user="root",
	password="sasa",db="test",port=3306)

# 使用cursor()方法获取操作游标  
cur = db.cursor()

sql_update ="update user set username = '%s' where id = %d"

try:
	cur.execute(sql_update % ("xiongda",3))#像sql语句传递参数  
	#提交  
	db.commit()
except Exception as e:
	#错误回滚  
	db.rollback()
finally:
	db.close()
import pymysql
#4.删除操作  
db= pymysql.connect(host="localhost",user="root",
	password="sasa",db="test",port=3306)

# 使用cursor()方法获取操作游标  
cur = db.cursor()

sql_delete ="delete from user where id = %d"

try:
	cur.execute(sql_delete % (3))#像sql语句传递参数  
	#提交  
	db.commit()
except Exception as e:
	#错误回滚  
	db.rollback()
finally:
	db.close()
