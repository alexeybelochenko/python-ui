import pymysql

conn = pymysql.connect(host='localhost',user='root', password='pythondevelop', db='atom')


a = conn.cursor()

sql = 'SELECT * from `users`;'
countrow =  a.execute(sql)
print(countrow)
