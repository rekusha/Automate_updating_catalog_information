#! /usr/bin/env python3

import requests
import os


url = 'http://localhost/upload/'
source_folder = os.path.abspath('./supplier-data/images')
files = os.listdir(source_folder)

for source_file in files:
    if os.path.splitext(source_file)[1] == '.jpeg':
        img_to_send = os.path.join(source_folder, source_file)
        with open(img_to_send, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            r.status_code
            opened.close()
