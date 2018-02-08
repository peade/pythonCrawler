import sqlite3

# '''创建一个数据库，文件名'''
conn = sqlite3.connect('../../sqlite3Data/test.db')
# '''创建游标'''
cur = conn.cursor()

# '''执行语句'''
sql = '''create table if not exists student (id int primary key, name varchar(20), score int, sex varchar(10), age int)'''
cur.execute(sql)
# save the changes
conn.commit()

# students = [(2, 'mark', 80, 'male', 18),
#             (3, 'tom', 78, 'male', 17),
#             (4, 'lucy', 98, 'female', 18),
#             (5, 'jimi', 60, 'male', 16)]
#
# # excute "INSERT"
# cur.execute("INSERT INTO student(id, name, score, sex, age) VALUES (1,'jack',80,'male',18)")
# # excute many
# cur.executemany('INSERT INTO student VALUES (?,?,?,?,?)', students)
# # using the placeholder
# cur.execute("INSERT INTO student VALUES (?,?,?,?,?)", (6, 'kim', 69, 'male', 16))
# conn.commit()
# 查询
# retrieve one record
cur.execute('SELECT * FROM student ORDER BY score DESC')
print('fetchone')
print(cur.fetchone())
print(cur.fetchone())
# retrieve all records as a list
print('fetchall')
cur.execute('SELECT * FROM student ORDER BY score DESC')
print(cur.fetchall())
# terate through the records
rs = cur.execute('SELECT * FROM student ORDER BY score DESC')
print('terate list')
for row in rs:
    print(row)
conn.commit()
# update
updateSql = "update student set name='jerry' where id=2"
cur.execute(updateSql)
conn.commit()
# delete
cur.execute('delete from student where id=5')
conn.commit()
# delte table
# cur.excute('drop table student')
# conn.commit()
# 关闭数据库连接
conn.close()
