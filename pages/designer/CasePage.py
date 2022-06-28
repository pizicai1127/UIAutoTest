#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File : CasePage.py"""

from time import sleep
from pages.designer.DesigerBasePage import DesignerBasePage


class AnliPage(DesignerBasePage):
    # 案例页，操作元素
    selectors = {
        "creat_btn": "text=新建案例",
        "case_name": "input[placeholder=\'输入案例名称\']",
        "case_description": "textarea",
        "anli_xinzhi1": "div[role =\"document\"] span:has-text(\"非商业案例\")",
        "case_nature": "div[role=\"document\"] >> text=非商业案例",
        "industry_field": ".row.mt-24 .col-9 .tui-select-wrap .ant-select-show-arrow .ant-select-selection "
                       ".ant-select-selection__rendered",
        "internet": "text=互联网",
        "consumption": "text=消费",
        # "anli_xuan": "text=* 设计风格", #design_style
        "add_service_type_btn": "text=+添加服务类型",
        "poster_btn": "li:has-text(\"海报 / kv\")",
        "checkbox_poster": 'text=主视觉KV设计海报设计长图设计测试标准spu >> input[type="checkbox"]',
        "copywriting_btn": 'li:has-text("方案 / 文案 / 其他")',
        "checkbox_copywriting": 'text=方案Social平台代运营文案编辑PPT书籍素材购买KOL采买搭建生产打样服装设计驻场服务其他服务 >> input[type=\"checkbox\"]',
        "confirm_btn": ":nth-match(:text(\"确 定\"), 2)",
        "style_btn": "text=* 设计风格添加案例设计风格，输入或搜索后按 Enter 确认 >> input",
        "calendar": "[aria-label=\"icon: calendar\"] svg",
        "january": "text=一月",
        "individual_independent_completion": "text=个人独立完成",
        "private": "text=非公开",
        "determine_btn": "text=确 定",
        "background": ":nth-match(textarea, 2)",
        "blank": "text=编辑成功后页面会实时保存",
        "background_btn": ":.display-flex div:nth-child(2) .tip-icon .anticon.type-hover",
        "upload_button": 'xpath=//*[@id="rc-root"]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/span',
        "upload": 'xpath=//*[ @ id = "rc-root"]/div/div[2]/div[2]/div[1]/div[3]/div[2]/input',
        "click_on_the_picture": "img",
        "set_as_cover": "text=设为封面",
        "cutting": ".cropper - point.point - se",
        "cover_confirmation": "text=确 认",
        "cover_description": "text=图片编辑 替换文件 调整排序 删除文件 设为封面 >> textarea",
        # "save": "text=保存",
        "more_btn": "li:nth-child(1) .item-footer .item-brand .operator-dot",
        "edit_btn": 'li[role="menuitem"]:has-text("编辑")',
        "describe": "text=背景描述背景描述背景描述背景描述",
        "brand": "text=相关品牌（选填）添加案例服务品牌，输入或搜索后按 Enter 确认 >> input",
        "design_style": "text=* 设计风格",
        "confirm_modification": "text=确定修改",
        "describe_background": "text=背景描述背景描述背景描述背景描述",
        "save_btn": "text=保存",
        "click_blank": "text=退出编辑编辑案例信息保存",
        "delete_btn": "li[role=\"menuitem\"]:has-text(\"删除\")",
        "business_btn": 'text = 商业案例非商业案例 >> input[type =\"checkbox\"]',
        "non_business_btn": ":nth-match(input[type=\"checkbox\"], 3)",
        "add_material": "text=新添加素材",
        "source_material": '.tip-btn',
        "click_the_input_box": "p",
        "add_text_btn": "text = 文字",
        "sucai11": '.tip-btn',

    }

    @staticmethod
    def check_element() -> None:
        """页面审查元素"""
        print("页面审查元素成功")
        pass

    # 创意方案例流程
    def anlicase(self, case_name, case_description, style_btn, background):
        # 点击新建案例按钮
        self.page.click(AnliPage.selectors['creat_btn'])
        # 输入风格
        self.page.fill(AnliPage.selectors['style_btn'], style_btn)
        self.page.click(AnliPage.selectors['design_style'])
        # self.page.wait_for_load_state("networkidle")
        # self.page.wait_for_load_state("load")
        # 选择案例性质
        self.page.click(AnliPage.selectors['case_nature'])
        self._wait(1)
        # 输入案例名称
        self.page.click(AnliPage.selectors['case_name'])
        self.page.fill(AnliPage.selectors['case_name'], case_name)

        # 输入案例描述
        self.page.click(AnliPage.selectors['case_description'])
        self.page.fill(AnliPage.selectors['case_description'], case_description)
        # sleep(1)

        self.page.click(AnliPage.selectors['case_nature'])

        # 选择行业领域
        self.page.click(AnliPage.selectors['industry_field'])
        self.page.click(AnliPage.selectors['internet'])
        self.page.click(AnliPage.selectors['consumption'])
        self.page.click(AnliPage.selectors['industry_field'])

        # 点击添加服务类型
        self.page.click(AnliPage.selectors['add_service_type_btn'])
        # 点击海报/KV
        self.page.click(AnliPage.selectors['poster_btn'])
        # 选择海报
        self.page.check(AnliPage.selectors['checkbox_poster'])
        # 点击方案/文案
        self.page.click(AnliPage.selectors['copywriting_btn'])
        # 选择方案
        self.page.check(AnliPage.selectors['checkbox_copywriting'])

        # 点击确定按钮
        self.page.click(AnliPage.selectors['confirm_btn'])

        # 选择日历
        self.page.click(AnliPage.selectors['calendar'])
        self.page.click(AnliPage.selectors['january'])

        self.page.click(AnliPage.selectors['individual_independent_completion'])
        self.page.click(AnliPage.selectors['private'])
        self.case_name("测试案例1")
        self.designer("特赞")

        with self.page.expect_navigation():
            self.page.click(AnliPage.selectors['determine_btn'])
            self.page.wait_for_load_state("load")

        self.page.click(AnliPage.selectors['background'])

        self.page.fill(AnliPage.selectors['background'], background)

        self.page.click(AnliPage.selectors['blank'])
        # self.upload_file1("Users/tezign/Downloads/tup/tu/u3.jpeg")
        """上传图片本地可以；git不行，所以暂注释了
        self.upload_file()
        sleep(2)
        # 等待图片元素出来
        self.page.wait_for_selector(AnliPage.selectors['dianjitupian'])

        self.page.click(AnliPage.selectors['dianjitupian'])
        sleep(1)

        self.page.click(AnliPage.selectors['sheweifengm'])
        sleep(1)

        self.page.click(AnliPage.selectors['fengmianqueren'])
        self.page.fill(AnliPage.selectors['fengmianmiaoshu'], fengmianmiaoshu)"""

        self.page.click(AnliPage.selectors['save_btn'])
        self.goto("https://www.tezign.com/designer/#/portfolio")
        print("新建案例成功")

    def gotoanli(self, url):
        self.page.goto(url)

    # /Users/tezign/Downloads/tup/shangchuan.png
    # / Users / tezign / Downloads / tup / u3.jpeg
    # https://git.tezign.com/engineering/tezign-watchmen/blob/zjb/case/designer/u3.jpeg
    def upload_file(self, files=["/Users/tezign/Downloads/tup/u3.jpeg"]):
        self.upload(files)

    # 上传文件操作
    def upload(self, files):
        self.page.click(AnliPage.selectors['upload_button'])
        self.page.set_input_files(AnliPage.selectors['upload'], files)

    # 获取元素文本内容操作
    def get_Content(self, selectors):
        return self._text_content(selectors)

    def case_name(self, case_name):
        """若页面没有案例名称，则再次填写，重新提交"""
        self.page.wait_for_load_state('networkidle')
        # if self.page.query_selector(AnliPage.selectors['anli_name']).get_attribute("value") == "测试案例1":
        if self.page.get_attribute(AnliPage.selectors['case_name'], "value") == "测试案例1":
            pass
        else:
            self.page.fill(AnliPage.selectors['case_name'], case_name)
            # anli_name = self.page.get_attribute(AnliPage.selectors['anli_name'], anli_name)
            # assert anli_name == "Text"

    def designer(self, style_btn):
        """若页面没有风格，重新提交"""
        self.page.wait_for_load_state('networkidle')
        # if self.page.query_selector(AnliPage.selectors['style_btn']).get_attribute("value") == "特赞":
        if self.page.get_attribute(AnliPage.selectors['style_btn'], "value") == "特赞":
            pass
        else:
            self.page.fill(AnliPage.selectors['style_btn'], style_btn)
            self.page.click(AnliPage.selectors['design_style'])
            self._wait(2)

    # 上传图片，输入法要切换英文
    # def upload_file1(self, file):
    #     self.page.click(AnliPage.selectors['upload_button'])
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
    #     sleep(1)
    #     k.type_string(file)
    #     sleep(1)
    #     k.press_key('Return')
    #     sleep(2)
    #     k.press_key('Return')
    #     sleep(2)

    # 编辑修改案例
    def editcase(self, describe, brand, describe_background, click_the_input_box):
        self.page.click(AnliPage.selectors['more_btn'])
        self.page.click(AnliPage.selectors['edit_btn'])
        self.page.click(AnliPage.selectors['describe'])
        self.page.fill(AnliPage.selectors['describe'], describe)

        self.page.click(AnliPage.selectors['brand'])
        self.page.fill(AnliPage.selectors['brand'], brand)
        self.page.click(AnliPage.selectors['design_style'])
        self.page.click(AnliPage.selectors['confirm_modification'])
        self._wait(2)
        self.page.click(AnliPage.selectors['describe_background'])
        self.page.fill(AnliPage.selectors['describe_background'], describe_background)
        print("背景修改成功")
        # 添加文字
        self.page.click(AnliPage.selectors['add_text_btn'])

        self.page.click(AnliPage.selectors['add_material'])
        self.page.click(AnliPage.selectors['source_material'])
        self.page.click(AnliPage.selectors['click_the_input_box'])
        self.page.fill(AnliPage.selectors['click_the_input_box'], click_the_input_box)

        self.page.click(AnliPage.selectors['click_blank'])

        self.page.click(AnliPage.selectors['save_btn'])
        print("保存成功")

    @staticmethod
    def check_element() -> None:
        """页面审查元素"""
        print("页面审查元素成功")

    # def gotoanli(self, url):
    #     self.page.goto(url)

    # 删除案例
    def deletecase(self):
        self.page.click(AnliPage.selectors['more_btn'])
        self.page.click(AnliPage.selectors['delete_btn'])
        self.page.click(AnliPage.selectors['determine_btn'])
        print("案例删除成功")

    # 商业非商业
    def case_type(self):
        self.page.uncheck(AnliPage.selectors['business_btn'])
        self.page.uncheck(AnliPage.selectors['non_business_btn'])
        self.page.check(AnliPage.selectors['business_btn'])
        self.page.check(AnliPage.selectors['non_business_btn'])
