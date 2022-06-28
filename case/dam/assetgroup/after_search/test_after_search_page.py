# -*- coding:utf-8 -*-
# @author:ruiyin
# data:2022/3/18 1:16 下午
# @File:test_after_search_page.py
import pytest
from pages.assets.AfterSearchPage import AfterSearchPage


class TestAfterSearchPage:
    def test_search_page(self, login_i):
        """
        进入全部素材组页面
        @rtype: login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        asset_content = search_page._get_url()
        url = "https://asset-stage.tezign.com/dam_enterprise/group"
        assert url in asset_content

    @pytest.mark.parametrize('text', ['ry'])
    def test_search_text(self, text, login_i):
        """
        全部素材组页面搜索结果
        @rtype: text、login_in
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        ele = search_page.read_yaml_element("search_all")
        assert search_page._text_content(ele).strip() == '全部'

    '''以下是搜索后第一个是素材组'''
    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_search_newpage_group(self, text, login_i):
        """
        全部素材组页面搜索后素材组-新标签页打开
        @rtype: text， login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材组' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_first_group()
            search_page.search_newpage()
            ele = search_page._get_url()  # 获取当前页面的url
            url = "https://asset-stage.tezign.com/dam_enterprise/group"
            assert url in ele
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_search_edit_group(self, text, login_i):
        """
        全部素材组页面搜索后素材组-编辑信息
        @rtype: text,login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材组' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_first_group()
            search_page.search_edit_group()
            ele = search_page.read_yaml_element("search_edit_group_true")
            assert search_page._is_visible(ele) == True
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_search_subscribe_group(self, text, login_i):
        """
        全部素材组页面搜索后素材组-订阅
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材组' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_first_group()
            search_page.search_subscribe_group()
            ele = search_page.read_yaml_element("search_subscribe_toast")
            assert search_page._text_content(ele) == '订阅成功，每周三10:00将邮件通知更新'
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_search_subscribe_group2(self, text, login_i):
        """
        全部素材组页面搜索后素材组-取消订阅
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材组' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_first_group()
            search_page.search_subscribe_group()
            ele = search_page.read_yaml_element("search_subscribe_toast")
            assert search_page._text_content(ele) == '取消成功'
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_search_collection_group(self, text, login_i):  # 收藏
        """
        全部素材组页面搜索后素材组-收藏
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材组' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_first_group()
            search_page.search_collection_group()
            ele = search_page.read_yaml_element("search_collection_toast")
            assert search_page._text_content(ele) == '你已成功收藏该素材组'
        else:  # 其他
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_search_collection_group2(self, text, login_i):  # 取消收藏
        """
        全部素材组页面搜索后素材组-取消收藏
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材组' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_first_group()
            search_page.search_collection_group()
            ele = search_page.read_yaml_element("search_collection_toast")
            assert search_page._text_content(ele) == '你已取消收藏该素材组'
        else:  # 其他
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_search_share_group(self, text, login_i):
        """
        全部素材组页面搜索后素材组-分享
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材组' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_first_group()
            search_page.search_share_group()
            ele = search_page.read_yaml_element("search_share_toast")
            assert search_page._text_content(ele) == "链接创建并复制成功，快去分享吧～"
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_search_copy(self, text, login_i):  # 复制素材组
        """
        全部素材组页面搜索后素材组-复制素材组
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材组' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_first_group()
            search_page.search_copy_group()
            ele = search_page.read_yaml_element("search_copy_group_toast")
            assert search_page._text_content(ele) == "已复制成功"
        else:  # 其他
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_search_download(self, text, login_i):
        """
        全部素材组页面搜索后素材组-下载
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材组' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_first_group()
            search_page.search_download_group()
            ele = search_page.read_yaml_element("search_download1_asset")  # 下载-下载素材
            assert search_page._text_content(ele) == "下载素材"
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_search_delete(self, text, login_i):  # 删除素材组
        """
        全部素材组页面搜索后素材组-删除素材组
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材组' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_first_group()
            search_page.search_delete_group()
            ele = search_page.read_yaml_element("search_delete_toast")
            assert "已删除" in search_page._text_content(ele)
        else:  # 其他
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    '''以下是搜索后第一个是素材是图片类型'''
    @pytest.mark.parametrize('text', ['ry测试'])
    def test_search_newpage_asset(self, text, login_i):
        """
        全部素材组页面搜索后素材-新标签页打开
        @rtype: text， login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材' in search_page._text_content(search_title):  # 搜索结果有素材
            search_page.search_first_asset()
            search_page.search_newpage()
            ele = search_page._get_url()  # 获取当前页面的url
            url = "https://asset-stage.tezign.com/dam_enterprise/group"
            assert url in ele
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry测试'])
    def test_search_rename(self, text, login_i):
        """
        全部素材组页面搜索后素材-重命名
        @rtype: text， login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材' in search_page._text_content(search_title):  # 搜索结果有素材
            search_page.search_first_asset()
            search_page.search_rename()
            ele = search_page.read_yaml_element("search_rename_toast")
            assert search_page._text_content(ele) == "重命名成功"
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry测试'])
    def test_search_edit_asset(self, text, login_i):
        """
        全部素材组页面搜索后素材-编辑（操作更多中的编辑）
        @rtype: text， login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材' in search_page._text_content(search_title):  # 搜索结果有素材
            search_page.search_first_asset()
            search_page.search_edit_asset()
            ele = search_page._get_url()  # 获取当前页面的url
            url = "https://asset-stage.tezign.com/dam_enterprise/group"
            assert url in ele
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry测试'])
    def test_search_download_asset(self, text, login_i):
        """
        全部素材组页面搜索后素材-下载
        @rtype: text， login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材' in search_page._text_content(search_title):  # 搜索结果有素材
            search_page.search_first_asset()
            search_page.seach_download_asset()
            ele = search_page.read_yaml_element("search_download2_asset")
            assert search_page._text_content(ele) == "下载"
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry测试'])
    def test_search_share_asset(self, text, login_i):
        """
        全部素材组页面搜索后素材-分享
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_first_asset()
            search_page.search_share_asset()
            ele = search_page.read_yaml_element("search_share_toast")
            assert search_page._text_content(ele) == "链接创建并复制成功，快去分享吧～"
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry测试'])
    def test_search_add_group(self, text, login_i):
        """
        全部素材组页面搜索后素材-添加到组
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材' in search_page._text_content(search_title):  # 搜索结果有素材
            search_page.search_first_asset()
            search_page.search_add_group()
            ele = search_page.read_yaml_element("search_add_group_toast")
            assert search_page._text_content(ele) == "已成功添加到素材组"
        else:  # 其他
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry测试'])
    def test_search_add_basket(self, text, login_i):
        """
        全部素材组页面搜索后素材-添加到素材篮
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        # search_page.search_basket()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材' in search_page._text_content(search_title):  # 搜索结果有素材
            search_page.search_first_asset()
            search_page.search_add_basket_asset()
            ele = search_page.read_yaml_element("search_add_basket_toast")
            assert search_page._text_content(ele) == "已成功加入素材篮"
        else:  # 其他
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry测试'])
    def test_search_owner(self, text, login_i):
        """
        全部素材组页面搜索后素材-修改所有者
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材' in search_page._text_content(search_title):  # 搜索结果有素材
            search_page.search_first_asset()
            search_page.search_owner()
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'
        else:  # 其他
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry测试'])
    def test_search_type(self, text, login_i):
        """
        全部素材组页面搜索后素材-修改权限类型
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材' in search_page._text_content(search_title):  # 搜索结果有素材
            search_page.search_first_asset()
            search_page.search_type()
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'
        else:  # 其他
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    '''以下是勾选多个操作'''
    @pytest.mark.parametrize('text', ['ry测试'])
    def test_search_Multiple_download(self, text, login_i):
        """
        全部素材组页面搜索后是素材-勾选多个批量下载
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材' in search_page._text_content(search_title):
            search_page.search_Multiple_download_asset()  # 搜索结果没有素材组只有素材
            ele = search_page.read_yaml_element("search_all")
            assert search_page._is_visible(ele) == True
        else:  # 没有搜索结果
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_search_Multiple_download_group(self, text, login_i):
        """
        全部素材组页面搜索后是素材组-勾选多个批量下载
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材组' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_Multiple_download_group()
            ele = search_page.read_yaml_element("search_all")
            assert search_page._is_visible(ele) == True
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry测试'])
    def test_search_Multiple_basket_asset(self, text, login_i):
        """
        全部素材组页面搜索后是素材-勾选多个加入素材篮
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.search_basket()  # 先清空素材篮，以免添加已添加过的
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材' in search_page._text_content(search_title):
            search_page.search_Multiple_basket_asset()  # 搜索结果没有素材组只有素材
            ele = search_page.read_yaml_element("search_Multiple_basket_asset_toast")
            assert search_page._text_content(ele) == "已成功加入素材篮"
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_search_Multiple_basket_group(self, text, login_i):
        """
        全部素材组页面搜索后是素材组-勾选多个加入素材篮
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材组' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_Multiple_basket_group()
            ele = search_page.read_yaml_element("search_Multiple_basket_group_toast")
            assert search_page._text_content(ele) == "目前仅支持添加素材至素材篮"
        else:
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'

    @pytest.mark.parametrize('text', ['ry自动化'])
    def test_search_Multiple_cancel(self, text, login_i):
        """
        全部素材组页面搜索后批量操作取消
        @rtype: text, login_i
        """
        search_page = AfterSearchPage(login_i)
        search_page.goto_search()
        search_page.after_search(text)
        search_title = search_page.read_yaml_element("search_title")
        if '素材组' in search_page._text_content(search_title):  # 搜索结果有素材组
            search_page.search_Multiple_cancel_group()
            ele = search_page.read_yaml_element("search_all")
            assert search_page._is_visible(ele) == True
        else:  # 没有搜索结果
            ele = search_page.read_yaml_element("search_all")
            assert search_page._text_content(ele).strip() == '全部'
