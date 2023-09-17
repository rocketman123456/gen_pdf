import os
import re
import numpy as np
import shutil
#-----------------------------------------------------------------
paths = [
    'E:/Other/Cartoon/',
    #'/Volumes/TOURO/Comic/201712/',

    #'/Volumes/TOURO/Comic/201801/',
    #'/Volumes/TOURO/Comic/201802/',
    #'/Volumes/TOURO/Comic/201803/',
    #'/Volumes/TOURO/Comic/201804/',
    #'/Volumes/TOURO/Comic/201805/',
    #'/Volumes/TOURO/Comic/201806/',
    #'/Volumes/TOURO/Comic/201807/',
    #'/Volumes/TOURO/Comic/201808/',
    #'/Volumes/TOURO/Comic/201809/',
    #'/Volumes/TOURO/Comic/201810/',
    #'/Volumes/TOURO/Comic/201811/',
    #'/Volumes/TOURO/Comic/201812/',

    #'/Volumes/TOURO/Comic/201901/',
    #'/Volumes/TOURO/Comic/201902/',
    #'/Volumes/TOURO/Comic/201903/',
    #'/Volumes/TOURO/Comic/201904/',
    #'/Volumes/TOURO/Comic/201905/',
    #'/Volumes/TOURO/Comic/201906/',
    #'/Volumes/TOURO/Comic/201907/',
    #'/Volumes/TOURO/Comic/201908/',
    #'/Volumes/TOURO/Comic/201909/',
    #'/Volumes/TOURO/Comic/201910/',
    #'/Volumes/TOURO/Comic/201911/',
    #'/Volumes/TOURO/Comic/201912/',

    #'/Volumes/TOURO/Comic/202001/',
    ##'/Volumes/TOURO/Comic/202002/',
    #'/Volumes/TOURO/Comic/202003/',
    #'/Volumes/TOURO/Comic/202004/',
    #'/Volumes/TOURO/Comic/202005/',
    #'/Volumes/TOURO/Comic/202006/',
    #'/Volumes/TOURO/Comic/202007/',
    #'/Volumes/TOURO/Comic/202008/',
    #'/Volumes/TOURO/Comic/202009/',
    #'/Volumes/TOURO/Comic/202010/',
]
#-----------------------------------------------------------------
# match [author]
pattern = r'^\[.+?\]'
#-----------------------------------------------------------------
# store key-value
path_data = {}
name_data = {}
#-----------------------------------------------------------------
for path in paths:
    for folder in os.listdir(path):
        if os.path.isdir(os.path.join(path, folder)):
            result = re.match(pattern=pattern, string=folder)
            if result != None :
                author = result.group()
                if(author not in path_data):
                    path_data[author] = []
                if(folder not in path_data):
                    name_data[folder] = []
                path_data[author].append(os.path.join(path, folder))
                name_data[folder].append(os.path.join(path, folder))
            else:
                print(folder)
#-----------------------------------------------------------------
np.save('comic_path.npy', path_data)
np.save('comic_name.npy', name_data)
restored_path = np.load('comic_path.npy', allow_pickle=True).item()
restored_name = np.load('comic_name.npy', allow_pickle=True).item()
sort_path = 'E:/Other/Cartoon/sorted/'
#-----------------------------------------------------------------
for author in restored_path:
    new_author_path = os.path.join(sort_path, author)
    #print(new_author_path)
    isExists = os.path.exists(new_author_path)
    if not isExists:
        os.makedirs(new_author_path)
    comic_name_path = {}
    for comic in restored_path[author]:
        old_comic_path = comic
        new_comic_path = old_comic_path.replace(author + ' ','')
        #move_comic_path = os.path.join(new_author_path, author) 
        print(old_comic_path)
        print(new_comic_path)
        print(new_author_path)
        os.rename(os.path.join(path,old_comic_path),os.path.join(path,new_comic_path))
        shutil.move(new_comic_path, new_author_path)
#-----------------------------------------------------------------
print('End')
