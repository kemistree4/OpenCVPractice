#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

foreground_img_path = '/home/kemistree4/Desktop/bug_1.png'

def convertToPNG(foreground_img_path = foreground_img_path):
    img = Image.open(foreground_img_path)#image path and name
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save("Bug_1_w_alpha.png", "PNG")#converted Image name
    print('Done')

convertToPNG()

