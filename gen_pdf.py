#-*- coding: utf8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, PageBreak
from reportlab.lib.pagesizes import A4,A3,A2,A1, legal, landscape
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch
import PIL.Image,PIL.ExifTags

import glob
import fitz  # 导入本模块需安装 pymupdf 库
import os
import shutil
import threading

paths = [
    '/path/to/comic/',
]
ignore = '.DS_Store'
filetypeList = ['.png', '.jpg', '.jpeg', '.JPG', '.PNG', '.webp']

# 将文件夹中所有jpg图片全部转换为一个指定名称的pdf文件，并保存至指定文件夹
def pic2pdf(img_path, pdf_path, pdf_name):
    # Load Image ------------------------------------------
    imgs = []
    for img in os.listdir(img_path):
        #print("File name: ", img)
        filetype = os.path.splitext(img)[1]
        if img == ignore:
            continue
        if filetype not in filetypeList:
            continue
        #elif filetype == filetypeList[5]:
        #    print(os.path.join(img_path,img))
        #    image_file = PIL.Image.open(os.path.join(img_path,img))
        #    if image_file.mode == "RGBA":
        #        image_file.load()
        #        background = Image.new("RGB", image_file.size, (255, 255, 255))
        #        background.paste(image_file, mask=image_file.split()[3])
        #        image_file = background
        #    save_name = img.replace('webp', 'jpg')
        #    img = save_name
        #    image_file.save('{}'.format(os.path.join(img_path,img)), 'JPEG')
        imgs.append(img)
    imgs.sort()
    #print("Finish Sort Pics: ", pdf_name)
    # Check Image ------------------------------------------
    for img in imgs:
        try:
            image_file = PIL.Image.open(os.path.join(img_path,img))
        except Exception as e:
            print(os.path.join(img_path,img), " error ", e)
    # Make PDF ------------------------------------------
    doc = fitz.open()
    for img in imgs:
        #print(os.path.join(img_path,img))
        try:
            imgdoc = fitz.open(os.path.join(img_path,img))
            pdfbytes = imgdoc.convertToPDF()
            imgpdf = fitz.open("pdf", pdfbytes)
            doc.insertPDF(imgpdf)
        except:
            print(os.path.join(img_path,img))
    # Save File ------------------------------------------
    if os.path.exists(pdf_path + pdf_name):
        os.remove(pdf_path + pdf_name)
    try:
        doc.save(pdf_path + pdf_name)
    except ValueError as v:
        print(pdf_name, ' Page Count: ', doc.pageCount)
        print('Error ', v)
    doc.close()
    return

class MyThread (threading.Thread):
    def __init__(self, threadID, path, category):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.path = path
        self.category = category
    def run(self):
        self.img_path = os.path.join(self.path, self.category)
        self.pdf_name = category + '.pdf'
        pic2pdf(img_path=self.img_path, pdf_path=self.path, pdf_name=self.pdf_name)
        
        self.img_path_success = self.path + 'success/'
        if os.path.exists(self.img_path_success) == False:
            os.mkdir(self.img_path_success)
        shutil.move(self.img_path, self.img_path_success)
        print('Done ', self.pdf_name)

if __name__ == '__main__':
    id = 0
    _threads = []
    print(fitz.__doc__)
    #for path in paths:    
    #    for category in os.listdir(path):
    #        if os.path.isdir(os.path.join(path, category)) and category != 'success':
    #            _thread = MyThread(threadID=id, path=path, category=category)
    #            _thread.start()
    #            _threads.append(_thread)
    #            #_thread.join()
    #    for thread in _threads:
    #        thread.join()
    #    _threads.clear()
    #    print('Done ', path)
    #print('End')

    for path in paths:    
        for author in os.listdir(path):
            for category in os.listdir(author):
                if os.path.isdir(os.path.join(path, category)) and category != 'success':
                    _thread = MyThread(threadID=id, path=path, category=category)
                    _thread.start()
                    _threads.append(_thread)
                    #_thread.join()
            for thread in _threads:
                thread.join()
            _threads.clear()
        print('Done ', path)
    print('End')
