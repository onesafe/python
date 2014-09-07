import shelve

s = shelve.open('test.dat')
s['baidu'] = 'www.baidu.com'
s['google'] = 'www.google.com'
s['github'] = 'https://github.com'
s['csdn'] = 'www.csdn.com'
s.close()

s = shelve.open('test.dat')
print s

