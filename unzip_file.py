import zipfile
import rarfile
import py7zr
from pathlib import Path
import os

paths = [
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

for path in paths:
    for zip_file in os.listdir(path):
        if os.path.isfile(os.path.join(path, zip_file)):
            print(zip_file)
            f = None
            if os.path.splitext(zip_file)[1] == '.zip':
                f = zipfile.ZipFile(os.path.join(path, zip_file), 'r')
            if os.path.splitext(zip_file)[1] == '.rar':
                f = rarfile.RarFile(os.path.join(path, zip_file))
            if os.path.splitext(zip_file)[1] == '.7z':
                f = py7zr.SevenZipFile(os.path.join(path, zip_file))
            f.extractall(path=path)
            #namelist = f.namelist()
            #for file_name in f.namelist():
            #    extracted_path = Path(f.extract(file_name, path=path))
            #    extracted_path.rename(os.path.join(path, file_name).encode('cp437').decode('gbk'))
            f.close()
            #for name in namelist:
            #    if os.path.isdir(os.path.join(path, name)):
            #        print(os.path.join(path, name))
            #        os.rmdir(os.path.join(path, name))
            #        break
            os.remove(os.path.join(path, zip_file))
    print("Done" + path)
print('End')



