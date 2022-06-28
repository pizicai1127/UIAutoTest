#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : config.py
# @Author: liangjun
# @Date  : 2021/11/12
# @Desc  :
"""
import os
import datetime


def datetime_strftime(fmt="%Y%m%d%H"):
    """datetime格式化时间"""
    return datetime.datetime.now().strftime(fmt)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

muse_screenshot_path = os.path.join(BASE_DIR, 'report/screenshot/muse')


if __name__ == '__main__':
    # print(f"{muse_screenshot_path}/1.png")
    print(datetime.date.today().strftime('%Y.%m.%d'))