import pymysql

# import mysql.connector

# conn = mysql.connector.connect(host='sdri_db_3306', port=3306, user='summer', password='123456', database='sdri',charset='utf8')
conn = pymysql.connect(
    host='sdri_db_3306',
    port=3306,
    user='root',
    password='root',
    db='sdri',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = conn.cursor()
sql = "SELECT email FROM user"
cursor.execute(sql)
# for row in cursor.fetchall():
# print (row[0])
print('共查找出', cursor.rowcount, '条数据')
