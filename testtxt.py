# -*- coding: utf-8 -*-
#   -------------------------------------------
#   下载http://www.biquge.la笔趣阁首页上显示的所有小说
#   下载的小说存放在G:\txt文件夹下
#   -------------------------------------------
#   2014/8/23
#   wyp
#   -------------------------------------------


import re
import urllib
import os
import socket

def getHtml(url):
    reg = r'http:\.\.(.*)'
    res = re.compile(reg)
    urlstr = url.replace('/', '.')
    print urlstr
    name = re.findall(res, urlstr)
    urlpathname = r'G:\url' +'\\' + name[0]
    print 'urlpathname = '+urlpathname 
    try:
        socket.setdefaulttimeout(5.0)
        urllib.urlretrieve(url, urlpathname)
    except:
        pass
    print 'getHtml ---------------over'
    return urlpathname

def getBook(html):
    reg = r'<a href="/book/(.*?)/'
    res = re.compile(reg)
    Book = re.findall(res, html)
    return Book

def getName(html):
    reg = r'<h1>(.*?)</h1>'
    res = re.compile(reg)
    name = re.findall(res, html)
    return name

def getZhangJie(html):
    reg = r'<dd><a href="(.*?)">(.*?)</a>'
    res = re.compile(reg)
    zhangJie = re.findall(res, html)
    return zhangJie

def getContent(html):
    reg = r'<div id="content">(.*?)</div>'
    res = re.compile(reg)
    content = re.findall(res, html)
    return content


if __name__ == "__main__":
    url = raw_input("please input url: ")
    urlpathname = getHtml(url)
    print urlpathname
    f1 = open(urlpathname, 'rb+')
    html = f1.read()
    print html
    Book = getBook(html)
    
    #去重保持元素顺序
    book = list(set(Book))
    book.sort(key=Book.index)
    for b in book:
        realurl = url + '/book/' + b + '/'
        print realurl

        realurlname = getHtml(realurl)
        print realurlname
        f2 = open(realurlname, 'rb+')
        realhtml = f2.read()
        BookName = getName(realhtml)

        filepath = os.path.join(r"G:\txt", BookName[0])
        filename = filepath + '.txt'
        print filename

        if os.path.exists(filename):
            continue
        fd = open(filename, 'w+')

        zhangjie = getZhangJie(realhtml)
        for zj in zhangjie:
            sonurl = realurl + zj[0]
            print "url = %s" % sonurl
            try:
                sonurlname = getHtml(sonurl)
                print '-----'+sonurlname
            except:               
                continue

            try:
                f3 = open(sonurlname, 'rb+')
            except IOError:
                continue
            sonhtml = f3.read()
            zhangjieming = getName(sonhtml)
            if len(zhangjieming) == 0:
                continue
                
            fd.write('\t\t\t\t\t' + zhangjieming[0] + '\r\n')
            print "downding  " + zhangjieming[0]
            fd.write('\r\n')
            fd.flush()
            
            try:
                content = getContent(sonhtml)
            except:
                pass
            if len(content) == 0:
                continue
            
            c1 = content[0].replace('<br />', '')
            c2 = c1.replace('&nbsp;', ' ')
            fd.write(c2)
            fd.write('\r\n\r\n\r\n\r\n')
            fd.flush()
        fd.close()
        
        f2.close()
        f3.close()
