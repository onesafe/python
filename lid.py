#-*- encoding: utf-8 -*-
import requests
import os
import re

print '本脚本可以帮助您下载某个版块的帖子'+'\n'
boarddic = {}
boarddic['1']='Python'
boarddic['2']='AimGraduate'
boarddic['3']='Job'
boarddic['4']='Linux'
boarddic['5']='Feeling'
print '1 ---> Python'
print '2 ---> AimGraduate'
print '3 ---> Job'
print '4 ---> Linux'
print '5 ---> Feeling'
print 
boardnum = raw_input('请直接输入您所选择查询的版面数字(1-5): ')
board = boarddic[boardnum]
PAGE = int(raw_input('请输入您想下载的页数，一页代表最新的30篇帖子: '))

bourl = "http://bbs.byr.cn/board/" + board +"?p="

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',        
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36' }

if(PAGE>=50):
    PAGE=50

i = 1
while( i<= PAGE):
    bbourl = bourl + str(i)
    print bbourl
    bbocont = requests.get(bbourl, headers=headers).content
    #find title url and name
    res = r'<td\sclass="title_9"><a\shref="(.*?)">(.*?)</a>'
    reg = re.compile(res)
    articletitle = re.findall(reg, bbocont)
    for art in articletitle:
        #print art[0]
        #print art[1]
        articleurl = "http://bbs.byr.cn" + art[0]
        print articleurl
        pathname = 'bbs.byr.cn/' + board + '/' + str(i)
        if os.path.exists(pathname):
            pass
        else:
            os.makedirs(pathname)
        filename = pathname +'/' + art[1].replace('?','').replace('.','')\
        .replace(':', '').replace('<', '').replace('>','').replace('|','')\
        .replace('*','').replace('/','').replace('\\','')+".txt"        

        if os.path.exists(filename):
            continue
        else:
            articlename = open(filename, 'w+')
        articlecontent = requests.get(articleurl, headers=headers).content
        #calculate page num
        regpage = r'<li\sclass="page-pre">.*?<i>(.*?)</i>'
        respage = re.compile(regpage)
        pagedata = re.search(respage, articlecontent)
        pageall = int(pagedata.group(1))
        #print pageall
        yushu = 0
        if (pageall%9) > 0:
            yushu = 1
        page = pageall/9 + yushu
        #print 'page=',page
        j = 1
        while page > 0:
            pageurl = articleurl + '?p=' + str(j)
            #print 'pageurl=',pageurl
            pagecontent = requests.get(pageurl, headers=headers).content
            regname = r'<span\sclass="a-u-name"><a\shref=".*?">(.*?)</a>.*?<div\sclass="a-content-wrap">(.*?)<font\sclass="f000"></font>'
            resname = re.compile(regname)
            namecontent = re.findall(resname,pagecontent)
            for nc in namecontent:           
                tempsrc = nc[1].replace('<br />', '\n').replace('&nbsp;', '  ')
                #remove picture
                resformat = r'<a.*?>.*?</a>'
                tempstr2 = re.sub(resformat, '', tempsrc)
                #remove font
                resformat2 = r'<font.*?>|</font>'
                tempstr3 = re.sub(resformat2, '', tempstr2)
                #remove img
                resformat3 = r'<img.*?/>'
                tempstr4 = re.sub(resformat3, '', tempstr3)
                sepe = '*'*40
                tempstr = sepe + '\n' + tempstr4 +'\n'
                #print tempstr
                articlename.write(tempstr)
            page -= 1
            j += 1
    i += 1
articlename.close()
