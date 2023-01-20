
import boto3
import json
import requests
import urllib.request
import shutil
import os
import random
import io
import copy

json_object = open('Data.json')

with open('Data.json', 'r') as file:
    data = json.loads(file.read())


AWS_KEY =''
AWS_SECRET = ''

s3 = boto3.client('s3', aws_access_key_id=AWS_KEY,
                      aws_secret_access_key='AWS_SECRET')


img_name = []


def save_output(out):
    with open('Data.json', 'w') as f:
        json.dump(out, f)


for key in data:
    if len(key['pfp_url']) > 0:
        print(key['pfp_url'])
        name = random.randrange(1, 100)
        url = key['pfp_url']
        filename = url.split('/')[-1]
        full_name = str(name)+filename
        r = requests.get(url, allow_redirects=True)
        open(full_name, 'wb').write(r.content)
        # s3.upload_file(full_name, 'dayla', full_name)
        rename = key['pfp_url'] = "https://dayla.s3.amazonaws.com/"+full_name
        temp = copy.deepcopy(key)
        img_name.append(temp)
        save_output(img_name)
    save_output(img_name)
        
       
