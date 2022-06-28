# -*- coding: utf-8 -*- 
# @Time : 2022/3/4 11:09 
# @Author : WangCong
# @File : conection_function.py
from pages.basepage import BasePage
from playwright.sync_api import Page
import pymysql
import re
import requests
import json


def get_auth_code():
    """从数据库中获取验证码
    可以 填写 数据库账号 和替换sqlsql
    """
    # 建立链接
    conn = pymysql.connect(
        host="rr-2ze77jq079wm3y975.mysql.rds.aliyuncs.com",
        port=3306,
        user="sop_developer",
        password="DWF23RDC@erf234d",
        db="tezign"
    )

    # 创建游标
    cur = conn.cursor()

    # 查询 邮件内容
    cur.execute(
        "select content from tezign.tbl_email where `to` = 'tzvirtual1@tezign.com' order by create_time desc limit 1;")

    # 获取邮件数据
    result = cur.fetchall()
    print(result)
    # 获取 到验证码 n
    auth_code = re.findall(r"邮箱登录验证码「(.+?)」", str(result))
    return auth_code


def feishu_inform(feishu_webhook):
    """
    飞书推送群消息
    推送汇总的消息
    feishu_webhook：填写你的飞书web hook值
    inform_content: 填写你想要推送的内容
    """

    # 服务器路径
    data = get_allure_data("report/widgets/summary.json")
    retry_trend = read_json_file('report/history//retry-trend.json')
    url = feishu_webhook

    payload_message = {
        "msg_type": "text",
        "content": {
            "text": f'UI自动化测试用例执行完毕 \n'
                    f'失败用例数：{data[1]} \n'
                    f'跳过用例数：{data[2]} \n'
                    f'通过用例数：{data[3]} \n'
                    f'执行失败用例数：{data[0]} \n'
                    f'重试测试用例数：{retry_trend["retry"]} \n'
                    f'总用例数：{data[4]} \n'
                    f'测试总时长：{data[7]}分{data[6]}秒  \n'

        }
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload_message))

    print(response.text)


def get_report_data(file_url):
    '''获取测试报告 数据'''
    # 'report/history/history-trend.json'
    with open(file_url) as f:

        # 读取文件
        line = json.load(f)
        # 将list 转化为 dict
        a = line[0]
        # 取dict值 转化为新dict
        b = a["data"]
        f.close()
        return b


def read_json_file(json_file_url):
    '''读取json文件'''

    with open(json_file_url) as f:

        # 读取文件
        line = json.load(f)
        # 将list 转化为 dict
        dict_a = line[0]
        # 取dict值 转化为新dict
        dict_b = dict_a["data"]
        f.close()
        return dict_b


def read_json_file2(json_file_url):
    '''读取json文件'''

    with open(json_file_url) as f:

        # 读取文件
        line = json.load(f)
        f.close()

        return line


def get_allure_data(json_file_url):
    '''读取json文件'''
    # 读取sammary文件

    with open(json_file_url) as f:

        # 读取文件
        line = json.load(f)

        line2 = line["statistic"]
        fail_case_num = line2["failed"]
        broken_case_num = line2["broken"]
        skipped_case_num = line2["skipped"]
        passed_case_num = line2["passed"]
        total_case_num = line2["total"]
        time1 = line["time"]
        duration_time = time1["duration"]
        ms = duration_time % 1000
        secends = duration_time % 1000 // 60
        mineters = duration_time // 60000
        f.close()

        return fail_case_num,broken_case_num,skipped_case_num,passed_case_num,total_case_num,ms,secends,mineters


def seconds_to_time(seconds):

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    return ("%d小时%02d分钟%02d秒" % (h, m, s))

