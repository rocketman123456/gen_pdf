import os
import re
import numpy as np
import shutil

paths = [
    'G:\\Comic\\201711\\',
]
sort_path = 'G:\\Comic\\sorted\\'

# match [author]
pattern = r'^\[.+?\]'

# store key-value
stored_data = {}

for path in paths:
    for folder in os.listdir(path):
        if os.path.isdir(os.path.join(path, folder)):
            result = re.match(pattern=pattern, string=folder)
            if result != None :
                author = result.group()
                #print(result.group())
                #new_name = folder.replace(result.group(),'')
                #print(new_name)
                if(author not in stored_data):
                    stored_data[author] = []
                stored_data[author].append(os.path.join(path, folder))
            else:
                print(folder)
for author in stored_data:
    #print(stored_data[author])
    new_author_path = os.path.join(sort_path, author)
    print(new_author_path)
    isExists = os.path.exists(new_author_path)
    if not isExists:
        os.makedirs(new_author_path)
    for comic in stored_data[author]:
        old_comic_path = comic
        new_comic_path = old_comic_path.replace(author,'')
        #print(old_comic_path)
        #print(new_comic_path)
        #os.rename(os.path.join(path,category),os.path.join(path,_category))
        #shutil.move(new_comic_path, new_author_path)
#-----------------------------------------------------------------
np.save('comic.npy', stored_data)
restored_data = np.load('comic.npy', allow_pickle=True).item()
#-----------------------------------------------------------------
print('End')
