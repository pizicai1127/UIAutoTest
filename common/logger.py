#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@file: logger.py
@Date: 2021/08/24 15:48:26
@Author: Rethink
@Description:
'''
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
                  #   (filename='test.log')
logger = logging.getLogger(__name__)
