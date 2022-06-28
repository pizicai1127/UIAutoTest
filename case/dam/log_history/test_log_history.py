# -*- coding:utf-8 -*-
# @author:ruiyin
# data:2022/4/28 2:27 下午
# @File:test_log_history.py
import pytest
from pages.assets.LogHistoryPage import LogHistoryPage
import datetime
import calendar


class TestLogHistory:
    def test_log_history_page(self, login_i):
        """
        进入用户动态页面
        @param login_i:
        @return:
        """
        log_history_page = LogHistoryPage(login_i)
        log_history_page.goto_log_history()
        ele = log_history_page.read_yaml_element("log_history_title")
        assert log_history_page._text_content(ele) == '用户动态'

    def test_log_history_search(self,  login_i):
        """
        搜索用户
        @param login_i:
        @return:
        """
        log_history_page = LogHistoryPage(login_i)
        log_history_page.goto_log_history()
        log_history_page.log_history_search()
        ele = log_history_page.read_yaml_element("log_history_title")
        assert log_history_page._text_content(ele) == '用户动态'

    def test_log_history_modular(self, login_i):
        """
        按模块筛选
        @rtype: object
        """
        log_modular_dict = {
            'log_modular_upload': '模块: 上传',
            'log_modular_put_in': '模块: 入库',
            'log_modular_download': '模块: 下载',
            'log_modular_edit': '模块: 编辑',
            'log_modular_share': '模块: 分享',
            'log_modular_delete': '模块: 删除',
            'log_modular_create': '模块: 创建'
        }
        log_history_page = LogHistoryPage(login_i)
        log_history_page.goto_log_history()
        for key, value in log_modular_dict.items():
            selector = log_history_page.read_yaml_element(key)
            log_history_page.log_history_modular(selector)
            ele = log_history_page.read_yaml_element("log_modular_text")
            assert log_history_page._text_content(ele) == value
            log_history_page.goto_log_history()  # 每check一个模块后刷新重新进入浏览器来清空勾选框，因叉号未获取到用此方法

    def test_log_history_time(self, login_i):
        """
        按时间范围筛选
        @rtype: object
        """
        now = datetime.datetime.now()  # 当前时间
        today = now.strftime("%Y.%m.%d")  # 今天的年月日，并格式化
        recent7 = (now-datetime.timedelta(days=7)).strftime("%Y.%m.%d")  # 7天前的年月日
        year = now.year
        month = now.month
        last_day = calendar.monthrange(year, month)[1]  # 最后一天
        start = datetime.date(year, month, 1).strftime('%Y.%m.%d')  # 本月的第一天
        end = datetime.date(year, month, last_day).strftime('%Y.%m.%d')   # 本月的最后一天
        # last_month = now.month - 1
        last_day_1 = calendar.monthrange(year, month-1)[1]
        last_start = datetime.date(year, month-1, 1).strftime('%Y.%m.%d')
        last_end = datetime.date(year, month-1, last_day_1).strftime('%Y.%m.%d')
        log_modular_dict = {
            'log_time_today': '时间范围:'+today+'～'+today,
            'log_time_recent7': '时间范围:' + recent7 + '～' + today,
            'log_time_this_moth': '时间范围:' + start + '～' + end,
            'log_time_last_moth': '时间范围:'+last_start+'～'+last_end
        }
        log_history_page = LogHistoryPage(login_i)
        log_history_page.goto_log_history()
        for key, value in log_modular_dict.items():
            selector = log_history_page.read_yaml_element(key)
            log_history_page.log_history_time(selector)
            ele = log_history_page.read_yaml_element("log_time_text")
            assert log_history_page._text_content(ele) == value



