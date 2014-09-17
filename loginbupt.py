#-*- encoding: utf-8 -*-

from httplib2 import Http
from urllib import urlencode
from optparse import OptionParser
import sys

username='201314xxxx'
password='xxxxxx'
url='http://10.3.8.211/'

def test():
    h = Http()
    resp, content = h.request("http://baidu.com")
    if resp["content-location"] == "http://10.3.8.211":
        return False
    return True

def login(user = None, passwd = None, auth_url = None):
    if user is None or passwd is None or auth_url is None:
        return False
    h = Http()
    data = {"DDDDD":user, "upass":passwd, "save_me":1, "R1":0}
    resp, content = h.request(auth_url, "POST", urlencode(data))
    return test()

def logout(url = "http://10.3.8.211/F.hml"):
    if test():
        h = Http()
        resp, content = h.request(url)

    return not test()

def parse(args_w):
    parser = OptionParser(description='let me take you fly!')
    parser.add_option('-i', '--in', dest='login', action='store_true',default=False, help='login...hi')
    parser.add_option('-o', '--out', dest='logout', action='store_true',default=False, help='logout...bye')
    (options, args) = parser.parse_args(args=args_w)
    if options.login:
        succeed = login(username, password, url)
        if succeed:
            print("Login successfully, Yo Yo")
        else:
            print("Failed to Login, die die")

    if options.logout:
        try:
            succeed = logout()
        except httplib.BadStatusLine,e:
            pass
        if succeed:
            print("Logout successfully, Bye")
        else:
            print("Failedto Logout, yo")


if __name__ == "__main__":
    parse(sys.argv[1:])
    

