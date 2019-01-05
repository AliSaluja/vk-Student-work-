# -*- coding: utf-8 -*-
#!/user/bin/env python3

"""
:authors: binxpy
:github page: https://github.com/binxpy

"""

import vk
import requests
from time import sleep, asctime

def setCover(group_id=None, group_token=None, user_token=None, cover=None, num=0):
    """
    :param group_id: id of the your public in social network (Vk.com).
    :type group_id: int.

    :param group_token: access key of the your public.
    :type group_token: str.

    :param user_token: access key of the you page in social network (vk.com).
    :type user_token: str.

    :param cover: image, what will be set as cover of your public.
    :type cover: str.

    :param num: integer variable for creating a recursion. (WILL NOT EDIT)
    :type num: int (Default = 0)

    """
    if (group_token is None) and (user_token is None) or (cover is None) or (group_id is None):
        raise "status: {}".format("Alert! Underfined params of function with name [setCover]")

    try:
        SESSION = vk.AuthSession(access_token=group_token) if not (group_token is None) else vk.Session(access_token=user_token)
        API = vk.API(session=SESSION, v="5.92")

        url = API.photos.getOwnerCoverPhotoUploadServer(group_id=176129943, crop_x2=9999)["upload_url"]
        cover_img = {"photo": open(file=cover, mode="rb")}

        response = requests.post(url=url, files=cover_img).json()
        API.photos.saveOwnerCoverPhoto(hash=response["hash"], photo=response["photo"])
        
    except Exception as error:
        if num < 4:
            setCover(group_token=group_token, user_token=user_token, num=num+1)
        else:
            with open(file="./log.txt", mode="a") as f:
                f.write("{} | {}\n".format(asctime(), str(error)))
                
