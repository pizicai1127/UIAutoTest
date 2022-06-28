#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 8:08 下午
# @Author  : wmt
# @File    : test_dam_external_page.py
# @Software: PyCharm

import allure
import pytest

from common.file_method import FileMethod
from conf.confs import url_dam_external_page

account={
    "email_name":"auto_ui邮箱外部成员01",
    "new_email":"auto_ui_ex01@tester.com",
    "old_email":"wangmengting@tezign.com",
    "phone_name":"auto_ui手机外部成员01",
    "new_phone":"18817770050",
    "old_phone":"18817771750"
}

bulk_file=FileMethod().get_file_path("data", "", "外部联系人导入模板.xlsx")

class TestDamexternal():

    @pytest.mark.center
    @pytest.mark.p1
    @allure.title("dam企业客户-添加外部成员-添加全新的邮箱账户")
    def test_add_one_with_new_email(self, dam_external_page_init):
        dam_external_page_init.add_one_init(name=account["email_name"], email=account["new_email"])
        assert_selectors = "div > div.ant-modal-content > div.ant-modal-footer"
        assert dam_external_page_init._is_visible(assert_selectors)
        print("断言成功")
        dam_external_page_init._go(url_dam_external_page)
        dam_external_page_init._wait(5)

        # 外部联系人需要找先到子维度，才会出现注销按钮
        dam_external_page_init.search_dimension()
        dam_external_page_init._wait(2)
        # 找到子维度后，搜索用户
        dam_external_page_init.search_member(account["new_email"])
        dam_external_page_init.delete_member()


    @pytest.mark.center
    @pytest.mark.p2
    @allure.title("dam企业客户-添加外部成员-添加已存在邮箱账户")
    def test_add_one_with_old_email(self, dam_external_page_init):
        dam_external_page_init.add_one_init(name=account["email_name"], email=account["old_email"])
        assert_selectors = "button.tz-btn.form-modal-content__highlight.type-primary.shape-round.ghost-text"
        except_context = "下载错误报告"
        assert dam_external_page_init._text_content(assert_selectors) == except_context
        print("断言成功")

    @pytest.mark.center
    @pytest.mark.p1
    @allure.title("dam企业客户-添加外部成员-添加全新的手机账户")
    def test_add_one_with_new_phone(self, dam_external_page_init):
        dam_external_page_init.add_one_init(name=account["phone_name"], phone=account["new_phone"])
        assert_selectors = "div > div.ant-modal-content > div.ant-modal-footer"
        assert dam_external_page_init._is_visible(assert_selectors)
        print("断言成功")
        dam_external_page_init._go(url_dam_external_page)
        dam_external_page_init._wait(5)
        # 外部联系人需要找先到子维度，才会出现注销按钮
        dam_external_page_init.search_dimension()
        dam_external_page_init._wait(2)
        # 找到子维度后，搜索用户
        dam_external_page_init.search_member(account["new_phone"])
        dam_external_page_init.delete_member()

    @pytest.mark.center
    @pytest.mark.p2
    @allure.title("dam企业客户-添加外部成员-添加已存在邮箱账户")
    def test_add_one_with_old_phone(self, dam_external_page_init):
        dam_external_page_init.add_one_init(name=account["phone_name"], phone=account["old_phone"])
        assert_selectors = "button.tz-btn.form-modal-content__highlight.type-primary.shape-round.ghost-text"
        except_context = "下载错误报告"
        assert dam_external_page_init._text_content(assert_selectors) == except_context
        print("断言成功")

    @pytest.mark.center
    @pytest.mark.p1
    @allure.title("dam企业客户-批量添加外部成员-添加全新的邮箱账户")

    def test_add_bulk(self, dam_external_page_init):
        dam_external_page_init.add_bulk_init(path=bulk_file)
        assert_selectors = "div > div.ant-modal-content > div.ant-modal-footer"
        assert dam_external_page_init._is_visible(assert_selectors)
        print("断言成功")



    @pytest.mark.center
    @pytest.mark.p1
    @pytest.mark.parametrize("keyword",["annawang@3202.com","anna"] )
    @allure.title("dam外部联系人-搜索外部联系人-{keyword}")
    def test_search_external(self, dam_external_page_init, keyword):

        dam_external_page_init.search_member(keyword)
        assert_selectors ="div.memberlist > div > div > div > div > div > div > table > tbody"
        assert dam_external_page_init._is_visible(assert_selectors)
        print("-------断言成功-------")


    @pytest.mark.center
    @pytest.mark.p1
    @pytest.mark.parametrize("keyword", ["annawang@3202.com"])
    @allure.title("dam外部联系人-编辑-{keyword}")
    def test_edit_member(self,dam_external_page_init,keyword):
        dam_external_page_init.search_member(keyword)
        dam_external_page_init.edit_member()
        assert_selectors = ".tz-message.type-success.visible > div.message-inner>.message-text"
        except_context = "成员信息更新成功"
        assert dam_external_page_init._text_content(assert_selectors) == except_context
        print("-------断言成功-------")

    @pytest.mark.center
    @pytest.mark.p1
    @pytest.mark.parametrize("account", ["auto_ui_bulk02@tester.com"])
    @allure.title("dam企业客户-注销外部账户-{account}")
    def test_delete_exter(self, dam_external_page_init,account):
        # 外部联系人需要找先到子维度，才会出现注销按钮
        dam_external_page_init.search_dimension()
        dam_external_page_init._wait(2)
        # 找到子维度后，搜索用户
        dam_external_page_init.search_member(keyword=account)
        dam_external_page_init.delete_member()
        assert_selectors = ".member-delete-success-right-text"
        except_context = "前往权限迁移"
        assert dam_external_page_init._text_content(assert_selectors) == except_context
        print("断言成功")

