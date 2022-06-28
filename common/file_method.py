#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/10 7:25 下午
# @Author  : wmt
# @File    : file_method.py
# @Software: PyCharm
import configparser
import json
import logging
import os
import yaml


class FileMethod:
    def get_file_path(self, package_name, dir_name, file_name):
        ##找到文件父级目录
        base_root = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

        package_root = os.path.abspath(os.path.join(base_root, package_name))
        dir_root = os.path.join(package_root, dir_name)
        file_path = os.path.join(dir_root, file_name)
        return file_path

    def read_yaml(self,file_path):
        """
        读取yaml文件的方法
        :param file_path: 文件路径
        :return:
        """

        logging.info(f"加载 {file_path} 文件")
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
            f.close()
        logging.info(f"读到数据 ==>>  {data} ")
        return data

    def read_json(self,file_path):
        """
        读取json文件的方法
        :param file_path: 文件路径，完整的路径
        :return:
        """

        logging.info(f"加载 {file_path} 文件")
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
            f.close()
            logging.info(f"读到数据 ==>>  {data} ")
        return data

    def read_ini(self,file_path):

        logging.info(f"加载 {file_path} 文件")
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="UTF-8")
        data = dict(cf._sections)
        print(f"读到数据 ==>>  {data} ")
        return data




if __name__ == '__main__':



    file_path = FileMethod().get_file_path('data/test_file',"",'UI自动化测试1.jpg')





    print(file_path)
