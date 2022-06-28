#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: jianbo
# @Time: 2022/3/1 4:07 下午
# @File : HomePage.py

from pages.express.ExpressBasePage import ExpressBasePage


class HomePage(ExpressBasePage):
    selectors = {
        "marketing_scenario": "#root > div > div > div > div.wrap___2Hpa2 > div.sku_list___2DoAd.tz-responsive-view > div.label-wrapper___e_LYG > div > div > div > div:nth-child(2) > span",
        "creative_video": "#root > div > div > div > div.wrap___2Hpa2 > div.container___1DLfY > div > div > "
                          "div.label-list___EULHO.tz-responsive-view > div:nth-child(2) > div",
        "boutique_ip": "#root > div > div > div > div.wrap___2Hpa2 > div.container___1DLfY > div > div > "
                       "div.label-list___EULHO.tz-responsive-view > div:nth-child(3) > div",
        "hot_festivals": "#root > div > div > div > div.wrap___2Hpa2 > div.container___1DLfY > div > div > "
                         "div.label-list___EULHO.tz-responsive-view > div:nth-child(4) > div",
        "explosion_strategy": "#root > div > div > div > div.wrap___2Hpa2 > div.container___1DLfY > div > div > "
                              "div.label-list___EULHO.tz-responsive-view > div:nth-child(5) > div",
        "industry": "#root > div > div > div > div.wrap___2Hpa2 > div.container___1DLfY > div > div > "
                    "div.label-list___EULHO.tz-responsive-view > div:nth-child(7) > div",
        "recommend_for_you": "#root > div > div > div > div.wrap___2Hpa2 > div.container___1DLfY > div > div > "
                             "div.label-list___EULHO.tz-responsive-view > div:nth-child(8) > div",
        "double_micro": "#root > div > div > div > div.wrap___2Hpa2 > div.container___1DLfY > div > div > "
                        "div.label-list___EULHO.tz-responsive-view > div:nth-child(6) > div",
        "all_materials": "#root > div > div > div > div.wrap___2Hpa2 > div.sku_list___2DoAd.tz-responsive-view > "
                         "div.label-wrapper___e_LYG > div > div > div > div:nth-child(2)",
        # 平面插画
        "plane_illustration": "#root > div > div > div > div.wrap___2Hpa2 > div.sku_list___2DoAd.tz-responsive-view > div.label-wrapper___e_LYG > div > div.slideList-wrapper > div > div:nth-child(3)",
        "popular_recommendation": "#root > div > div > div > div.wrap___2Hpa2 > "
                                  "div.sku_list___2DoAd.tz-responsive-view > div.label-wrapper___e_LYG > div > div > "
                                  "div > div.label-card____8TdK.selected-label___3i0Lt",
        "enterprise_wechat": "#toolitembar > a.toolitembar-wechat > div",
        "customer_service_email": "#toolitembar > a.toolitembar-email > div",
        "online_service": "#toolitembar > a.toolitembar-im > div",
        "independent_release": "#toolitembar > a.toolitembar-support > div",
        "search": 'input[placeholder="搜索服务或案例"]',
        "search_btn": "#root > div > div > div > div.wrap___28j0G > div > div > div.leftContainer___N4dRX > "
                      "div:nth-child(3) > div.search-btn-wrapper___5RhVP > button",
        "search_give_the_thumbs_up": "#root > div > div > div > div.content-wrapper___2zVJo > div:nth-child(2) > div "
                                     "> div.lists___QMlm6 > div:nth-child(1) > div.bottom___3Arsv > div:nth-child(2) "
                                     "> i",
        "search_enterprise_logo": "#root > div > div > div > div.content-wrapper___2zVJo > div:nth-child(2) > div > "
                                  "div.lists___QMlm6 > div:nth-child(1) > div.bottom___3Arsv > div.brand-list___2o4tO "
                                  "> img",
        "case_btn": "#root > div > div > div > div.content-wrapper___2zVJo > div:nth-child(2) > div > "
                    "div.lists___QMlm6 > div:nth-child(6) > div.top___2OZh0 > div > div > div",
        "case_give_the_thumbs_up": '#root > div > div > div > div > div > div.box-wrapper___SbJv6 > div > '
                                   'div.share_case_box_content___J4Bvo > div > div:nth-child(1) > div > '
                                   'div.title_extra___2PZhU > div > i',
        "consult_immediately": "#root > div > div > div > div > div > div.box-wrapper___SbJv6 > div > "
                               "div.share_case_box_aside___18jqC > div > button",
        "case_order": 'input[placeholder="请输入文字，最多30个汉字"]',
        "case_order_textarea": ".desc___ubfBC",
        "confirm_btn": 'div[role="document"] button:has-text("立即咨询")',
        "short_video": "#root > div > div > div > div.wrap___28j0G > div > div > div.leftContainer___N4dRX > "
                       "div.keyword_list___QLa2B > div > div:nth-child(1)",
        "creative_mall": "#root > div > div > div > div.content-wrapper___2zVJo > "
                         "div.search_content_inner_back___2838p > div > span:nth-child(1) > span",
        "short_video_give_thumbs_up": "#root > div > div > div > div.content-wrapper___2zVJo > div:nth-child(2) > "
                                      "div:nth-child(2) > div.lists___QMlm6 > div:nth-child(1) > div.bottom___3Arsv >"
                                      " div:nth-child(2) > i",
        "short_video_give_thumbs": '[aria-label="icon-heart-hover"] path',
        "illustration": "#root > div > div > div > div.wrap___28j0G > div > div > div.leftContainer___N4dRX > "
                        "div.keyword_list___QLa2B > div > div:nth-child(2)",
        "illustration_Shopping_cart": "#root > div > div > div > div.content-wrapper___2zVJo > div:nth-child(2) > "
                                      "div:nth-child(1) > div.lists___QMlm6 > div:nth-child(1) > "
                                      "div.item_footer___2pxGU > button",
        "simple": "body > div:nth-child(11) > div > div > div > div.ant-popover-inner > div > div > div > "
                  "div:nth-child(2) > div > div:nth-child(1) > div",
        "secondary": "body > div:nth-child(11) > div > div > div > div.ant-popover-inner > div > div > div > "
                     "div:nth-child(2) > div > div:nth-child(2) > div",
        "complex": "body > div:nth-child(11) > div > div > div > div.ant-popover-inner > div > div > div > "
                   "div:nth-child(2) > div > div:nth-child(3) > div",
        "quantity": 'body > div:nth-child(11) > div > div > div > div.ant-popover-inner > div > div > div > '
                    'div:nth-child(3) > div > div > div.ant-input-number-input-wrap > input',
        "order": "body > div:nth-child(11) > div > div > div > div.ant-popover-inner > div > div > div > "
                 "div.sls_mini_buttons___2YWxR > button",
        "confirm": "body > div:nth-child(12) > div > div.ant-modal-wrap.ant-modal-centered > div > "
                   "div.ant-modal-content > div.ant-modal-footer > div > button.tz-btn.type-primary.shape-round",
        "immediately_btn": "#root > div > div > div > div.content-wrapper___2zVJo > div:nth-child(2) > div:nth-child("
                           "1) > div.lists___QMlm6 > div:nth-child(1) > div.item_footer___2pxGU > div > div > "
                           "span.item_footer_price_num_green___2n53K",
        "plane": "#root > div > div > div > div.wrap___28j0G > div > div > div.leftContainer___N4dRX > "
                 "div.keyword_list___QLa2B > div > div:nth-child(3)",
        "inquiry_btn": "body > div:nth-child(11) > div > div.ant-modal-wrap.ant-modal-centered > div > "
                       "div.ant-modal-content > div.ant-modal-footer > div > button.tz-btn.type-primary.shape-round",
        "view_order": "body > div:nth-child(11) > div > div.ant-modal-wrap.ant-modal-centered > div > "
                      "div.ant-modal-content > div > div > button",
        "poster": "#root > div > div > div > div.wrap___28j0G > div > div > div.leftContainer___N4dRX > "
                  "div.keyword_list___QLa2B > div > div:nth-child(4)",
        "view_whole": "#root > div > div > div > div.content-wrapper___2zVJo > div:nth-child(2) > div:nth-child(1) > "
                      "div.header___33Uil > div > div",
        "search_box1": 'input[placeholder="搜索服务或案例"]',
        "search_box": '#root > header > div > div.expressNavBarInnerRight___1UBSq > div.search-input___gQgZI.search-input___3kdcS > input',
        "close_search_box": '[aria-label="icon-close"] svg',
        "shopping_cart": "#cart-btn",
        "hot_search_shopping_cart_order": "body > div:nth-child(11) > div > div > div > div.ant-popover-inner > div > "
                                          "div > div > div.spin-container > div > div > div.bottom___2Rzxw > "
                                          "div:nth-child(2) > button",
        "cancel": "body > div:nth-child(12) > div > div.ant-modal-wrap.ant-modal-centered > div > "
                  "div.ant-modal-content > div.ant-modal-footer > div > "
                  "button.tz-btn.type-neutral.shape-round.ghost-text",
        "self_service_order": "#root > header > div > div.expressNavBarInnerRight___1UBSq > "
                              "button.tz-btn.advice-btn___1gXOb.type-primary.shape-round",
        "home_shopping_cart1": "#root > div > div > div > div.wrap___2Hpa2 > div.sku_list___2DoAd.tz-responsive-view > "
                              "div:nth-child(3) > div > div:nth-child(2) > div > div.item_footer___2pxGU > button > i",
        "home_shopping_cart":"#root > div > div > div > div.wrap___2Hpa2 > div.sku_list___2DoAd.tz-responsive-view > div:nth-child(3) > div > div:nth-child(1) > div > div.item_footer___2pxGU > button > i",
        "add_shopping_cart": "text=加入购物车",
        "special_discovery": "#root > header > div > div.expressNavBarInnerLeft___3vZnM > nav > ul > li:nth-child(2)",
        "marketing_calendar": "#root > header > div > div.expressNavBarInnerLeft___3vZnM > nav > ul > "
                              "li.navbar-tab.display-block.hot",
        "shopping_mall": "#root > header > div > div.expressNavBarInnerLeft___3vZnM > nav > ul > li:nth-child(1)",
        "autonomy_programme": "#root > header > div > div.expressNavBarInnerLeft___3vZnM > nav > ul > li:nth-child(4)",

    }

    def hot_search_shopping_cart(self):
        # 点击热门搜索短视频
        self.page.click(HomePage.selectors['short_video'])
        self.page.hover(HomePage.selectors['shopping_cart'])
        self.page.click(HomePage.selectors['hot_search_shopping_cart_order'])
        self.page.click(HomePage.selectors['cancel'])
        # self._wait(1)
        self.page.click(HomePage.selectors['self_service_order'])
        self.page.click(HomePage.selectors['cancel'])

    def home_page(self):
        # 点击全部物料
        self.click(HomePage.selectors['all_materials'])
        # 点击营销场景
        self.click(HomePage.selectors['marketing_scenario'])
        # 点击创意视频
        self.click(HomePage.selectors['creative_video'])
        # 点击精品IP
        self.click(HomePage.selectors['boutique_ip'])
        # 点击热点节日
        self.click(HomePage.selectors['hot_festivals'])
        # 点击爆款策略
        self.click(HomePage.selectors['explosion_strategy'])
        # 点击行业、职能
        self.click(HomePage.selectors['industry'])
        # 点击为你推荐
        self.click(HomePage.selectors['recommend_for_you'])
        # 点击双微
        self.click(HomePage.selectors['double_micro'])

    def hot_search(self):
        # 点击热门搜索短视频
        self.page.click(HomePage.selectors['short_video'])
        self.page.click(HomePage.selectors['short_video_give_thumbs_up'])
        self.page.click(HomePage.selectors['short_video_give_thumbs'])
        self.page.click(HomePage.selectors['creative_mall'])

    def hot_illustration(self, quantity, case_order, case_order_textarea):
        # 鼠标悬浮热门搜索插画
        self.page.hover(HomePage.selectors['illustration'])
        # 点击热门搜索插画
        self.page.click(HomePage.selectors['illustration'])
        # 鼠标悬浮购物车
        self.page.hover(HomePage.selectors['illustration_Shopping_cart'])
        # 点击中等
        self.page.click(HomePage.selectors['secondary'])
        # 点击简单
        self.page.click(HomePage.selectors['simple'])
        # 点击复杂
        self.page.click(HomePage.selectors['complex'])
        # 点击数量
        self.page.click(HomePage.selectors['quantity'])
        self.page.fill(HomePage.selectors['quantity'], quantity)
        # 点击下单按钮，进入下单流程
        self.page.click(HomePage.selectors['order'])
        self.page.click(HomePage.selectors['case_order'])
        self.page.fill(HomePage.selectors['case_order'], case_order)
        self.page.click(HomePage.selectors['case_order_textarea'])
        self.page.type(HomePage.selectors['case_order_textarea'], case_order_textarea)
        self.page.click(HomePage.selectors['confirm'])

    def hot_plane(self, case_order, case_order_textarea):
        # 鼠标悬浮热门搜索平面
        self.page.hover(HomePage.selectors['plane'])
        # 点击热门搜索平面
        self.page.click(HomePage.selectors['plane'])
        # 点击立即询价按钮
        self.page.click(HomePage.selectors['immediately_btn'])
        # 下单流程
        self.page.click(HomePage.selectors['case_order'])
        self.page.fill(HomePage.selectors['case_order'], case_order)
        self.page.click(HomePage.selectors['case_order_textarea'])
        self.page.type(HomePage.selectors['case_order_textarea'], case_order_textarea)
        self.page.click(HomePage.selectors['inquiry_btn'])
        self.page.click(HomePage.selectors['view_order'])

    def hot_poster(self, xiaomi):
        # 鼠标悬浮热门搜索海报
        self.page.hover(HomePage.selectors['poster'])
        # 点击热门搜索海报
        self.page.click(HomePage.selectors['poster'])
        # 查看全部
        self.page.click(HomePage.selectors['view_whole'])
        # 重新搜索,小米
        self.page.click(HomePage.selectors['search_box'])
        self.page.click(HomePage.selectors['close_search_box'])
        self.page.click(HomePage.selectors['search_box'])
        self.page.fill(HomePage.selectors['search_box'], xiaomi)
        self.page.press(HomePage.selectors['search_box'], "Enter")

    def home_page_search(self, search, case_order, case_order_textarea):
        # 首页点击搜索输入框
        self.page.click(HomePage.selectors['search'])
        self.page.fill(HomePage.selectors['search'], search)
        # 点击搜索按钮
        self.page.click(HomePage.selectors['search_btn'])
        # 点赞
        self.page.click(HomePage.selectors['search_give_the_thumbs_up'])
        # 取消点赞
        self.page.click(HomePage.selectors['search_give_the_thumbs_up'])
        # 鼠标悬浮企业logo
        self.page.hover(HomePage.selectors['search_enterprise_logo'])
        # 搜索页面，点击案例
        with self.page.expect_popup() as popup_info:
            self.page.click(HomePage.selectors['case_btn'])
        page2 = popup_info.value
        # 进详情页面，没有登录，必须要刷新一下页面
        page2.goto("https://express.tezign.com/platform/share-case?id=36575")
        # 点赞
        page2.click(HomePage.selectors['case_give_the_thumbs_up'])
        # 取消点赞
        page2.click(HomePage.selectors['case_give_the_thumbs_up'])
        # 立即下单
        page2.click(HomePage.selectors['consult_immediately'])
        page2.click(HomePage.selectors['case_order'])
        page2.fill(HomePage.selectors['case_order'], case_order)
        page2.click(HomePage.selectors['case_order_textarea'])
        page2.type(HomePage.selectors['case_order_textarea'], case_order_textarea)
        page2.click(HomePage.selectors['confirm_btn'])

    def home_page_special_content(self):
        # 点击全部物料
        self.page.click(HomePage.selectors['all_materials'])
        # 点击热门推荐
        self.page.click(HomePage.selectors['popular_recommendation'])

    def home_page_sidebar(self):
        # 点击全部物料
        self.page.click(HomePage.selectors['all_materials'])
        # 鼠标悬浮企业微信
        self.page.hover(HomePage.selectors['enterprise_wechat'])
        # 鼠标悬浮企业邮箱
        self.page.hover(HomePage.selectors['customer_service_email'])
        # 点击自动发布按钮
        with self.page.expect_popup() as popup_info:
            self.page.click((HomePage.selectors['independent_release']))
        page1 = popup_info.value
        page1.close()

    def home_page_operation(self, quantity):
        # 点击热门推荐
        self.page.click(HomePage.selectors['popular_recommendation'])
        # 点击全部物料
        # self.page.click(HomePage.selectors['all_materials'])
        # 点击平面插画plane_illustration
        self.page.click(HomePage.selectors['plane_illustration'])
        # 鼠标悬浮购物车
        self.page.hover(HomePage.selectors['home_shopping_cart'])
        # 点击中等
        self.page.click(HomePage.selectors['secondary'])
        # 点击简单
        self.page.click(HomePage.selectors['simple'])
        # 点击复杂
        self.page.click(HomePage.selectors['complex'])
        # 点击数量
        self.page.click(HomePage.selectors['quantity'])
        self.page.fill(HomePage.selectors['quantity'], quantity)
        #  点击添加购物车
        self.page.click(HomePage.selectors['add_shopping_cart'])
        # 鼠标悬浮购物车
        self.page.hover(HomePage.selectors['home_shopping_cart'])
        # 点击下单按钮
        self.page.click(HomePage.selectors['order'])

    def home_page_navigation(self):
        # 点击特赞发现
        self.page.click(HomePage.selectors['special_discovery'])
        # 点击营销日历
        self.page.click(HomePage.selectors['marketing_calendar'])
        # 点击创意商城
        self.page.click(HomePage.selectors['shopping_mall'])
        # Click text=发布自助项目
        with self.page.expect_popup() as popup_info:
            self.page.click(HomePage.selectors['autonomy_programme'])
        page3 = popup_info.value
        page3.close()
