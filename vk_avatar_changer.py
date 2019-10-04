from pathlib import Path

import time
import os
import random
import requests
import vk

# Insert your user token and profile/group ID accordingly. Remember about minus before group ID.
user_token = '1c53091fae5b8ae2f2c25bf2d940e1d191cb783d6bfd2b6fcbb8b6068879f582d2fb46780ccbd50381398'
owner_id = -187198717

API_version = 5.101

path = Path('pictures')
pictures_list = os.listdir(path)
pictures = []
for f in pictures_list:
    pictures.append(f)

session = vk.Session(access_token=user_token)
vk_api = vk.API(session, v=API_version)

upload_url = vk_api.photos.getOwnerPhotoUploadServer(owner_id=owner_id)['upload_url']

while(True):
    x = random.randint(0, len(pictures) - 1)
    image = {'photo': open(path/pictures[x], 'rb')}
    ur = requests.post(upload_url, files=image).json()
    vk_api.photos.saveOwnerPhoto(server=ur['server'], photo=ur['photo'], hash=ur['hash'])
    print('Avatar has changed successfully.')
    time.sleep(300)
