# -*- coding: utf-8 -*-
from telethon import TelegramClient, sync
from config import *
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
from utils import *


client = TelegramClient('word', api_id, api_hash)
client.start()

prev_update_time = ""

while True:
    if time_has_changed(prev_update_time):
        prev_update_time = convert_time_to_string(datetime.now())
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(f"time_images/{prev_update_time}.jpg")
        client(UploadProfilePhotoRequest(file))
#ef
