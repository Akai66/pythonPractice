#操作文件和目录
import os
def findFileByName(file,name):
    if os.path.isfile(file):
        if os.path.basename(file).find(name) > -1:
            print(file)
    elif os.path.isdir(file):
        for f in os.listdir(file):
            f=os.path.join(file,f)
            findFileByName(f,name)

findFileByName('../','read')
