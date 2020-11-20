import zipfile
import rarfile
from pathlib import Path
import os

paths = [
    'G:\\Comic\\201801\\',
]

for path in paths:
    for zip_file in os.listdir(path):
        if os.path.isfile(os.path.join(path, zip_file)):
            print(zip_file)
            f = None
            if os.path.splitext(zip_file)[1] == '.zip':
                f = zipfile.ZipFile(os.path.join(path, zip_file), 'r')
            if os.path.splitext(zip_file)[1] == '.rar':
                f = rarfile.RarFile(os.path.join(path, zip_file))
            namelist = f.namelist()
            for file_name in f.namelist():
                extracted_path = Path(f.extract(file_name, path=path))
                extracted_path.rename(os.path.join(path, file_name).encode('cp437').decode('gbk'))
            f.close()
            for name in namelist:
                if os.path.isdir(os.path.join(path, name)):
                    print(os.path.join(path, name))
                    os.rmdir(os.path.join(path, name))
                    break
print('End')



