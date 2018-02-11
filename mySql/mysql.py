import pymysql

# db = pymysql.connect("localhost", "root", "password", "peade_data")
db = pymysql.connect(host="localhost", user="root", password="password", db="peade_data", port=3306)
cur = db.cursor()
# createTableSql = """create table  if not exists book(
#    id INT NOT NULL AUTO_INCREMENT,
#    title VARCHAR(100) NOT NULL,
#    author VARCHAR(40) NOT NULL,
#    date DATE,
#    PRIMARY KEY ( id )
# )"""
# cur.execute(createTableSql)
# db.commit()

insql01 = "INSERT INTO book(title, author) VALUES ('glory','jack')"
cur.execute(insql01)
db.commit()
sql_update = "update book set title = '%s' where author = '%s'"
cur.execute(sql_update % ("testbook", "jack"))
db.commit()
db.close()
