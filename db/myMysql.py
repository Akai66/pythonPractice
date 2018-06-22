import mysql.connector
conn=mysql.connector.connect(user='root',password='helloworld',database='adver')
# cursor=conn.cursor()
#建表
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
# print(cursor.rowcount)
# conn.commit()
# cursor.close()

#查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
datas=cursor.fetchall()
print(datas)
cursor.close()
conn.close()

