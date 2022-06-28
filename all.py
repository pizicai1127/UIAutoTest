# -*- coding: utf-8 -*- 
# @Time : 2021/10/13 11:51 
# @Author : Athtony
# @File : all.py
import time
import pytest
import os
from common.conection_function import get_report_data,feishu_inform

if __name__ == '__main__':

    """
    使用系统命令生成allure报告
    """
    #清空 temp文件  保证每次 显示的报告都是最新的
    os.system('rm -rf ./temp')

    # 运行pytest
    pytest.main()
    # pytest.main(['./case/top','./case/ms'])
    # pytest.main(['./case/topmanage'])
    # pytest.main(['./case/dam/assetgroup'])        #yl测试
    # pytest.main(['./case/dam/Asset', './case/dam/AssetBasket', './case/dam/main', './case/dam/assetgroup'])       # lzj测试

    # 本地执行allure 生成报告
    # os.system('cd /Users/congwang/PycharmProjects/watchmen')
    # os.system('allure generate temp -o report --clean')
    
    # 服务器生成aluure 报告
    os.system('/allure-2.15.0/bin/allure generate temp -o report --clean')
    feishu_inform("https://open.feishu.cn/open-apis/bot/v2/hook/6004efb9-745e-459b-8d96-41a8f57ebd9a")
