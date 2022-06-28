#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/3/4 10:46 上午
# @File : SpecialDiscoveryPage.py
from pages.express.ExpressBasePage import ExpressBasePage


class SpecialDiscoveryPage(ExpressBasePage):
    selectors = {
        "special_discovery_btn": "#root > header > div > div.expressNavBarInnerLeft___3vZnM > nav > ul > li:nth-child(2)",
        "banner_left_btn": "#root > div > div > div > div.ant-carousel > div > div.slick-arrow.slick-prev",
        "banner_right_btn": "#root > div > div > div > div.ant-carousel > div > div.slick-arrow.slick-next",
        "banner_picture": "#root > div > div > div > div.ant-carousel > div > div.slick-list > div > div.slick-slide.slick-active.slick-current > div > div > div",
        "special_discovery_back": "#root > div > div > div > div > div.bread-crumb___36_XR.bread-crumb___1DOQO > span:nth-child(1)",
        "selected_cases_more": "#root > div > div > div > div:nth-child(2) > div:nth-child(1) > div.align-between___2VWD8 > div.view-all-btn___VkFrp",
        "give_the_thumbs_up": "#root > div > div > div > div:nth-child(2) > div:nth-child(1) > div.content___1HQQB > div > div:nth-child(1) > div.bottom___3Arsv > div:nth-child(2) > i",
        "company_logo": "#root > div > div > div > div:nth-child(2) > div:nth-child(1) > div.content___1HQQB > div > div:nth-child(1) > div.bottom___3Arsv > div.brand-list___2o4tO > img",
        "inquiry_immediately": "#root > div > div > div > div.count_wrap___3q4MP > div:nth-child(2) > button",
        "cancel_btn": "body > div:nth-child(11) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > div > button.tz-btn.type-neutral.shape-round.ghost-text",
        "cases": "#root > div > div > div > div.case_list___3bvBG > div:nth-child(2) > div:nth-child(1) > div > div.case_card_item_top___3RuyN.inner_content > div > div",
        "give_the_thumbs_up_btn": "#root > div > div > div > div > div > div.box-wrapper___SbJv6 > div > div.share_case_box_content___J4Bvo > div > div:nth-child(1) > div > div.title_extra___2PZhU > div > i",
        "inquiry_immediately_btn": "#root > div > div > div > div > div > div.box-wrapper___SbJv6 > div > div.share_case_box_aside___18jqC > div > button",
        "cancel": "body > div:nth-child(11) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > div > button.tz-btn.type-neutral.shape-round.ghost-text",
        "view": "#root > div > div > div > div.row___SIBHH.section___s6vKD > div.section___QT3eG.section___1iffr > div:nth-child(1) > div.align-between___2VWD8.sub-title-area___AuuBg > div.view-all-btn___VkFrp",
        "view_more": "#root > div > div > div > div.row___SIBHH.section___s6vKD > div.section___QT3eG.section___340Au > div:nth-child(1) > div.align-between___2VWD8.sub-title-area___AuuBg > div.view-all-btn___VkFrp",
        "view_detail": "#root > div > div > div > div.section___QT3eG.section___1OMgA > div.content___1HQQB > div > div.left___1UpfZ > button",
        "go_now": "#root > div > div > div > div.body___3FSJq > div.qualityContentBanner___1YBQk > div.qualityContentLeft___lToKj > div.qclTitle___1oCLX > div.qclTitleBtn___2nt1A > button",
        "category_btn": "#root > div > div > div > div.label-area___3yBzc > div.label-list___1Pgk3 > div:nth-child(1)",
        "festival": "#root > div > div > div > div.label-area___3yBzc > div.label-list___1Pgk3 > div:nth-child(2)",
        "hotspot": "#root > div > div > div > div.label-area___3yBzc > div.label-list___1Pgk3 > div:nth-child(3)",
        "industry": "#root > div > div > div > div.label-area___3yBzc > div.label-list___1Pgk3 > div:nth-child(1)",
        "website": "#root > div > div > div > div.label-area___3yBzc > div.sub-label-list___11y2r > button:nth-child(2)",
        "H5": "#root > div > div > div > div.label-area___3yBzc > div.sub-label-list___11y2r > button:nth-child(3)",
        "spring_festival": "#root > div > div > div > div.label-area___3yBzc > div.sub-label-list___11y2r > button.tz-btn.sub-label-btn___26Vbt.type-neutral.shape-round",
        "christmas": "#root > div > div > div > div.label-area___3yBzc > div.sub-label-list___11y2r > button.tz-btn.sub-label-btn___26Vbt.type-neutral.shape-round",
        "click_fabulous": "#root > div > div > div > div:nth-child(6) > div.spin-wrap.size-default > div.spin-container > div > div > div:nth-child(1) > div > div.bottom___3Arsv > div:nth-child(2) > i > svg",
        "christmas_fabulous": "#root > div > div > div > div:nth-child(6) > div > div.spin-container > div > div > div:nth-child(1) > div > div.bottom___3Arsv > div:nth-child(2) > i > svg",
        "olympic": "#root > div > div > div > div.label-area___3yBzc > div.sub-label-list___11y2r > button.tz-btn.sub-label-btn___26Vbt.type-neutral.shape-round",
        "national_tide": "#root > div > div > div > div.label-area___3yBzc > div.sub-label-list___11y2r > button.tz-btn.sub-label-btn___26Vbt.type-neutral.shape-round",
        "national_tide_fabulous": "#root > div > div > div > div:nth-child(6) > div.spin-wrap.size-default > div.spin-container > div > div > div:nth-child(5) > div > div.bottom___3Arsv > div:nth-child(2) > i > svg",
        "more_btn": ':nth-match(:text("查看全部"), 2)',
        "order_consult": "#root > div > div > div > div.count_wrap___3q4MP > div:nth-child(2) > button",
        "order_cancel": "body > div:nth-child(11) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > div > button.tz-btn.type-neutral.shape-round.ghost-text",
        "national_tide_img": "text=5.10国潮来了海报设计",
        "click_fabulous_btn": '#root > div > div > div > div > div > div.box-wrapper___SbJv6 > div > div.share_case_box_content___J4Bvo > div > div:nth-child(1) > div > div.title_extra___2PZhU > div > i',
        "cancel_fabulous_btn": '#root > div > div > div > div > div > div.box-wrapper___SbJv6 > div > div.share_case_box_content___J4Bvo > div > div:nth-child(1) > div > div.title_extra___2PZhU > div > i > svg',
        "order_consult_btn": "#root > div > div > div > div > div > div.box-wrapper___SbJv6 > div > div.share_case_box_aside___18jqC > div > button",
        "order_cancel_btn": "body > div:nth-child(11) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > div > button.tz-btn.type-neutral.shape-round.ghost-text",
        "internet": "#root > div > div > div > div.label-area___3yBzc > div.sub-label-list___11y2r > button:nth-child(2)",
        "fast_elimination": "#root > div > div > div > div.label-area___3yBzc > div.sub-label-list___11y2r > button:nth-child(3)",
        "food_and_beverage": "#root > div > div > div > div.label-area___3yBzc > div.sub-label-list___11y2r > button:nth-child(5)",
        "financial_real_estate": "#root > div > div > div > div.label-area___3yBzc > div.sub-label-list___11y2r > button:nth-child(4)",
        "beauty_makeup": "#root > div > div > div > div.label-area___3yBzc > div.sub-label-list___11y2r > button:nth-child(8)",
        "medical_health": "#root > div > div > div > div.label-area___3yBzc > div.sub-label-list___11y2r > button:nth-child(6)",
        "input_search1": 'input[placeholder="搜索服务或案例tf"]',
        'input_search': 'xpath=//*[@id="root"]/header/div/div[2]/div[1]/input',
        "expand_all": "text=展开全部",
        "put_away": "text=收起服务",
        "shopping_cart": "#root > div > div > div > div.content-wrapper___2zVJo > div:nth-child(2) > div:nth-child(1) > div.lists___QMlm6 > div:nth-child(1) > div.item_footer___2pxGU > button > i > svg",
        "inquiry": "#root > div > div > div > div.content-wrapper___2zVJo > div:nth-child(2) > div:nth-child(1) > div.lists___QMlm6 > div:nth-child(1) > div.item_footer___2pxGU > div > div > span.item_footer_price_num_green___2n53K",
        "call_off": "text=取 消",
        "input_title": 'input[placeholder="请输入文字，最多30个汉字"]',

    }

    def discovery_page(self):
        # 点击特赞发现
        self.page.click(SpecialDiscoveryPage.selectors['special_discovery_btn'])
        # 点击轮播图右侧按钮
        self.page.click(SpecialDiscoveryPage.selectors['banner_right_btn'])
        # 点击轮播图右侧按钮
        self.page.click(SpecialDiscoveryPage.selectors['banner_left_btn'])
        self.page.click(SpecialDiscoveryPage.selectors['banner_left_btn'])
        # 点击轮播图，进入详情页面
        with self.page.expect_popup() as popup_info:
            self.page.click(SpecialDiscoveryPage.selectors['banner_picture'])
        page1 = popup_info.value
        page1.click(SpecialDiscoveryPage.selectors['special_discovery_back'])
        page1.close()

    def discovery_page_selected_cases(self):
        # 鼠标悬浮企业logo
        self.page.hover(SpecialDiscoveryPage.selectors['company_logo'])
        # 点赞案例
        self.page.click(SpecialDiscoveryPage.selectors['give_the_thumbs_up'])
        self.page.click(SpecialDiscoveryPage.selectors['give_the_thumbs_up'])

    def selected_cases(self):
        # 点击案例查看全部
        with self.page.expect_popup() as popup_info:
            self.page.click(SpecialDiscoveryPage.selectors['selected_cases_more'])
        page2 = popup_info.value
        # 点击立即询价
        page2.click(SpecialDiscoveryPage.selectors['inquiry_immediately'])
        # 点击点击取消下单按钮
        page2.click(SpecialDiscoveryPage.selectors['cancel_btn'])
        # 点击案例
        with page2.expect_popup() as popup_info:
            page2.click(SpecialDiscoveryPage.selectors['cases'])
        page3 = popup_info.value
        page3.goto("https://express.tezign.com/platform/share-case?id=41769")
        self._wait(3)
        page3.click(SpecialDiscoveryPage.selectors['give_the_thumbs_up_btn'])
        page3.click(SpecialDiscoveryPage.selectors['give_the_thumbs_up_btn'])
        page3.click(SpecialDiscoveryPage.selectors['inquiry_immediately_btn'])
        page3.click(SpecialDiscoveryPage.selectors['cancel'])
        page3.close()
        page2.close()

    # 特赞发现，研究院
    def creative_research_institute(self):
        # 点击特赞发现
        self.page.click(SpecialDiscoveryPage.selectors['special_discovery_btn'])
        # 点击特赞创意研究院查看全部
        with self.page.expect_popup() as popup_info:
            self.page.click(SpecialDiscoveryPage.selectors['view'])
        page4 = popup_info.value
        # 点击立即前往
        page4.click(SpecialDiscoveryPage.selectors['go_now'])
        page4.close()

        # 点击特赞特赞学院查看全部
        with self.page.expect_popup() as popup_info:
            self.page.click(SpecialDiscoveryPage.selectors['view'])
        page5 = popup_info.value
        page5.goto("https://express.tezign.com/platform/tezign-academy?id=3552")
        # 点击立即前往
        page5.click(SpecialDiscoveryPage.selectors['go_now'])
        page5.close()

        # 点击特赞特赞学院查看全部
        with self.page.expect_popup() as popup_info:
            self.page.click(SpecialDiscoveryPage.selectors['view_detail'])
        page6 = popup_info.value
        page6.close()

    # 特赞发现页，案例分类
    def classification(self):
        # 点击特赞发现
        self.page.click(SpecialDiscoveryPage.selectors['special_discovery_btn'])
        # 点击节日Tab
        self.page.click(SpecialDiscoveryPage.selectors['festival'])
        # 点击品类Tab
        self.page.click(SpecialDiscoveryPage.selectors['category_btn'])
        # 点击热点Tab
        self.page.click(SpecialDiscoveryPage.selectors['hotspot'])

    # 特赞发现页，案例二级分类
    def classification_second_level(self):
        # 点击特赞发现
        self.page.click(SpecialDiscoveryPage.selectors['special_discovery_btn'])
        # 点击品类Tab
        self.page.click(SpecialDiscoveryPage.selectors['category_btn'])
        # 点击网站
        self.page.click(SpecialDiscoveryPage.selectors['website'])
        # 点击H5
        self.page.click(SpecialDiscoveryPage.selectors['H5'])
        # 点击节日
        self.page.click(SpecialDiscoveryPage.selectors['festival'])
        # 点击春节
        self.page.click(SpecialDiscoveryPage.selectors['spring_festival'])
        # 点赞，取消点赞
        self.page.click(SpecialDiscoveryPage.selectors['click_fabulous'])
        self.page.click(SpecialDiscoveryPage.selectors['click_fabulous'])
        # 点击圣诞节
        self.page.click(SpecialDiscoveryPage.selectors['christmas'])
        self._wait(2)
        self.page.click(SpecialDiscoveryPage.selectors['christmas_fabulous'])
        self.page.click(SpecialDiscoveryPage.selectors['christmas_fabulous'])
        # 点击热点Tab
        self.page.click(SpecialDiscoveryPage.selectors['hotspot'])
        # 点击奥运
        self.page.click(SpecialDiscoveryPage.selectors['olympic'])
        # 点击国潮
        self.page.click(SpecialDiscoveryPage.selectors['national_tide'])
        self.page.click(SpecialDiscoveryPage.selectors['national_tide_fabulous'])
        self.page.click(SpecialDiscoveryPage.selectors['national_tide_fabulous'])
        # 点击国潮查看更多
        # with self.page.expect_popup() as popup_info:
        #     self.page.click(SpecialDiscoveryPage.selectors['more_btn'])
        # page7 = popup_info.value
        # page7.click(SpecialDiscoveryPage.selectors['order_consult'])
        # page7.click(SpecialDiscoveryPage.selectors['order_cancel'])
        # 点击"5.10国潮来了海报设计"
        with self.page.expect_popup() as popup_info:
            self.page.click(SpecialDiscoveryPage.selectors['national_tide_img'])
        page8 = popup_info.value
        self._wait(3)
        # page8.goto("https://express.tezign.com/platform/share-case?id=28395")
        page8.click(SpecialDiscoveryPage.selectors['click_fabulous_btn'])
        page8.click(SpecialDiscoveryPage.selectors['cancel_fabulous_btn'])
        # page7.close()
        page8.close()
        # # 点击行业Tab
        # self.page.click(SpecialDiscoveryPage.selectors['industry'])
        # # 点击互联网
        # self.page.click(SpecialDiscoveryPage.selectors['internet'])
        # # 点击医疗健康
        # self.page.click(SpecialDiscoveryPage.selectors['medical_health'])
        # # 点击快消
        # self.page.click(SpecialDiscoveryPage.selectors['fast_elimination'])
        # # 点击食品饮料
        # self.page.click(SpecialDiscoveryPage.selectors['food_and_beverage'])
        # # 点击金融房地产
        # self.page.click(SpecialDiscoveryPage.selectors['financial_real_estate'])
        # # 点击美妆
        # self.page.click(SpecialDiscoveryPage.selectors['beauty_makeup'])

    def input_search(self, input_search):
        # 点击特赞发现
        self.page.click(SpecialDiscoveryPage.selectors['special_discovery_btn'])
        # 点击发现页面搜索框
        self.page.click(SpecialDiscoveryPage.selectors['input_search'])
        self.page.fill(SpecialDiscoveryPage.selectors['input_search'], input_search)
        self.page.press(SpecialDiscoveryPage.selectors['input_search'], "Enter")
        self.page.click(SpecialDiscoveryPage.selectors['expand_all'])
        self.page.click(SpecialDiscoveryPage.selectors['put_away'])
        self.page.click(SpecialDiscoveryPage.selectors['inquiry'])
        self.page.click(SpecialDiscoveryPage.selectors['input_title'])
        self.page.click(SpecialDiscoveryPage.selectors['call_off'])
        self.page.hover(SpecialDiscoveryPage.selectors['shopping_cart'])




