import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='beiyouren',port=3306, charset='utf8')
    cur = conn.cursor()
    conn.select_db('pythonDB')
    count = cur.execute('select * from userinfo')
    print 'there has %d rows record' % count

    print '===='*10
    result = cur.fetchone()
    print result
    print 'ID:%d\tusername:%s\tage:%d\tgender:%s' % result 

    print '===='*10
    result = cur.fetchmany(6)
    for r in result:
        print r

    print '===='*10

    cur.scroll(0, mode='absolute')
    results = cur.fetchall()
    for r in results:
	print r

    conn.commit()
    cur.close()
    conn.close()

except MySQLdb.Error, e:
    print "Mysql Error %d:%s" % (e.args[0], e.args[1])
    
