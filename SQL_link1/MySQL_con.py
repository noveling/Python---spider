import pymysql

try:
    db = pymysql.connect(host='localhost', user='root', db='example')
    cur = db.cursor()
    print("连接成功")
    try:
        cur.execute("CREATE TABLE Students(sex varchar(11),name varchar(11))")

    except:
        cur.execute("DROP TABLE Students")

        cur.execute("CREATE TABLE Students(sex varchar(11),name varchar(11))")

except pymysql.Error as e:
    print(e)
    exit(1)



if db:
    if cur:
        cur.close()
    db.close()
    print("关闭sql")

