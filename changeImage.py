#! /usr/bin/env python3

from PIL import Image
import os

source_folder = os.path.abspath('./supplier-data/images')
target_size = (600, 400)

files = os.listdir(source_folder)

for file in files:
    if os.path.splitext(file)[1] == '.tiff':
        source_img = os.path.join(source_folder, file)
        try:
            img = Image.open(source_img)
        except:
            continue
        target_img = os.path.join(source_folder, file)
        img.convert('RGB').resize(target_size).save(target_img + '.jpeg', 'JPEG')
