#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File  : handle_func
# @Author: yanglun@tezign.com
# @Date  : 2022/1/21
# @Desc  :  通用方法工具类
"""

import json
import os
import yaml
import csv
import codecs
from itertools import islice
from conf import confs
from common.logger import logger

class HandleTool():
    """
    工具类，包含各种公共方法
    """

    def read_yaml(self, path=confs.yaml_path):
        """
        读取yaml文件
        @param path: yaml文件路径
        @return:
        """
        try:
            result = yaml.safe_load(open(os.path.dirname(__file__) + path, 'r', encoding='utf-8'))  # 相对路径转绝对路径
            return result
        except FileNotFoundError:
            logger.error('文件读取失败 %s' % FileNotFoundError)

    def read_csv(self, csv_path=confs.csv_path):
        """
        读取data的csv文件
        @param csv_path: csv文件的path
        @return:
        """

        try:
            # 读取本地csv文件
            data = csv.reader(codecs.open(csv_path, 'r', 'utf-8'))

            # 存放用户数据
            user_account = []

            # 循环输出每行信息
            for line in islice(data, 0, None):
                user_account.append(line)
            return user_account
        except FileNotFoundError:
            logger.error('文件读取失败 %s' % FileNotFoundError)

    def read_json(self, json_path= confs.json_path):
        """
        读取data的json文件
        @param json_path: json文件的path
        @return: json字符串
        """
        # 读取json文件

        try:
            with open(json_path, "r") as f:
                data = f.read()
            user_account = json.loads(data)
            return user_account
        except FileNotFoundError:
            logger.error('文件读取失败 %s' % FileNotFoundError)

    def read_ab_file_path(self,  file_name, project_name='tezign-watchmen', file_path='data/test_file/'):
        """
        读取文件的绝对路径
        @param project_name: 项目名称
        @param file_name: 文件名称
        @param file_path: 文件所在目录
        @return:
        """

        cur_path = os.path.abspath(os.path.dirname(__file__))
        root_path = cur_path[:cur_path.find(project_name+"/")+len(project_name+"/")]
        return root_path + file_path + file_name


if __name__ == '__main__':
    fileojb = HandleTool()
    print(fileojb.read_ab_file_path(''))




