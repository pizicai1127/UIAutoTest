#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/5/7 10:38 上午
# @File : SalePage.py
from pages.topmanage.TopBasePage import TopBasePage


class SalePage(TopBasePage):
    selectors = {
        "crm_tab": "#rc-root > div.main > div.side > div.side_row1 > ul > li:nth-child(2) > div > span > span",
        "sale_btn": "text = 销售机会",
        "search_btn": "text=搜索",
        "reset_btn": "text=重置",
        "more_search_btn": "text=更多筛选",
        "select_business_type_btn": "#rc-root > div.main > div.wrap > div > div:nth-child(2) > div > div > div:nth-child(2) > div > div.ant-col.ant-col-17 > div > div.ant-select-show-arrow.ant-select.ant-select-enabled.ant-select-allow-clear > div > div > div",
        "select_content": 'li[role="option"]:has-text("Content业务")',
        "input_sale_name": '[placeholder="请输入机会名称"]',
        "delete_sale_btn": '[aria-label="图标: close"] svg',
        "create_sale_btn": "text=新建销售机会",
        "input_name_btn": 'text=企业名称请选择企业部门阿里公司 机会名称机会类型请选择机会类型Content业务请选择机会分类标准项目是否需要比稿是否需要比稿否需求描述客户意向SKU请选择SK >> ['
                          'placeholder="请输入机会名称"]',
        "select_company_name": 'text=企业名称请选择企业部门 >> input[type="text"]',
        "select_company": 'li[role="option"]:has-text("阿里公司")',
        "select_company_btn": "._n29Q3",
        "requirements_description": 'text=企业名称请选择企业部门阿里公司 机会名称机会类型请选择机会类型Content业务请选择机会分类标准项目是否需要比稿是否需要比稿否需求描述客户意向SKU'
                                    '请选择SK >> textarea',
        "select_SKU": 'div[role="document"] >> text=请选择SKU类型',
        "select_port": "text=海报 / kv",
        "select_customer": 'div[role="combobox"]:has-text("请选择客户部门")',
        "confirm_select_customer": 'li[role="option"]:has-text("阿里部门")',
        "customer_contact_btn": ':nth-match(:text("客户首次联系人"), 2)',
        "confirm_customer_contact_btn": "text=阿里测试 | 阿里部门 | 15244145431",
        "customer_type": 'body > div:nth-child(15) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                         'div.ant-modal-body > div > div:nth-child(9) > div.ant-col.ant-col-18 > div > '
                         'div.ant-select-show-arrow.ant-select.ant-select-enabled > div > div > div',
        "confirm_customer_type": 'li[role="option"]:has-text("新客户机会")',
        "input_estimate_price": 'input[placeholder="请输入预估销售金额（元）"]',
        "input_cost": '[placeholder="请输入预估项目成本（元）"]',
        "input_estimate_date": '[placeholder="请选择预计成单日期"]',
        "confirm_estimate_date": 'span:has-text("今天")',
        "estimated_delivery_date": '[placeholder="请选择预估交付时间"]',
        "confirm_estimated_delivery_date": "text=今天",
        'submit_btn': 'text = 提交',
        'cancel_btn': 'text = 取消',
        'edit_sale': ':nth-match(td:has-text("测试销售机会25"), 2)',
        'edit_brief': 'text=创建/编辑Brief',
        'relation_brief': 'text=关联Brief 点击创建 >> div[role="combobox"] div',
        'brief': 'text=ESPN 微信H5页面设计',
        'submit': 'text=提交',
        'edit': 'text=完成可修改',
        'close_brief': '[aria-label="icon-close"] svg',
        'brief_btn': '#rc-root > div.main > div.wrap > div > div.tz-panel-new > div._3BfRI > div._20ehf._2xwFf._1Zdcj '
                     '> div > button > i > svg',
        'confirm_btn': 'text=确 定',
        'feedback_form': 'text=填写反馈表单',
        'proposal': 'text=是否0 / 300 >> textarea',
        'proposal_btn': 'text=Final提案方案上传附件 >> textarea',
        'determine_the_next_stage': 'text=确认进入下一阶段',
        'quotation_approval': 'text=报价审批',
        'deliver_time': '[placeholder="请填写预计交付日期"]',
        'time': 'text=今天',
        'crate_price_btn': '#rc-root > div.main > div.wrap > div > div.tz-panel-new > div:nth-child(3) > div > div > '
                           'div:nth-child(2) > div > div._18V55 > button',
        'select_crate_price_btn': 'div[role="document"] div[role="combobox"] div:has-text("关联报价单")',
        'confirm_price_btn': 'li[role="option"]:has-text("测试一下")',
        'submit_for_approval': 'text=提交审批',
        'associated_quotation': 'text=已关联报价单',
        'look_btn': 'button:has-text("查看")',
        'unbind': 'body > div:nth-child(12) > div > div > div > div.ant-popover-inner > div > div > div > div > '
                  'button:nth-child(2)',
        'more': 'text=更多更多更多更多更多更多更多更多更多更多 >> span',
        'add_member': 'div[role="tooltip"] >> text=添加团队成员',
        'delete_btn': 'text=删除',
        'pipeline': 'text=Pipeline视图',
        'select_box': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div > '
                      'div.ant-table-wrapper.tz-table-inner-handler-7356643902171087 > div > div > div > div > '
                      'div.ant-table-fixed-left > div > div > table > thead > tr > th.ant-table-selection-column > '
                      'span > div > span.ant-table-column-title > div > label > span > input',
        'sale_amount_of_money': 'input[placeholder="金额（元）"]',
        'filling_rules': 'text=Pipeline填写规则',
        'select_department': 'text=请选择公司/部门名称',
        'confirm_department': 'text=测试部门12121',
        'department': 'text=请选择所属部门',
        'select_business_department': 'text=平台业务部',
        'select_business_department_search_result_assert': '#rc-root > div.main > div.wrap > div > div:nth-child(3) > div > div._a3rOK > div:nth-child(1)',
        'select_sku': 'div:nth-child(13) .ant-row .ant-col.ant-col-17 .tui-select-wrap .ant-select-show-arrow .ant-select-selection .ant-select-selection__rendered',
        'select_sku_post': 'text=海报 / kv',
        # 自带的联系人
        'self_contained': '#rc-root > div.main > div.wrap > div > div:nth-child(2) > div > div > div:nth-child(5) > div > div.ant-col.ant-col-17 > div > span > span > ul > li.ant-select-selection__choice > span.ant-select-selection__choice__content',
        'customer_style': 'text=请选择客户类型全部',
        'regular_customers': 'text=老客户机会',
        'new_customer': 'text=新客户机会',
        'relate_quotation': ':nth-match(:text("全部"), 3)',
        'select_yes': 'li[role="option"]:has-text("是")',
        'total': 'text=全部',
        'select_no': 'li[role="option"]:has-text("否")',
        'start_time': '[placeholder="开始日期"]',
        'week': 'text=近一周',
        'month': 'text=本月',
        'three_months': 'text=近三个月',
        'half_a_year': 'text=近半年',
        'last_quarter': 'text=上季度',
        'quarter': 'text=本季度',
        'delivery_time': 'text=预估交付时间 ~ >> [placeholder="开始日期"]',
        'approval_btn': 'text=未找到企业/部门信息，点击发起审批',
        'submit_btn1': ':nth-match(:text("提交"), 2)',
        'record_btn': 'text=快速记录',
        'phone': 'text=电话',
        'visit': 'text=拜访',
        'meeting': 'li[role="option"]:has-text("会议")',
        'plan': 'text=计划Plan',
        'explain': 'textarea',
        'publish': 'text=发布',
        'publish_success_assert': 'text=记录信息 >> li',
        'associated_quotation_btn': 'text=创建/关联报价单',
        'cancel_btn1': 'text=取 消',
        'associated_quotation_btn_assert': 'text=创建/关联报价单',
        'sku_case': '#rc-root > div.main > div.wrap > div > div._3r9u2 > div._3sc1x > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1)',
        'company_introduction_link': '#rc-root > div.main > div.wrap > div > div._3r9u2 > div._3sc1x > div:nth-child(3) > div:nth-child(2) > div > div > a',
        'reference_spi': '#rc-root > div.main > div.wrap > div > div._3r9u2 > div._3sc1x > div:nth-child(3) > div:nth-child(3) > div > div > a',
        'record_message': 'text=记录信息',
        'team': 'text=团队成员',
        'basic_information': 'text=基本资料',
        'all_btn': 'text=全部',
        'meet': 'span:has-text("会议")',
        'plan_assert': '#rc-root > div.main > div.wrap > div > div._3r9u2 > div.tz-panel-new > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div._3EZ8w._34v9S > div._3o3MP > div > label.ant-checkbox-group-item.ant-checkbox-wrapper.ant-checkbox-wrapper-checked > span.ant-checkbox.ant-checkbox-checked > input',
        'add_btn': '#rc-root > div.main > div.wrap > div > div._3r9u2 > div.tz-panel-new > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > h6 > button',
        'more_btn': '#rc-root > div.main > div.wrap > div > div._3r9u2 > div.tz-panel-new > div > div.ant-tabs-bar.ant-tabs-top-bar > div.ant-tabs-extra-content > button > i > svg',
        'company_name': '#rc-root > div.main > div.wrap > div > div._3r9u2 > div.tz-panel-new > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div:nth-child(1) > div._G3nJd > div:nth-child(1) > div:nth-child(1) > p._2KNZ3',
        'estimated_order_forming_date': '#rc-root > div.main > div.wrap > div > div._3r9u2 > div.tz-panel-new > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div:nth-child(1) > div._G3nJd > div:nth-child(1) > div:nth-child(4) > p._2KNZ3',
        'requirements_description_btn': '#rc-root > div.main > div.wrap > div > div._3r9u2 > div.tz-panel-new > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div:nth-child(1) > div._G3nJd > div:nth-child(1) > div:nth-child(2) > p._2KNZ3',
        'pipeline_filling_rules': 'text=Pipeline填写规则',
        'lose_btn': '#rc-root > div.main > div.wrap > div > div.tz-panel-new > div._24fDd > button',
        'lose_reason': 'text=请输入输单原因',
        'price_reason': 'text=价格原因',
        'lose_describe': 'text=输单原因请输入输单原因价格原因输单描述取消确定 >> textarea',
        'determine': 'text=确定',
        # '': '',


    }

    def crm_sale_search(self):
        # # 点击CRM tab
        # self._click(SalePage.selectors["crm_tab"])
        # # 点击销售机会
        # self._click(SalePage.selectors["sale_btn"])
        # 点击更多搜索按钮
        self._click(SalePage.selectors["more_search_btn"])
        # 点击删除销售机会所有人
        self._click(SalePage.selectors["delete_sale_btn"])
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])
        # 选择机会类型
        self._click(SalePage.selectors["select_business_type_btn"])
        self._click(SalePage.selectors["select_content"])
        self._click(SalePage.selectors["input_sale_name"])
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])
        self._wait(1)

    def select_sale(self, input_sale_name):
        # 点击删除销售机会所有人
        # self._click(SalePage.selectors["delete_sale_btn"])
        self._click(SalePage.selectors["input_sale_name"])
        self._fill(SalePage.selectors["input_sale_name"], input_sale_name)
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])

    def sale_amount_of_money(self, sale_amount_of_money):
        # 点击销售金额
        self._click(SalePage.selectors["sale_amount_of_money"])
        self._fill(SalePage.selectors["sale_amount_of_money"], sale_amount_of_money)
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])

    def pipeline(self):
        # 点击CRM tab
        self._click(SalePage.selectors["crm_tab"])
        # 点击销售机会
        self._click(SalePage.selectors["sale_btn"])
        # 点击更多搜索按钮
        self._click(SalePage.selectors["more_search_btn"])
        # 点击删除销售机会所有人
        self._click(SalePage.selectors["delete_sale_btn"])
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])
        # 选择机会类型
        self._click(SalePage.selectors["select_business_type_btn"])
        self._click(SalePage.selectors["select_content"])
        self._click(SalePage.selectors["input_sale_name"])
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])
        self._click(SalePage.selectors["pipeline"])

    # 查看pipeline填写规则
    def filling_rules(self):
        with self.page.expect_popup() as popup_info:
            self.page.click(SalePage.selectors["filling_rules"])
        page6 = popup_info.value
        page6.close()

    # 客户/部门选择
    def department(self):
        # 点击客户/部门选择框
        self._click(SalePage.selectors["select_department"])
        # 选择部门
        self._click(SalePage.selectors["confirm_department"])
        # 点击机会名称输入框
        self._click(SalePage.selectors["input_sale_name"])
        # 点击搜索按钮
        self._click(SalePage.selectors["search_btn"])

    # 所属部门
    def my_department(self):
        # 点击更多筛选按钮
        self._click(SalePage.selectors["more_search_btn"])
        # 点击所属部门
        self._click(SalePage.selectors["department"])
        # 点击客户/部门选择框
        self._click(SalePage.selectors["select_business_department"])
        # 点击机会名称输入框
        self._click(SalePage.selectors["input_sale_name"])
        # 点击搜索按钮
        self._click(SalePage.selectors["search_btn"])

    def relate_sku(self):
        # # 点击CRM tab
        # self._click(SalePage.selectors["crm_tab"])
        # # 点击销售机会
        # self._click(SalePage.selectors["sale_btn"])
        self.delete_contacts()
        # 点击更多筛选按钮
        self._click(SalePage.selectors["more_search_btn"])
        # 点击关联sku
        self._click(SalePage.selectors["select_sku"])
        # 选择海报、sku
        self._click(SalePage.selectors["select_sku_post"])
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])

    # 搜索销售阶段
    def sales_phase(self):
        # # 点击CRM tab
        # self._click(SalePage.selectors["crm_tab"])
        # # 点击销售机会
        # self._click(SalePage.selectors["sale_btn"])
        self.delete_contacts()
        # 点击更多筛选按钮
        self._click(SalePage.selectors["more_search_btn"])
        # 选择客户类型
        self._click(SalePage.selectors["customer_style"])
        # 选择新客户
        self._click(SalePage.selectors["new_customer"])
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])

    # 搜索关联报价单
    def relate_quotation(self):
        # 点击CRM tab
        self._click(SalePage.selectors["crm_tab"])
        # 点击销售机会
        self._click(SalePage.selectors["sale_btn"])
        self.delete_contacts()
        # 点击更多筛选按钮
        self._click(SalePage.selectors["more_search_btn"])
        # 选择关联报价单
        self._click(SalePage.selectors["relate_quotation"])
        # 选择是
        self._click(SalePage.selectors["select_yes"])
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])

    # 搜索关联报价单
    def pending(self):
        self.delete_contacts()
        # 点击更多筛选按钮
        self._click(SalePage.selectors["more_search_btn"])
        # 选择关联报价单
        self._click(SalePage.selectors["total"])
        # 选择否
        self._click(SalePage.selectors["select_no"])
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])

    # 搜索创建时间
    def start_time(self):
        self.delete_contacts()
        # 点击创建时间
        self._click(SalePage.selectors["start_time"])
        self._hover(SalePage.selectors["week"])
        self._hover(SalePage.selectors["month"])
        self._hover(SalePage.selectors["three_months"])
        self._hover(SalePage.selectors["half_a_year"])
        self._hover(SalePage.selectors["last_quarter"])
        self._hover(SalePage.selectors["quarter"])
        self._click(SalePage.selectors["week"])
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])

    # 搜索预估交付时间
    def delivery_time(self):
        self.delete_contacts()
        # 点击更多筛选按钮
        self._click(SalePage.selectors["more_search_btn"])
        # 点击预估交付时间
        self._click(SalePage.selectors["delivery_time"])
        self._hover(SalePage.selectors["week"])
        self._hover(SalePage.selectors["month"])
        self._hover(SalePage.selectors["three_months"])
        self._hover(SalePage.selectors["half_a_year"])
        self._hover(SalePage.selectors["last_quarter"])
        self._hover(SalePage.selectors["quarter"])
        self._click(SalePage.selectors["month"])
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])

    # 新建销售机会
    def crm_create(self, select_company_name, input_name_btn, requirements_description, input_estimate_price,
                   input_cost):
        # 点击新建销售机会按钮
        self._click(SalePage.selectors["create_sale_btn"])
        # 点击企业名称
        self._click(SalePage.selectors["select_company_btn"])
        # 输入企业名称
        self._fill(SalePage.selectors['select_company_name'], select_company_name)
        self._click(SalePage.selectors["select_company"])
        # 点击机会名称
        self._click(SalePage.selectors["input_name_btn"])
        # 输入机会名称
        self._fill(SalePage.selectors['input_name_btn'], input_name_btn)
        # 点击机会描述
        self._click(SalePage.selectors["requirements_description"])
        # 输入机会描述
        self._type(SalePage.selectors['requirements_description'], requirements_description)
        # 点击客户意向SKU
        self._click(SalePage.selectors["select_SKU"])
        # 选择海报
        self._click(SalePage.selectors["select_port"])
        # 选择客户部门
        self._click(SalePage.selectors["select_customer"])
        # 确认客户部门
        self._click(SalePage.selectors["confirm_select_customer"])
        # 选择客户首次联系人
        self._click(SalePage.selectors["customer_contact_btn"])
        # 确认客户首次联系人
        self._click(SalePage.selectors["confirm_customer_contact_btn"])
        # # 选择客户类型
        # self._click(SalePage.selectors["customer_type"])
        # # 确认客户类型
        # self._click(SalePage.selectors["confirm_customer_type"])
        # 点击预估销售金额
        self._click(SalePage.selectors["input_estimate_price"])
        # 输入预估销售金额
        self._fill(SalePage.selectors['input_estimate_price'], input_estimate_price)
        # 点击预估成本
        self._click(SalePage.selectors["input_cost"])
        # 输入预估项目成本
        self._fill(SalePage.selectors['input_cost'], input_cost)
        # 点击预估成单日期
        self._click(SalePage.selectors["input_estimate_date"])
        # 确定预估成单日期
        self._click(SalePage.selectors["confirm_estimate_date"])
        # 点击预估交付日期
        self._click(SalePage.selectors["estimated_delivery_date"])
        # 确定交付日期
        self._click(SalePage.selectors["confirm_estimated_delivery_date"])
        # 点击提交按钮
        self._click(SalePage.selectors["submit_btn"])

    # 点击快速记录
    def fast_record(self, explain):
        # 点击新建的销售机会
        with self.page.expect_popup() as popup_info:
            self._click(SalePage.selectors["edit_sale"])
        page11 = popup_info.value
        page11.click(SalePage.selectors["record_btn"])
        page11.click(SalePage.selectors["phone"])
        page11.click(SalePage.selectors["phone"])
        page11.click(SalePage.selectors["visit"])
        page11.click(SalePage.selectors["visit"])
        page11.click(SalePage.selectors["plan"])
        page11.click(SalePage.selectors["explain"])
        page11.type(SalePage.selectors["explain"], explain)
        # 点击发布记录
        page11.click(SalePage.selectors["publish"])
        page11.close()

    # 点击销售建议
    def sales_advice(self):
        with self.page.expect_popup() as popup_info:
            self._click(SalePage.selectors["edit_sale"])
        page12 = popup_info.value
        # 点击创建、关联报价单
        page12.click(SalePage.selectors["associated_quotation_btn"])
        # 点击取消按钮
        page12.click(SalePage.selectors["cancel_btn1"])
        with page12.expect_popup() as popup_info:
            page12.click(SalePage.selectors["sku_case"])
        page13 = popup_info.value
        page13.close()
        # 点击准准找人
        with page12.expect_popup() as popup_info:
            page12.click(":nth-match(:text(\"准准找人\"), 2)")
        page14 = popup_info.value
        page14.close()
        page12.close()

    # 在销售机会详情页面，点击知识库
    def knowledge_base(self):
        with self.page.expect_popup() as popup_info:
            self._click(SalePage.selectors["edit_sale"])
        page15 = popup_info.value
        with page15.expect_popup() as popup_info:
            page15.click(SalePage.selectors["company_introduction_link"])
        page16 = popup_info.value
        page16.close()
        with page15.expect_popup() as popup_info:
            page15.click(SalePage.selectors["reference_spi"])
        page17 = popup_info.value
        page17.close()
        page15.close()

    # 在销售机会详情页面，点击基本资料，记录信息，团队成员
    def sale_detail_record(self):
        self.delete_contacts()
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])
        with self.page.expect_popup() as popup_info:
            self._click(SalePage.selectors["edit_sale"])
        page18 = popup_info.value
        # 点击记录信息
        page18.click(SalePage.selectors["record_message"])
        # 点击团队成员
        page18.click(SalePage.selectors["team"])
        # 点击基本资料
        page18.click(SalePage.selectors["basic_information"])
        page18.close()

    # 在销售机会详情页面，点击记录信息
    def message_record(self):
        self.delete_contacts()
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])
        with self.page.expect_popup() as popup_info:
            self._click(SalePage.selectors["edit_sale"])
        page19 = popup_info.value
        page19.click(SalePage.selectors["record_message"])
        # 点击操作记录全部
        page19.click(SalePage.selectors["all_btn"])
        page19.click(SalePage.selectors["meet"])
        page19.click(SalePage.selectors["meet"])
        page19.check(SalePage.selectors["plan"])
        checked = page19.is_checked(SalePage.selectors["plan_assert"])
        assert checked
        page19.close()

    # 在销售机会详情页面，点击团队成员
    def team(self):
        self.delete_contacts()
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])
        with self.page.expect_popup() as popup_info:
            self._click(SalePage.selectors["edit_sale"])
        page20 = popup_info.value
        page20.click(SalePage.selectors["team"])
        page20.click(SalePage.selectors["add_btn"])
        page20.click(SalePage.selectors["cancel_btn"])
        page20.close()

    # 在销售机会详情页面，点击团队成员
    def basic_information(self):
        self.delete_contacts()
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])
        with self.page.expect_popup() as popup_info:
            self._click(SalePage.selectors["edit_sale"])
        page21 = popup_info.value
        # 点击基本资料
        page21.click(SalePage.selectors["basic_information"])
        # 鼠标悬浮更多按钮
        page21.hover(SalePage.selectors["more_btn"])
        page21.close()

    # 在销售机会详情页面，点击基本资料各个编辑按钮
    def basic_information_detail(self):
        self.delete_contacts()
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])
        with self.page.expect_popup() as popup_info:
            self._click(SalePage.selectors["edit_sale"])
        page22 = popup_info.value
        # 点击企业名称
        page22.click(SalePage.selectors["company_name"])
        # 点击编辑企业名称弹窗取消按钮
        page22.click(SalePage.selectors["cancel_btn"])
        # 点击预计成单日期
        page22.click(SalePage.selectors["estimated_order_forming_date"])
        # 点击预计成单日期弹窗取消按钮
        page22.click(SalePage.selectors["cancel_btn"])
        # 点击需求描述
        page22.click(SalePage.selectors["requirements_description_btn"])
        # 点击需求描述弹窗取消按钮
        page22.click(SalePage.selectors["cancel_btn"])
        page22.close()

    # 在销售机会详情页面，点击pipeline填写规则
    def pipeline_filling_rules(self):
        self.delete_contacts()
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])
        with self.page.expect_popup() as popup_info:
            self._click(SalePage.selectors["edit_sale"])
        page23 = popup_info.value
        with page23.expect_popup() as popup_info:
            page23.click(SalePage.selectors["pipeline_filling_rules"])
        page24 = popup_info.value
        page24.close()
        page23.close()

    def crm_cancel(self):
        # 点击新建销售机会按钮
        self._click(SalePage.selectors["create_sale_btn"])
        # 点击取消按钮
        self._click(SalePage.selectors["cancel_btn"])

    # 点击审批
    def approval(self):
        # 点击新建销售机会按钮
        self._click(SalePage.selectors["create_sale_btn"])
        # 点击审批按钮
        self._click(SalePage.selectors["approval_btn"])
        # 点击提交按钮
        self._click(SalePage.selectors["submit_btn1"])

    # 绑定brief
    def crm_brief(self):
        # 点击新建的销售机会
        with self.page.expect_popup() as popup_info:
            self._click(SalePage.selectors["edit_sale"])
        page2 = popup_info.value
        # 点击创建、编辑brief
        page2.click(SalePage.selectors["edit_brief"])
        # 点击关联brief
        page2.click(SalePage.selectors["relation_brief"])
        # 关联brief
        page2.click(SalePage.selectors["brief"])
        # 点击提交按钮
        page2.click(SalePage.selectors["submit"])
        # 点击完成修改brief
        page2.click(SalePage.selectors["edit"])
        # 点击取消绑定brief
        page2.click(SalePage.selectors["close_brief"])
        page2.close()

    def crm_edit_brief(self, proposal, proposal_btn):
        # 点击新建的销售机会
        with self.page.expect_popup() as popup_info:
            self._click(SalePage.selectors["edit_sale"])
        page3 = popup_info.value
        # 点击创建、编辑brief
        page3.click(SalePage.selectors["edit_brief"])
        # 点击关联brief
        page3.click(SalePage.selectors["relation_brief"])
        # 关联brief
        page3.click(SalePage.selectors["brief"])
        # 点击提交按钮
        page3.click(SalePage.selectors["submit"])
        # 点击改变brief按钮
        page3.click(SalePage.selectors["brief_btn"])
        # 点击确定按钮
        page3.click(SalePage.selectors["confirm_btn"])
        # 点击反馈表单
        page3.click(SalePage.selectors["feedback_form"])
        # 点击提案输入框
        page3.click(SalePage.selectors["proposal"])
        page3.type(SalePage.selectors["proposal"], proposal)
        page3.click(SalePage.selectors["proposal_btn"])
        page3.type(SalePage.selectors["proposal_btn"], proposal_btn)
        # 点击下一步阶段
        page3.click(SalePage.selectors["determine_the_next_stage"])
        # 点击创建关联报价单按钮
        page3.click(SalePage.selectors["crate_price_btn"])
        # 选择报价单
        page3.click(SalePage.selectors["select_crate_price_btn"])
        # 选择测试报价单
        page3.click(SalePage.selectors["confirm_price_btn"])
        # 点击确定按钮
        page3.click(SalePage.selectors["confirm_btn"])
        # 点击报价审批按钮
        page3.click(SalePage.selectors["quotation_approval"])
        # 点击交付日期
        page3.click(SalePage.selectors["deliver_time"])
        # 交付日期选择今天
        page3.click(SalePage.selectors["time"])
        # # 点击提交审批按钮  预发环境没有飞书
        # page3.click(SalePage.selectors["submit_for_approval"])

    # 编辑报价单
    def crm_edit_quotation(self):
        # 点击新建的销售机会
        with self.page.expect_popup() as popup_info:
            self._click(SalePage.selectors["edit_sale"])
        page4 = popup_info.value
        # 鼠标悬浮已关联的报价单
        page4.hover(SalePage.selectors["associated_quotation"])
        # 鼠标点击查看报价单按钮
        with page4.expect_popup() as popup_info:
            page4.click(SalePage.selectors["look_btn"])
        page5 = popup_info.value
        page5.close()
        page4.hover(SalePage.selectors["associated_quotation"])
        # 点击解绑按钮
        page4.click(SalePage.selectors["unbind"])
        # 点击确定解绑按钮
        page4.click(SalePage.selectors["confirm_btn"])
        page4.close()

    # 删除销售机会
    def crm_edit_operation(self):
        # 点击删除销售机会所有人
        self._click(SalePage.selectors["delete_sale_btn"])
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])
        self._hover(SalePage.selectors["more"])
        # 点击添加成员按钮
        self._click(SalePage.selectors["add_member"])
        # 点击取消按钮
        self._click(SalePage.selectors["cancel_btn"])
        # 悬浮更多按钮
        self._hover(SalePage.selectors["more"])
        # 点击删除按钮
        self._click(SalePage.selectors["delete_btn"])
        # 确定删除销售机会
        self._click(SalePage.selectors["confirm_btn"])

    # 因打开销售机会页面，会自动带销售机会联系人，先做个判断
    def delete_contacts(self):
        """若页面自动带销售机会联系人，则点击删除按钮,进行删除"""
        self.page.wait_for_load_state('networkidle')
        # self._wait(1)
        if self.page.get_attribute(SalePage.selectors['self_contained'], "value") == "张建波":
            pass
        else:
            self._click(SalePage.selectors["delete_sale_btn"])

    # 在销售机会详情页面，点击pipeline填写规则
    def crm_create_lose(self, lose_describe):
        self.goto("https://top.tezign.com/#/app/salesOpportunity")
        self.delete_contacts()
        # 点击搜索按钮
        with self.page.expect_navigation():
            self._click(SalePage.selectors["search_btn"])
        with self.page.expect_popup() as popup_info:
            self._click(SalePage.selectors["edit_sale"])
        page25 = popup_info.value
        page25.click(SalePage.selectors["lose_btn"])
        # 选择输单原因
        page25.click(SalePage.selectors["lose_reason"])
        page25.click(SalePage.selectors["price_reason"])
        page25.click(SalePage.selectors["lose_describe"])
        # 输入输单原因
        page25.type(SalePage.selectors["lose_describe"], lose_describe)
        page25.click(SalePage.selectors["determine"])





