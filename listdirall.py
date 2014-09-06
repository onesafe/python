import os

def listall(rootpath):
    listdir = os.listdir(rootpath)
    for single in listdir:
        filepath = os.path.join(rootpath, single)
        print filepath
        if os.path.isdir(filepath):
            listall(filepath)

    
listall("c:\Python27\\")

for path, d, filelist in os.walk("c:\Python27\\"):
	for filename in filelist:
		fileout = os.path.join(path,filename)
		print fileout

