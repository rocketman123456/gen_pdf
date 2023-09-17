import os
from PIL import Image

img_paths = [
    #'/Users/developer/Downloads/pdf/国王游戏起源 第02回/',
    # '/Users/developer/Downloads/pdf/国王游戏起源 第03回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第04回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第05回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第06回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第07回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第08回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第09回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第10回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第11回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第12回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第13回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第14回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第15回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第16回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第17回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第18回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第19回/',
    '/Users/developer/Downloads/pdf/国王游戏起源 第20回/',
]
ignore = '.DS_Store'

filetypeList = ['.webp']

for img_path in img_paths:
    for img in os.listdir(img_path):
        #print("File name: ", img)
        filename = os.path.splitext(img)[0]
        filetype = os.path.splitext(img)[1]
        if img == ignore:
            continue
        if filetype not in filetypeList:
            continue
        print(img_path + img)
        img = Image.open(img_path + img)
        img.load()
        img.save(img_path + filename + '.png')
        os.remove(img_path + filename + '.webp')
