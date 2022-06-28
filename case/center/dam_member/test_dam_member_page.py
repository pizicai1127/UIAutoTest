#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 4:23 下午
# @Author  : wmt
# @File    : test_dam_member_page.py
# @Software: PyCharm
import allure
import pytest

from common.file_method import FileMethod

account={
    "name":"ui自动化测试企业成员01",
    "email":"auto_ui01@tester.com"
}
bulk_file=FileMethod().get_file_path("data", "", "成员导入模板.xlsx")

class TestDammember():

    @pytest.mark.center
    @pytest.mark.p1
    @allure.title("dam企业客户-添加企业成员-添加全新的邮箱账户")
    def test_add_onemember_with_new_email(self,dam_member_page_init):
        dam_member_page_init.add_one_only_email(name=account["name"],email=account["email"])
        assert_selectors=".tz-message.type-success.visible > div.message-inner>.message-text"
        except_context="成员添加成功，已发送邀请邮件"
        assert dam_member_page_init._text_content(assert_selectors)==except_context
        print("断言成功")


    @pytest.mark.center
    @pytest.mark.p2
    @allure.title("dam企业客户-添加企业成员-添加库内已存在的邮箱账户")
    @pytest.mark.parametrize("email,name", [('wangmengting@tezign.com','wangemngting')])
    def test_add_onemember_with_old_email(self,dam_member_page_init,name,email):
        dam_member_page_init.add_one_only_email(name=name,email=email)
        assert_selectors="div.ant-modal-content > div.ant-modal-body > div.addmember-wrap > div.addmember-email > div > div > div"
        except_context="邮箱已被企业用户注册"
        assert dam_member_page_init._text_content(assert_selectors)==except_context
        print("断言成功")

    @pytest.mark.center
    @pytest.mark.p1
    @allure.title("dam企业客户-批量企业成员-添加全新的账户")
    def test_add_bulk_with_new_account(self,dam_member_page_init):
        dam_member_page_init.add_bulk(path=bulk_file)
        assert_selectors=".tz-message.type-success.visible > div.message-inner>.message-text"
        except_context="成员添加成功，已发送邀请邮件"
        assert dam_member_page_init._text_content(assert_selectors)==except_context
        print("断言成功")

    @pytest.mark.center
    @pytest.mark.p2
    @allure.title("dam企业客户-批量企业成员-重复的账户")
    def test_add_bulk_with_old_email(self,dam_member_page_init):
        dam_member_page_init.add_bulk(path=bulk_file)
        assert_selectors="div.form-modal-content.form-modal-content--upload-status > span > button"
        assert dam_member_page_init._is_visible(assert_selectors)
        print("断言成功")

    @pytest.mark.center
    @pytest.mark.p1
    @pytest.mark.parametrize("keyword", [account["email"],"auto_ui_bulk01@tester.com"])
    @allure.title("dam企业客户-注销账户-{keyword}")
    def test_delete_member(self,dam_member_page_init,keyword):

        dam_member_page_init.search_member(keyword=keyword)
        dam_member_page_init.delete_member()
        assert_selectors = ".member-delete-success-right-text"
        except_context = "前往权限迁移"
        assert dam_member_page_init._text_content(assert_selectors) == except_context
        print("断言成功")


    @pytest.mark.center
    @pytest.mark.p1
    @pytest.mark.parametrize("keyword",["wangmengting@tezign.com","18817771750","王梦婷"] )
    @allure.title("dam企业客户-搜索企业成员-{keyword}")
    def test_search_member_with_email(self,dam_member_page_init,keyword):
        dam_member_page_init.search_member(keyword)
        assert_selectors ="tbody > tr > td:nth-child(1) > div > div.flex-1.text-ellipsis > p"
        assert dam_member_page_init._is_visible(assert_selectors)
        print("-------断言成功-------")


    @pytest.mark.center
    @pytest.mark.p1
    @allure.title("dam企业客户-编辑企业成员")
    @pytest.mark.parametrize("keyword", ["wangmengting@tezign.com"])
    def test_edit_member(self,dam_member_page_init,keyword):

        dam_member_page_init.search_member(keyword)
        dam_member_page_init.edit_member()
        assert_selectors = ".tz-message.type-success.visible > div.message-inner>.message-text"
        except_context = "成员编辑成功"
        assert dam_member_page_init._text_content(assert_selectors) == except_context
        print("-------断言成功-------")




    @pytest.mark.center
    @pytest.mark.p1
    @pytest.mark.parametrize("keyword",["ui自动化测试企业成员01","18817770050","auto_ui01@tester.com"])
    @allure.title("dam企业客户-已注销用户搜索-{keyword}")
    def test_search_delete_member(self, dam_member_page_init, keyword):
        dam_member_page_init.delete_member_serach(keyword)
        #assert_selectors =".ant-table-tbody"
        assert_selectors ='td.ant-table-row-cell-ellipsis.ant-table-row-cell-break-word'
        assert dam_member_page_init._is_visible(assert_selectors)
        print("-------断言成功-------")

