# -*- coding: utf-8 -*-
import os
import re
import sys
#设定文件路径
paths = [
    'E:/Other/Comic/',
]
#对目录下的文件进行遍历
for path in paths:
    for category in os.listdir(path):
        #判断是否是文件
        if os.path.isdir(os.path.join(path,category))==True:
            print(category)
            name1 = ''
            name2 = ' [漫之学园资源部]'
            name3 = ''
            #pattern = re.findall(name,category)
            #_category = category.replace(name1,'')
            _category = category.replace(name2,name3)
            print(_category)
            #重命名
            os.rename(os.path.join(path,category),os.path.join(path,_category))
#结束
print ("End")
