# -*- coding: utf-8 -*-
from datetime import datetime

def convert_time_to_string(dt):
    return f"{dt.hour} {dt.minute:02}"

def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != prev_time
