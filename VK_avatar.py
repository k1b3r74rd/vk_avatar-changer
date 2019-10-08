from pathlib import Path

import time
import os
import random
import requests
import vk
import logging
import configparser

logging.basicConfig(format=u'[LINE:%(lineno)d]# %(levelname)-9s [%(asctime)s]  %(message)s',
                    level=logging.INFO, filename='logs.log')

pictures = []
path = Path('pictures')


class Config:
    config = configparser.ConfigParser()
    config.read('settings.ini')
    access_token = config.get('Config', 'access_token')
    owner_id = config.get('Config', 'owner_id')
    API_version = config.get('Config', 'API_version')
    timer = int(config.get('Config', 'timer'))


def auth():
    session = vk.Session(access_token=Config.access_token)
    vk_api = vk.API(session, v=Config.API_version)
    return vk_api


def main_auth():
    logging.info('Got config...')
    logging.info('Logging in...')
    auth()


def pictureloader():
    pictures_list = os.listdir(path)
    for f in pictures_list:
        pictures.append(f)
    logging.debug('Pictures sorted.')


def uploadlink():
    upload_url = auth().photos.getOwnerPhotoUploadServer(owner_id=Config.owner_id)['upload_url']
    return upload_url


def main_uploadlink():
    uploadlink()
    logging.info('Logged in.')
    logging.debug('Got upload link.')


def avatarchanger():
    while(True):
        x = random.randint(0, len(pictures) - 1)
        image = {'photo': open(path/pictures[x], 'rb')}
        ur = requests.post(uploadlink(), files=image).json()
        auth().photos.saveOwnerPhoto(server=ur['server'], photo=ur['photo'], hash=ur['hash'])
        logging.info('Picture uploaded successful')
        time.sleep(Config.timer)


if __name__ == '__main__':
    logging.warning('PROGRAM STARTED')
    main_auth()
    pictureloader()
    main_uploadlink()
    logging.info('Main program started.')
    avatarchanger()
