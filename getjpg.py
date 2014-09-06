#!/usr/bin/python

import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'<img class=.*? width=.*? height=.*? src="(.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    i = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%d,jpg' % i)
        i = i+1
    
url = raw_input("please input url: ")
html = getHtml(url)
getImg(html)
