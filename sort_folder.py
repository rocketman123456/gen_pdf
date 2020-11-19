import os
import re
import numpy as np
import shutil
#-----------------------------------------------------------------
paths = [
    'G:\\Comic\\201711\\',
    'G:\\Comic\\201712\\',

    #'G:\\Comic\\201801\\',
    #'G:\\Comic\\201802\\',
    #'G:\\Comic\\201803\\',
    #'G:\\Comic\\201804\\',
    #'G:\\Comic\\201805\\',
    #'G:\\Comic\\201806\\',
    #'G:\\Comic\\201807\\',
    #'G:\\Comic\\201808\\',
    #'G:\\Comic\\201809\\',
    #'G:\\Comic\\201810\\',
    #'G:\\Comic\\201811\\',
    #'G:\\Comic\\201812\\',

    #'G:\\Comic\\201901\\',
    #'G:\\Comic\\201902\\',
    #'G:\\Comic\\201903\\',
    #'G:\\Comic\\201904\\',
    #'G:\\Comic\\201905\\',
    #'G:\\Comic\\201906\\',
    #'G:\\Comic\\201907\\',
    #'G:\\Comic\\201908\\',
    #'G:\\Comic\\201909\\',
    #'G:\\Comic\\201910\\',
    #'G:\\Comic\\201911\\',
    #'G:\\Comic\\201912\\',

    #'G:\\Comic\\202001\\',
    ##'G:\\Comic\\202002\\',
    #'G:\\Comic\\202003\\',
    #'G:\\Comic\\202004\\',
    #'G:\\Comic\\202005\\',
    #'G:\\Comic\\202006\\',
    #'G:\\Comic\\202007\\',
    #'G:\\Comic\\202008\\',
    #'G:\\Comic\\202009\\',
    #'G:\\Comic\\202010\\',
]
#-----------------------------------------------------------------
# match [author]
pattern = r'^\[.+?\]'
#-----------------------------------------------------------------
# store key-value
stored_data = {}
#-----------------------------------------------------------------
for path in paths:
    for folder in os.listdir(path):
        if os.path.isdir(os.path.join(path, folder)):
            result = re.match(pattern=pattern, string=folder)
            if result != None :
                author = result.group()
                if(author not in stored_data):
                    stored_data[author] = []
                stored_data[author].append(os.path.join(path, folder))
            else:
                print(folder)
#-----------------------------------------------------------------
np.save('comic.npy', stored_data)
restored_data = np.load('comic.npy', allow_pickle=True).item()
sort_path = 'G:\\Comic\\sorted\\'
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
        #print(old_comic_path)
        #print(new_comic_path)
        #os.rename(os.path.join(path,category),os.path.join(path,_category))
        #shutil.move(new_comic_path, new_author_path)
#-----------------------------------------------------------------
print('End')
