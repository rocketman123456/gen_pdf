import os
import re
import numpy as np
import shutil
#-----------------------------------------------------------------
paths = [
    '/Volumes/TOURO/Comic/201711/',
    '/Volumes/TOURO/Comic/201712/',

    '/Volumes/TOURO/Comic/201801/',
    '/Volumes/TOURO/Comic/201802/',
    '/Volumes/TOURO/Comic/201803/',
    '/Volumes/TOURO/Comic/201804/',
    '/Volumes/TOURO/Comic/201805/',
    '/Volumes/TOURO/Comic/201806/',
    '/Volumes/TOURO/Comic/201807/',
    '/Volumes/TOURO/Comic/201808/',
    '/Volumes/TOURO/Comic/201809/',
    '/Volumes/TOURO/Comic/201810/',
    '/Volumes/TOURO/Comic/201811/',
    '/Volumes/TOURO/Comic/201812/',

    '/Volumes/TOURO/Comic/201901/',
    '/Volumes/TOURO/Comic/201902/',
    '/Volumes/TOURO/Comic/201903/',
    '/Volumes/TOURO/Comic/201904/',
    '/Volumes/TOURO/Comic/201905/',
    '/Volumes/TOURO/Comic/201906/',
    '/Volumes/TOURO/Comic/201907/',
    '/Volumes/TOURO/Comic/201908/',
    '/Volumes/TOURO/Comic/201909/',
    '/Volumes/TOURO/Comic/201910/',
    '/Volumes/TOURO/Comic/201911/',
    '/Volumes/TOURO/Comic/201912/',

    '/Volumes/TOURO/Comic/202001/',
    #'/Volumes/TOURO/Comic/202002/',
    '/Volumes/TOURO/Comic/202003/',
    '/Volumes/TOURO/Comic/202004/',
    '/Volumes/TOURO/Comic/202005/',
    '/Volumes/TOURO/Comic/202006/',
    '/Volumes/TOURO/Comic/202007/',
    '/Volumes/TOURO/Comic/202008/',
    '/Volumes/TOURO/Comic/202009/',
    '/Volumes/TOURO/Comic/202010/',
]
#-----------------------------------------------------------------
# match [author]
pattern = r'^\[.+?\]'
#-----------------------------------------------------------------
# store key-value
stored_data = {}
#-----------------------------------------------------------------
for path in paths:
    for file_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_name)):
            result = re.match(pattern=pattern, string=file_name)
            if result != None :
                author = result.group()
                if(author not in stored_data):
                    stored_data[author] = []
                stored_data[author].append(os.path.join(path, file_name))
            else:
                print(file_name)
#-----------------------------------------------------------------
np.save('comic.npy', stored_data)
restored_data = np.load('comic.npy', allow_pickle=True).item()
sort_path = '/Volumes/TOURO/Comic/sorted/'
#-----------------------------------------------------------------
for author in restored_data:
    new_author_path = os.path.join(sort_path, author)
    print(new_author_path)
    isExists = os.path.exists(new_author_path)
    if not isExists:
        os.makedirs(new_author_path)
    for comic in restored_data[author]:
        old_comic_path = comic
        new_comic_path = old_comic_path.replace(author + ' ','')
        print(old_comic_path)
        print(new_comic_path)
        os.rename(os.path.join(path,category),os.path.join(path,_category))
        shutil.move(new_comic_path, new_author_path)
#-----------------------------------------------------------------
print('End')
