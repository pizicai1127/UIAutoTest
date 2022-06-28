#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/6/15 5:59 下午
# @File : MusePage.py

# import pyperclip
# from pykeyboard import PyKeyboard
# from pymouse import PyMouse
#
from pages.muse.MuseBasePage import MuseBasePage


class MusePage(MuseBasePage):
    selectors = {
        "add_btn": ".plus-btn___1OZ11",  # 添加按钮
        'creat_link': 'button:has-text("生成链接")',
        "creat_link_btn": '#root > div > div.drag-box___xM3gW.backdrop-filter___3P37L.bounce___1pbD1 > div.upload-panel___u0wlR > div.bottom___2pvz9.bottom-bg___3_dAL > div.upload-area___3HOj_ > button > span',
        "agree_btn": "#root > div > div.drag-box___xM3gW.backdrop-filter___3P37L.bounce___1pbD1 > div.policy-area___3tuO1 > button > span",
        "agree": 'button:has-text("我同意")',
        "drag_and_drop": "#root > div > div.drag-box___xM3gW.backdrop-filter___3P37L.bounce___1pbD1 > div.drag-area___D1q8O > div",
        # "add_btn": "img[alt=\"icon-plus\"]",
        # "add_btn": "img[alt=\"icon-plus\"]",
        # "add_btn": "img[alt=\"icon-plus\"]",
        'a': 'text=传输历史',
        'b': 'text=联系我们',
        'c': 'text=了解我们',
        '': '',
        '': '',
        '': '',
        '': '',
        '': '',
        '': '',
        '': '',

    }

    # 鼠标拖拽操作
    def drag_and_drop(self):
        self._click(MusePage.selectors['drag_and_drop'])
        # self.page.mouse.move(1000, 1500)
        # self.page.mouse.down()
        # self.page.mouse.move(991, 313)
        # self.page.mouse.up()




    def homepage(self):
        # 点击添加按钮
        self.page.click(MusePage.selectors['add_btn'])

        self.upload_file("Users/tezign/Downloads/tup/tu/u3.jpeg")
        # self.upload_file("Users/tezign/Downloads/tup/tu/u3.jpeg")
        self.close_agreetanchuang()
        self.page.click(MusePage.selectors['creat_link'])

    def close_agreetanchuang(self):
        """若页面出现提示同意弹窗，则点击关闭按钮"""
        self.page.wait_for_load_state('networkidle')
        self._wait(3)
        if self.page.query_selector("text=即刻开启飞速传输～"):
            self.page.click(MusePage.selectors['agree'])

    def upload_file(self, files=["/Users/tezign/Downloads/tup/u3.jpeg"]):
        self.upload(files)

    # 上传文件操作
    def upload(self, files):
        self.page.hover(MusePage.selectors['add_btn'])
        self.page.click(MusePage.selectors['add_btn'])
        self.page.set_input_files(MusePage.selectors['add_btn'], files)

    # 上传图片，输入法要切换英文
    # def upload_file1(self, file):
    #     self.page.click(HomeMusePage.selectors['add_btn'])
    #     k = PyKeyboard()
    #     m = PyMouse()
    #     filepath = '/'
    #     k.press_keys(['Command', 'Shift', 'G'])
    #     x_dim, y_dim = m.screen_size()
    #     m.click(x_dim // 2, y_dim // 2, 1)
    #     # 复制文件路径开头的斜杠/
    #     pyperclip.copy(filepath)
    #     # 粘贴斜杠/
    #     k.press_keys(['Command', 'V'])
    #     # 输入文件全路径进去
    #     self._wait(2)
    #     k.type_string(file)
    #     self._wait(2)
    #     k.press_key('Return')
    #     self._wait(2)
    #     k.press_key('Return')
    #     self._wait(1)

    # # 获取元素文本内容操作
    # def get_Content(self, selectors):
    #     return self._text_content(selectors)
