#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/3/7 5:20 下午
# @File : NewEnterpriseProjectPage.py
from pages.topmanage.TopBasePage import TopBasePage


class NewEnterpriseProjectPage(TopBasePage):
    selectors = {
        "create_project": "text=新建项目",
        "project_title": 'input[placeholder="请输入项目的标题"]',
        # 选择campaign按钮
        "campaign": "text=Campaign类",
        # 选择content按钮
        "content": "text=Content类",
        "background": '[aria-label="rdw-editor"] >> :nth-match(div, 3)',
        "preview": "text=预览",
        # 点击蒙层
        "close": "body > div:nth-child(13) > div > div.ant-modal-wrap.ant-modal-centered",
        "project_budget": '[placeholder="请输入项目预算"]',
        "delivery_time_btn": '[placeholder="请选择具体时间"]',
        "next_month": ".ant-calendar-next-month-btn",
        "delivery_time": 'span:has-text("今天")',
        "non_comparison_items": "text=非比稿项目",
        "input_customer": "text=选择签单后自动填充，若无签单，请手动选择客户部门",
        "customer_department": 'li[role="option"]:has-text("阿里巴巴零售通")',
        "save_draft": "text=保存草稿",
        "draft_project": "text=测试项目",
        "delete_draft_project": "text=删除草稿",
        "cancel": "text=取 消",
        "confirm_delete": 'button:has-text("确认删除")',
        "next_step": "text=下一步",
        "previous_step": "text=上一步",
        "3D_poster": "text=使用3D海报 >> span",
        "cartoon_poster": "text=使用漫画海报 >> span",
        "quantity": 'input[placeholder="0"]',
        "quantity_btn": 'text=海报 / kv|海报设计|漫画海报数量展开 >> [placeholder="0"]',
        "view_budget": 'label:has-text("展示为待定")',
        "publish_project": "text=发布项目",
        "marketing_purpose": "text=请输入或选择营销目的",
        "brand_promotion": "text=品牌宣传",
        "brand_design": "text=新品牌设计",
        "marketing_btn": "text=营销目的",
        "style": "text=请输入并选择风格",
        "simplicity": 'li[role="option"]:has-text("简约")',
        "style": "text=请输入并选择风格",
        # "style": "text=请输入并选择风格",
        # "style": "text=请输入并选择风格",
        # "style": "text=请输入并选择风格",
        # "style": "text=请输入并选择风格",
        # "style": "text=请输入并选择风格",
        # "style": "text=请输入并选择风格",
        # "style": "text=请输入并选择风格",
        # "style": "text=请输入并选择风格",
        # "style": "text=请输入并选择风格",
        # "style": "text=请输入并选择风格",
        # "style": "text=请输入并选择风格",
        # "style": "text=请输入并选择风格",



    }

    def create_project(self, project_title, background, project_budget, input_customer):
        # 点击新建项目
        self._click(NewEnterpriseProjectPage.selectors['create_project'])
        # 选择campaign和content类
        self._click(NewEnterpriseProjectPage.selectors['campaign'])
        self._check(NewEnterpriseProjectPage.selectors['content'])
        # 输入项目标题
        self._fill(NewEnterpriseProjectPage.selectors['project_title'], project_title)
        self._click(NewEnterpriseProjectPage.selectors['background'])
        # 输入项目背景
        self._fill(NewEnterpriseProjectPage.selectors['background'], background)
        self._click(NewEnterpriseProjectPage.selectors['marketing_purpose'])
        self._click(NewEnterpriseProjectPage.selectors['brand_promotion'])
        self._click(NewEnterpriseProjectPage.selectors['brand_design'])
        self._click(NewEnterpriseProjectPage.selectors['marketing_btn'])
        self._click(NewEnterpriseProjectPage.selectors['style'])
        self._click(NewEnterpriseProjectPage.selectors['simplicity'])
        self._click(NewEnterpriseProjectPage.selectors['marketing_btn'])
        # 输入项目预算
        self._fill(NewEnterpriseProjectPage.selectors['project_budget'], project_budget)
        # 选择项目交付日期
        self._click(NewEnterpriseProjectPage.selectors['delivery_time_btn'])
        self._click(NewEnterpriseProjectPage.selectors['next_month'])
        self._click(NewEnterpriseProjectPage.selectors['delivery_time'])
        # 选择非比稿
        self._click(NewEnterpriseProjectPage.selectors['non_comparison_items'])
        # 选择客户部门
        self._click(NewEnterpriseProjectPage.selectors['input_customer'])
        self._type(NewEnterpriseProjectPage.selectors['input_customer'], input_customer)
        self._click(NewEnterpriseProjectPage.selectors['customer_department'])
        self._click(NewEnterpriseProjectPage.selectors['save_draft'])

    def edit_draft_project(self, quantity, quantity_btn):
        # 点击要编辑的草稿项目
        self._click(NewEnterpriseProjectPage.selectors['draft_project'])
        # 点击下一步
        self._click(NewEnterpriseProjectPage.selectors['next_step'])
        # 选择3D海报
        self._click(NewEnterpriseProjectPage.selectors['3D_poster'])
        # 选择漫画海报
        self._click(NewEnterpriseProjectPage.selectors['cartoon_poster'])
        # 点击数量
        self._click(NewEnterpriseProjectPage.selectors['quantity'])
        self._fill(NewEnterpriseProjectPage.selectors['quantity'], quantity)
        self._click(NewEnterpriseProjectPage.selectors['quantity_btn'])
        self._fill(NewEnterpriseProjectPage.selectors['quantity_btn'], quantity_btn)
        # 可见预算
        self._check(NewEnterpriseProjectPage.selectors['view_budget'])
        # 上一步
        self._click(NewEnterpriseProjectPage.selectors['previous_step'])
        # 点击下一步
        self._click(NewEnterpriseProjectPage.selectors['next_step'])
        # 保存草稿
        self._click(NewEnterpriseProjectPage.selectors['save_draft'])

    def publish_project(self):
        # 点击要编辑的草稿项目，进行发布
        self._click(NewEnterpriseProjectPage.selectors['draft_project'])
        self._click(NewEnterpriseProjectPage.selectors['next_step'])
        self._click(NewEnterpriseProjectPage.selectors['publish_project'])

    def delete_draft_project(self):
        # 点击要删除的草稿项目
        self._click(NewEnterpriseProjectPage.selectors['draft_project'])
        # 点击删除按钮
        self._click(NewEnterpriseProjectPage.selectors['delete_draft_project'])
        # 点击取消按钮
        self._click(NewEnterpriseProjectPage.selectors['cancel'])
        # 点击删除按钮
        self._click(NewEnterpriseProjectPage.selectors['delete_draft_project'])
        # 点击确认删除按钮
        self._click(NewEnterpriseProjectPage.selectors['confirm_delete'])

    def edit_publish_project(self):
        # 点击要编辑的草稿项目，进行发布
        with self.page.expect_popup() as popup_info:
            self._click(NewEnterpriseProjectPage.selectors['draft_project'])
        page1 = popup_info.value
        page1.close()