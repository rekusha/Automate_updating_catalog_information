#! /usr/bin/env python3

import os
import requests


source_text_folder = os.path.abspath('./supplier-data/descriptions')
source_image_folder = os.path.abspath('./supplier-data/images')
files = os.listdir(source_text_folder)
url = ('http://[!!!_IP_!!!]/fruits/') #insert IP


for file in files:
    with open(os.path.join(source_text_folder, file), 'r') as f:
        name = f.readline().strip()
        weight = int(f.readline().strip().split()[0])
        description = f.read()
        image_name = os.path.splitext(file)[0] + '.jpeg'
        f.close()
        data_dict = {'name': name, 'weight': weight, 'description': description, 'image_name': image_name}
        r = requests.post(url, json=data_dict)
        print(r.status_code)
