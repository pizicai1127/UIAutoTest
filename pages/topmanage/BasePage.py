#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File : BasePage.py"""

from playwright.sync_api import Page
from common.logger import logger


class BasePage:
    """
    基础Page层，在这里可以封装一些公共重复方法 ，例如 寻找元素，等待，点击等
    """

    # 定义构造函数，初始化 page
    def __init__(self, page: Page = None, ) -> None:
        if page is not None:
            self.page = page

    # # 重新封装一个 click方法
    # def t_click(self, locator):
    #     self.page.fill(locator)

    # 获取cookies模拟登录

    #  封装 click动作
    def _click(self, element):
        logger.info(f"点击页面元素{element}")
        self.page.click(element)

    #  封装 type动作
    def _type(self, element, text):
        logger.info(f"点击页面元素{element}")
        self.page.type(element, text)

    #  封装 check动作
    def _check(self, element):
        logger.info(f"点击页面元素{element}")
        self.page.check(element, )

    #  封装 uncheck动作
    def _uncheck(self, element):
        logger.info(f"点击页面元素{element}")
        self.page.uncheck(element, )

    #  封装 hover动作
    def _hover(self, element):
        logger.info(f"点击页面元素{element}")
        self.page.hover(element, )

    #  封装 fill动作
    def _fill(self, element, text):
        logger.info(f"向页面元素{element}中输入：{text}")
        self.page.fill(element, text)

    #  封装 set_input_files动作
    def _set_input_files(self, element, file):
        logger.info(f"向页面元素{element}中输入：{file}")
        self.page.set_input_files(element, file)

    #  封装 text_content动作
    def _text_content(self, element):
        logger.info(f"获取页面元素{element} 中的文本内容")
        return self.page.text_content(element)

    #  封装 内部文字
    def _inner_text(self, element):
        logger.info(f"获取页面元素{element} 中的文本内容")
        return self.page.inner_text(element)

    #  封装 内部文字
    def _get_attribute(self, element,value):
        logger.info(f"获取页面元素{element} 中的文本内容")
        return self.page.get_attribute(element,value)

    # 封装 goto方法
    def goto(self, url):
        logger.info(f"跳转到：{url} ")
        self.page.goto(url)

    #  封装等待动作(1s=1000)
    def _wait(self, time):
        self.page.wait_for_timeout(time * 1000)

    # 判断元素是否可见
    def _is_visible(self, element):
        logger.info(f"判断{element}是否可见")
        return self.page.is_visible(element)

    def is_checked(self, selector):
        pass

    def check(self, selector):
        pass
