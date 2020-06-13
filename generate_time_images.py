# -*- coding: utf-8 -*-

from utils import *
import cv2
import numpy as np
from datetime import datetime, timedelta

def get_black_background():
    return np.zeros((600, 600, 3))

def generate_new_time_text(text):
    ind = len(text)
    
    if ind == 4:
        newtext = text[0] + ":" + text[len(text)-2] + text[len(text)-1]
    elif ind == 5:
        newtext = text[0] + text[1] + ":" + text[len(text)-2] + text[len(text)-1]
    else:
        print("wrong", ind)

    return newtext

def generate_image_with_text(text, text5):
    image = get_black_background()
    font = cv2.FONT_HERSHEY_TRIPLEX  #font = cv2.FONT_HERSHEY_SIMPLEX

    text = generate_new_time_text(text)
    text5 = generate_new_time_text(text5)

    text2 = "you are seeing"
    text3 = "this image at"
    text4 = "Greenwich Mean Time"
    text6 = "& my time zone"

    cv2.putText(image, text,
                (int(image.shape[0]*0.4), int(image.shape[1]*0.46)), font,
                1.5, (10, 210, 8),
                2, cv2.LINE_AA)
    cv2.putText(image, text2,
                (int(image.shape[0]*0.295), int(image.shape[1]*0.3)), font,
                1, (10, 210, 8),
                1, cv2.LINE_AA)
    cv2.putText(image, text3,
                (int(image.shape[0]*0.31), int(image.shape[1]*0.37)), font,
                1, (10, 210, 8),
                1, cv2.LINE_AA)
    cv2.putText(image, text4,
                (int(image.shape[0]*0.18), int(image.shape[1]*0.52)), font,
                1, (10, 210, 8),
                1, cv2.LINE_AA)
    cv2.putText(image, text5,
                (int(image.shape[0]*0.4), int(image.shape[1]*0.61)), font,
                1.5, (10, 210, 8),
                2, cv2.LINE_AA)
    cv2.putText(image, text6,
                (int(image.shape[0]*0.27), int(image.shape[1]*0.67)), font,
                1, (10, 210, 8),
                1, cv2.LINE_AA)

    return image

# start_time - do not matter whice date
# it needs to create images. we are writing time anly
start_time = datetime.strptime("2019-01-01", "%Y-%m-%d")
end_time = start_time + timedelta(days=1)
utc6_time = start_time + timedelta(hours=6)

while start_time < end_time:
    text = convert_time_to_string(start_time)
    text5 = convert_time_to_string(utc6_time)
    image = generate_image_with_text(text, text5)
    cv2.imwrite(f"time_images/{text}.jpg", image)
    start_time += timedelta(minutes=1)
    utc6_time += timedelta(minutes=1)

image = cv2.imread('Black_background.jpg', 1)
