#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File : RatecardPage.py"""
from pages.designer.DesigerBasePage import DesignerBasePage


class RatePage(DesignerBasePage):
    selectors = {
        "new_services": "text=新增服务",
        "short_video": 'li:has-text("短视频 / 直播")',
        "video": "li:has-text(\"视频 / 拍摄\")",
        "animation": 'li:has-text("动画 / 3D")',
        "make": 'li:has-text("GIF 制作")',
        "select_production": 'li:has-text("GIF动图")',
        "next_step_btn": "text=下一步",
        "lowest_price": '[placeholder="最低价"]',
        "maximum_price": '[placeholder="最高价"]',
        "explain_btn": "text=添加说明",
        "show": "textarea",
        "save_btn": "text=保 存",
        "add_case_btn": 'button:has-text("添加案例")',
        "select_case": "li:nth-child(2) .item-select .select-inner.will div",
        "submit_btn": "text=提 交",
        "relate_case_btn": "text=关联案例中选择",
        "relate_case": ":nth-match(input[type=\"checkbox\"], 4)",
        "delete_btn": "text=删除",
        "click_relate_case": '#rc-root > div > div.layout-body > div > div > div:nth-child(2) > '
                              'div.service-category-view-inner > div.service-image > ul > li > button',
        "view_schematic_btn": "text=查看示意图",
        "publish_now_btn": "text=立即发布",
        "more": "[aria-label=\"icon-more\"] svg",
        "edit_btn": "text=编辑",
        "select_case1": "li:nth-child(4) .item-select .select-inner.will div",
        "tijiao_btn1": "text=提 交",
        "service_picture": "text=动画 / 3D|GIF 制作",
        "edit": "text=编 辑",
        "cancel_btn": "text=取 消",
        "determine_btn": "text=确 定",

    }

    def ratecard(self, lowest_price, maximum_price):
        self.page.click(RatePage.selectors['new_services'])
        # with self.page.expect_navigation(url="https://www.tezign.com/designer/#/ratecardList")：
        self.page.click(RatePage.selectors['short_video'])
        self.page.click(RatePage.selectors['short_video'])
        self.page.click(RatePage.selectors['video'])
        # 选择动态制作
        self.page.click(RatePage.selectors['animation'])
        self.page.click(RatePage.selectors['make'])
        self.page.click(RatePage.selectors['select_production'])
        self.page.click(RatePage.selectors['next_step_btn'])
        print("选择动态制作成功")

        self.page.click(RatePage.selectors['lowest_price'])
        self.page.fill(RatePage.selectors['lowest_price'], lowest_price)
        self.page.click(RatePage.selectors['maximum_price'])
        self.page.fill(RatePage.selectors['maximum_price'], maximum_price)
        print("填写价格成功")

        # # 点击说明，添加备注
        # self.page.click(RatePage.selectors['explain_btn'])
        # self.page.click(RatePage.selectors['show'])
        # self.page.fill(RatePage.selectors['show'], show)
        # self.page.click(RatePage.selectors['save_btn'])
        # print("填写备注成功")

        # 添加案例展示
        self.page.click(RatePage.selectors['add_case_btn'])
        self.page.click(RatePage.selectors['select_case'])
        self.page.click(RatePage.selectors['submit_btn'])
        print("添加案例展示成功")

        # 添加服务主图
        self.page.click(RatePage.selectors['click_relate_case'])
        self.page.click(RatePage.selectors['relate_case_btn'])
        self.page.click(RatePage.selectors['relate_case'])
        with self.page.expect_navigation():
            self.page.click(RatePage.selectors['publish_now_btn'])
        print("服务发布成功哈哈")

    def editratecard(self, modify_lowest_price, modify_maximum_price):
        self.page.click(RatePage.selectors['more'])
        self.page.click(RatePage.selectors['edit_btn'])

        self.page.click(RatePage.selectors['lowest_price'])
        self.page.fill(RatePage.selectors['lowest_price'], modify_lowest_price)

        self.page.click(RatePage.selectors['maximum_price'])
        self.page.fill(RatePage.selectors['maximum_price'], modify_maximum_price)

        # 添加案例展示
        self.page.click(RatePage.selectors['add_case_btn'])
        self.page.click(RatePage.selectors['select_case1'])
        self.page.click(RatePage.selectors['submit_btn'])
        print("添加案例展示成功")
        self.page.click(RatePage.selectors['publish_now_btn'])
        self._wait(1)

        # def gotofuwu(self, url):
        #     self.page.goto(url)
        #     pass

    # 分享服务
    def share(self):
        self.page.goto("https://www.tezign.com/designer/#/ratecardList")
        self.page.click("text=生成主页并分享")
        self.page.click("button:has-text(\"复制链接\")")
        self.page.goto("https://www.tezign.com/designer/#/share/designer?code=37luyoglq&tab=1")

    # 查看编辑的效果
    def service(self):
        self.page.click(RatePage.selectors["service_picture"])
        self._wait(2)
        self.page.click(RatePage.selectors["edit"])
        self.page.click(RatePage.selectors["view_schematic_btn"])
        self.page.click(RatePage.selectors["cancel_btn"])

    # 删除服务
    def delete_service(self):
        self.page.click(RatePage.selectors['more'])
        self.page.click(RatePage.selectors['delete_btn'])
        self.page.click(RatePage.selectors['determine_btn'])
        print("服务删除成功")
