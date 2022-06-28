#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : exception_handle
# @Author: yanglun@tezign.com
# @Date  : 2022/2/20
# @Desc  :  封装异常处理，避免将异常处理写入page和testcase中，直接使用装饰器即可
"""

from common.logger import logger

def element_not_found_exception(func):
    """
    定位元素失败异常处理
    @param func:
    @return:
    """
    def warpper(*args):
        try:
            return func(*args)
        except Exception as e:
            logger.error(f"element not found {e}")
        return None
    return warpper

def exception_logger(func):
    """
    通用异常处理
    @param func:
    @return:
    """
    def warpper(*args):
        try:
            return func(*args)
        except Exception as e:
            logger.error(f"这个地方有错误：{e}")
        return None
    return warpper

