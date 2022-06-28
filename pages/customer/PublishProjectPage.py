#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/2/28 2:26 下午
# @File : PublishProjectPage.py
from pages.customer.CustomerBasePage import CustomerBasePage


class PublishProject(CustomerBasePage):
    selectors = {
        "publish_project_btn": ".icon-tz-plus",
        "publish_project": '#rc-root > div.default-layout > div.layout-body > div > div.view-body > div > '
                           'div.spin-container > ul > li.create',
        "typeface_btn": ".slick-slide div div:nth-child(2) div .item-inner",
        "quantity_btn": 'input[type="text"]',
        "black_btn": "html",
        "book_btn": 'text=书籍装帧封面／封底 / 腰封 内页排版特殊工艺其他 >> input[type="checkbox"]',
        "continue_btn": "text=继 续",
        "project_name": 'input[placeholder="如：特赞网站 UI 设计"]',
        "project_stage_btn": 'input[type="radio"]',
        "existing_visual_elements_btn": 'text=没有任何视觉设计有一些核心元素，如 '
                                        'Logo有标识使用手册，创意方可以直接使用我们的视觉系统有标识使用手册，但这个项目的视觉元素仍需要创意方重新设计 >> :nth-match('
                                        'input[type="radio"], 2)',
        "target_user": "textarea",
        "industry_field_btn": "text=行业领域最多选择两个行业 >> input",
        "internet": 'text=互联网',
        "consumption": 'text=消费',
        "industry_field": 'text=行业领域',
        "minimalist": 'text=极简',
        "click_add_style": 'text=添加风格',
        "input_style": 'text=极简扁平拟物活泼商业磨砂Material Design添加风格 >> input',
        "start_time": 'text=灵活（和创意方协调）需要马上开始有具体开始时间 >> :nth-match(input[type="radio"], 2)',
        "project_cycle": 'label:nth-child(5) .ant-radio .ant-radio-input',
        "budget": ".step-body div:nth-child(3) .item-body .ant-radio-group label:nth-child(4) .ant-radio "
                  ".ant-radio-input",
        "location_btn": ".ant-cascader-picker-label",
        "location_china": 'text=中国',
        "location_beijing": 'text=北京',
        "location_beijing_btn": 'text=西城区',
        "mailbox": 'text=姓名职位邮箱电话 >> :nth-match(input[type="text"], 3)',
        "skip_btn": "text=跳 过",
        "channel": '.recommend-info div:nth-child(2) .radio-icon',
        "storage_btn": "#rc-root > div.default-layout > div.layout-body > div > div.view-body > div > div > "
                       "div.view-head > div.head-inner > div.head-title > div > span.tz-action.head-action.head-save",
        "confirm": "text = 确认项目信息",
        "hover_project": '#rc-root > div.default-layout > div.layout-body > div > div.view-body > '
                         'div.spin-wrap.size-default > div.spin-container > ul > li:nth-child(2) > div.c1',
        "copy_btn": '#rc-root > div.default-layout > div.layout-body > div > div.view-body > '
                    'div.spin-wrap.size-default > div.spin-container > ul > li:nth-child(2) > div.operate > span.opt1 '
                    '> i.icon-tz-copy',
        'cancel_btn': "text=取 消",
        'confirm_btn': "text=确 定",
        'delete': "#rc-root > div.default-layout > div.layout-body > div > div.view-body > div > div.spin-container > "
                  "ul > li:nth-child(2) > div.operate > span.opt2 > i.icon-tz-delete",
        'delete_btn': "text=删 除",

    }

    def publish_project(self, quantity_btn, project_name, target_user, input_style, project_cycle, budget, mailbox):
        # 我的项目，点击发布按钮
        self.page.hover(PublishProject.selectors['publish_project'])
        self.page.click(PublishProject.selectors['publish_project_btn'])
        # 点击装帧/字体
        self.page.click(PublishProject.selectors['typeface_btn'])
        # 点击空白
        self.page.click(PublishProject.selectors['black_btn'])
        # 点击书籍装帧
        self.page.check(PublishProject.selectors['book_btn'])
        # 输入下单数量
        self.page.click(PublishProject.selectors['quantity_btn'])
        self.page.fill(PublishProject.selectors['quantity_btn'], quantity_btn)
        # 点击继续按钮
        self.page.click(PublishProject.selectors['continue_btn'])
        # 输入项目名称
        self.page.click(PublishProject.selectors['project_name'])
        self.page.fill(PublishProject.selectors['project_name'], project_name)
        # 选择项目阶段
        self.page.check(PublishProject.selectors['project_stage_btn'])
        self.page.check(PublishProject.selectors['existing_visual_elements_btn'])
        # 输入目标用户
        self.page.click(PublishProject.selectors['target_user'])
        self.page.type(PublishProject.selectors['target_user'], target_user)
        # 点击行业领域，选择互联网和消费
        self.page.click(PublishProject.selectors['industry_field_btn'])
        self.page.click(PublishProject.selectors['internet'])
        self.page.click(PublishProject.selectors['consumption'])
        self.page.click(PublishProject.selectors['industry_field'])
        # 选择风格和添加风格
        self.page.click(PublishProject.selectors['minimalist'])
        self.page.click(PublishProject.selectors['click_add_style'])
        self.page.type(PublishProject.selectors['minimalist'], input_style)
        self.page.press(PublishProject.selectors['minimalist'], "Enter")
        # 点击继续按钮
        self.page.click(PublishProject.selectors['continue_btn'])
        # 选择项目开始时间
        self.page.click(PublishProject.selectors['start_time'])
        self.page.type(PublishProject.selectors['project_cycle'], project_cycle)
        self.page.click(PublishProject.selectors['project_cycle'])
        self.page.click(PublishProject.selectors['budget'])
        # 选择项目预算
        self.page.type(PublishProject.selectors['budget'], budget)
        self.page.click(PublishProject.selectors['budget'])
        # 选择地址
        self.page.click(PublishProject.selectors['location_btn'])
        self.page.click(PublishProject.selectors['location_china'])
        self.page.click(PublishProject.selectors['location_beijing'])
        self.page.click(PublishProject.selectors['location_beijing_btn'])
        # 点击继续按钮
        self.page.click(PublishProject.selectors['continue_btn'])
        # 点击跳过按钮
        self.page.click(PublishProject.selectors['skip_btn'])
        # 点击邮箱，输入邮箱
        self.page.click(PublishProject.selectors['mailbox'])
        self.page.fill(PublishProject.selectors['mailbox'], mailbox)
        # 选择知道特赞的渠道
        self.page.click(PublishProject.selectors['channel'])
        # 点击保存按钮
        self.page.click(PublishProject.selectors['storage_btn'])
        # 点击确定按钮
        self.page.click(PublishProject.selectors['confirm'])

    # 取消复制项目
    def edit_cancel_copy_project(self):
        # 鼠标悬浮，点击复制按钮，点击取消按钮
        self.page.hover(PublishProject.selectors['hover_project'])
        self.page.click(PublishProject.selectors['copy_btn'])
        self.page.click(PublishProject.selectors['cancel_btn'])

    # 复制项目
    def edit_confirm_copy_project(self):
        # 鼠标悬浮，点击复制按钮，点击确定按钮
        self.page.hover(PublishProject.selectors['hover_project'])
        self.page.click(PublishProject.selectors['copy_btn'])
        self.page.click(PublishProject.selectors['confirm_btn'])

    # 取消删除项目
    def delete_cancel_project(self):
        # 鼠标悬浮，点击删除按钮，点击取消按钮
        self.page.hover(PublishProject.selectors['hover_project'])
        self.page.click(PublishProject.selectors['delete'])
        self.page.click(PublishProject.selectors['cancel_btn'])

    # 删除项目
    def delete_project(self):
        # 鼠标悬浮，点击删除按钮，点击确定按钮
        self.page.hover(PublishProject.selectors['hover_project'])
        self.page.click(PublishProject.selectors['delete'])
        self.page.click(PublishProject.selectors['delete_btn'])
