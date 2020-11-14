# -*- coding: utf-8 -*-
import os
import re
import sys
#设定文件路径
paths = [
    #'/Volumes/DATA/Download/(無修正+有修正) 高清动画 第2弹 [漫之学园资源部]',
    #'/Volumes/DATA/Download/(無修正+有修正) 高清动画 第4弹 [漫之学园资源部]',
    #'/Volumes/DATA/Download/(無修正+有修正) 高清动画 第5弹 [漫之学园资源部]',
    #'/Volumes/DATA/Download/(無修正+有修正) 高清动画 第6弹 [漫之学园资源部]',
    #'/Volumes/DATA/Download/(無修正+有修正) 高清动画 第7弹 [漫之学园资源部]',
    #'/Volumes/DATA/Download/(無修正+有修正) 高清动画 第8弹 [漫之学园资源部]',
    #'/Volumes/DATA/Download/(無修正+有修正) 高清动画 第11弹 [漫之学园资源部]',
    '/Volumes/DATA/Cartoon/(無修正+有修正) 高清动画 第2弹 [漫之学园资源部]',
    '/Volumes/DATA/Cartoon/(無修正+有修正) 高清动画 第4弹 [漫之学园资源部]',
    '/Volumes/DATA/Cartoon/(無修正+有修正) 高清动画 第9弹 [漫之学园资源部]',
    '/Volumes/DATA/Cartoon/(無修正+有修正) 高清动画 第10弹 [漫之学园资源部]',
    '/Volumes/DATA/Cartoon/(無修正+有修正) 高清动画 第12弹 [漫之学园资源部]',
    '/Volumes/DATA/Cartoon/(無修正+有修正) 高清动画 第13弹 [漫之学园资源部]',
    '/Volumes/DATA/Cartoon/(無修正+有修正) 高清动画 第14弹 [漫之学园资源部]',
]
#对目录下的文件进行遍历
for path in paths:
    for category in os.listdir(path):
        #判断是否是文件
        if os.path.isdir(os.path.join(path,category))==True:
            print(category)
            name1 = '[BanYuner.net整理发布]'
            name2 = '(15禁アニメ) '
            name3 = ''
            #pattern = re.findall(name,category)
            #_category = category.replace(name1,'')
            _category = category.replace(name2,name3)
            print(_category)
            #重命名
            os.rename(os.path.join(path,category),os.path.join(path,_category))
#结束
print ("End")
