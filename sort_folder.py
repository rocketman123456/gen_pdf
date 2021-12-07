import os
import re
import numpy as np
import shutil
#-----------------------------------------------------------------
paths = [
    '/Volumes/TOURO/Cartoon/',
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
sort_path = '/Volumes/TOURO/Cartoon/sorted/'
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
