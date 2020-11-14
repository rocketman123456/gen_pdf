#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Zerui Han  hanzr.nju@gmail.com
@Date: 2019-07-15 18:42:40
@LastEditTime: 2019-09-30 10:26:31
@Description: This code can automatically change the filename \\
    of all subtitle files (.ass, .ssa, .srt, .sup or you can \\
    modify it manually) in the folder to the same filename as \\
    the video files (.mkv, .mp4 or others). \\
    Just modify the path to your folder in the last line of code.
'''
import os


def get_file_name(path):
    filetypeList = ['.mkv', '.mp4']  # 视频扩展名
    filenameList = []
    subtypeList = ['.ass', '.ssa', '.srt', '.sup']  # 字幕扩展名
    subtitleList = []
    filelist = os.listdir(path)
    filelist.sort()
    for filename in filelist:
        filetype = os.path.splitext(filename)[1]
        filename = os.path.splitext(filename)[0]
        #print(filename, " ", filetype)
        if filetype in filetypeList:
            filenameList.append(filename)  # 返回mkv mp4文件名（不包含扩展名）
        elif filetype in subtypeList:
            subtitleList.append(filename+filetype)  # 返回字幕文件名（包含扩展名）
    return filenameList, subtitleList


def rename(path, filenameList, subtitleList):
    for i, filename in enumerate(subtitleList):  # 遍历所有字幕文件
        #print(filename)
        subtype = os.path.splitext(filename)[1]
        newName = os.path.join(path, filenameList[i]+subtype)
        oldName = os.path.join(path, filename)
        #print(newName)
        os.rename(oldName, newName)


def main(path=os.getcwd()):  # 若main()函数无输入则path=当前目录
    filename_list, subtitle_list = get_file_name(path)
    #print(filename_list)
    #print(subtitle_list)
    rename(path, filename_list, subtitle_list)


if __name__ == '__main__':
    # 文件夹路径中的斜杠\必须使用反斜杠/或者双斜杠\\代替！
    # 例如 'G:\\anime\\Fate Zero_ 2011_ VCB-Studio'
    # 或   'G:/anime/Fate Zero_ 2011_ VCB-Studio'
    # 或使用r+路径 r'G:\anime\Fate Zero_ 2011_ VCB-Studio'
    main('/Users/developer/Movies/最近我的妹妹有点怪')