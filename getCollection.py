#-*- coding: utf-8 -*-
import os
import shutil
path = "/root/tmp/a"
target = "/root/tmp/result.txt"
print target
appendfile = open(target, 'a+')

for roots, dirs, files in os.walk(path):
    for ifile in files:
	tempfile = roots + '/' + ifile
	openfile = open(tempfile)
	print tempfile
	shutil.copyfileobj(openfile, appendfile)
	openfile.close()

appendfile.close()

