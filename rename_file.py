import os
import re
import sys
#设定文件路径
paths = [
    '/Users/developer/Documents/pdf/'
]

for path in paths:
    for filename in os.listdir(path):
        #判断是否是文件
        if os.path.isfile(os.path.join(path,filename))==True:
            #print(filename)
            #_filename = filename.replace('[Gokukoku-no-Brynhildr]','')
            _filename = filename.replace('[Vol.moe]','')
            print(_filename)
            os.rename(os.path.join(path,filename),os.path.join(path,_filename))
print('End')
