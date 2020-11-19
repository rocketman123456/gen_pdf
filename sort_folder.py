import os
import re
import numpy as np

paths = [
    'G:\\Comic\\201711\\',
]

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
                new_name = folder.replace(result.group(),'')
                #print(new_name)
                if(author not in stored_data):
                    stored_data[author] = []
                stored_data[author].append(new_name)
            else:
                print(folder)
#-----------------------------------------------------------------
np.save('comic.npy', stored_data)
restored_data = np.load('comic.npy', allow_pickle=True).item()
#-----------------------------------------------------------------
print('End')
