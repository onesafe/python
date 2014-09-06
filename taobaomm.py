import urllib2
import urllib
import re

mmurl = "http://mm.taobao.com/json/request_top_list.htm?type=0&page="

reg = r'<a href="(.*?.htm)"'
res = re.compile(reg)
reg2 = r'src="(.*?\.jpg)"'
res2 = re.compile(reg2)

for i in range(1,5):
    url = mmurl + str(i)
    try:
        up = urllib2.urlopen(url, timeout=5)
        cont = up.read()
    except:
        continue
    
    mm = re.findall(res, cont)
    for j in mm:
        try:
            imgsrc = urllib2.urlopen(j, timeout=5)
            imghtml = imgsrc.read()
        except:
            continue
        imglist = re.findall(res2, imghtml)
        imglist2 = list(set(imglist))
        imglist2.sort(key=imglist.index)
        for img in imglist2:
            if len(img) > 200:
                continue
            tupian = img.strip()
            tu1 = tupian.split('/')
            tu2 = tu1[len(tu1) - 1]
            filename = "G:\\tu\\" + tu2
            print filename
            try:
                urllib.urlretrieve(tupian, filename)
            except:
                pass
    
    i += 1
