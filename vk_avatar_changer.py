from pathlib import Path

import time
import os
import random
import requests
import vk

token_user = r'1c53091fae5b8ae2f2c25bf2d940e1d191cb783d6bfd2b6fcbb8b6068879f582d2fb46780ccbd50381398'
API_version = 5.101

path = Path('pictures')
pictures_list = os.listdir(path)
pictures = []
for f in pictures_list:
    pictures.append(f)

session = vk.Session(access_token=token_user)
vk_api = vk.API(session, v=API_version)

upload_url = vk_api.photos.getOwnerPhotoUploadServer(owner_id=-187198717)['upload_url']

while(True):
    time.sleep(300)
    x = random.randint(0, len(pictures) - 1)
    image = {'photo': open(path/pictures[x], 'rb')}
    ur = requests.post(upload_url, files=image).json()
    vk_api.photos.saveOwnerPhoto(server=ur['server'], photo=ur['photo'], hash=ur['hash'])
