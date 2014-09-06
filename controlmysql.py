import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost', user='root', passwd='beiyouren', db='pythonDB', port=3306)
    cur = conn.cursor()

    sqlstr = "insert into userinfo(username, age, gender) values(%s,%s,%s)"
    str = raw_input("please input username,age,gender: ")
    infolist = str.split(',')
    
    cur.execute(sqlstr, (infolist[0], infolist[1], infolist[2]))
    
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb,e:
    print "Mysql Error "
