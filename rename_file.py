import os
import re
import sys
#设定文件路径
paths = [
    #'/Users/developer/Documents/Weekly Playboy/2018/',
    #'/Users/developer/Documents/Weekly Playboy/2016/',
    #'/Users/developer/Documents/FLASH/2018/',
    #'/Users/developer/Documents/FLASH/2017/',
    #'/Users/developer/Documents/FLASH/2016/',
    #'/Users/developer/Documents/FLASH/2015/',
    #'/Users/developer/[FLASH]2018年/',
    #'/Users/developer/[FLASH]2015-2017年/2015/',
    #'/Users/developer/[FLASH]2015-2017年/2016/',
    #'/Users/developer/[FLASH]2015-2017年/2017/',
    #'/Users/developer/Movies/最近我的妹妹有点怪/'
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
