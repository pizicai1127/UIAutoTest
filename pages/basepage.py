# -*- coding: utf-8 -*-
# @Time : 2021/10/9 17:00 
# @Author : Athtony
# @File : basepage.py
import os
import yaml
from playwright.sync_api import Page
from common.logger import logger
from conf.confs import ui_conf_path


class BasePage:
    """
    基础Page层，在这里可以封装一些公共重复方法 ，例如 寻找元素，等待，点击等
    """

    # 定义构造函数，初始化 page
    def __init__(self, page: Page = None) -> None:
        if page is not None:
            self.page = page

    # 窗口尺寸
    def _setViewportSize(self, width, height):
        logger.info(f"设置窗口尺寸为：宽{width}，高{height}")
        self.page.set_viewport_size({"width": width, "height": height})
        self.page.expect_download()

    #  封装 click动作
    def _click(self, element):
        logger.info(f"点击页面元素{element}")
        self.page.click(element)

    #  封装 fill动作
    def _fill(self, element, text):
        logger.info(f"向页面元素{element}中输入：{text}")
        self.page.fill(element, text)

    # 清空原有的再输入动作
    def _empty_fill(self, element, text):
        logger.info(f"先将向页面元素{element}中数据清空，再输入：{text}")
        pass

    #  封装 set_input_files动作
    def _set_input_files(self, element, file):
        logger.info(f"向页面元素{element}中输入：{file}")
        self.page.set_input_files(element, file)


    #  封装 text_content动作
    def _text_content(self, element):
        logger.info(f"获取页面元素{element} 中的文本内容")
        return self.page.text_content(element)

    # 封装 goto方法
    def _go(self, urls):
        logger.info(f"跳转到：{urls} ")
        self.page.goto(urls)

    # 封装 hover方法
    def _hover(self, element):
        logger.info(f"hover页面元素：{element}")
        self.page.hover(element)

    # 封装等待 wait_for_timeout方法
    def _wait_for(self, millisecond):
        self.page.wait_for_timeout(millisecond)

    # 封装 check 勾选方法
    def _check(self, element):
        logger.info(f"勾选页面元素：{element}")
        self.page.check(element)

    # 获取当前页面url
    def _get_url(self):
        return self.page.url

    # 封装取消勾选 uncheck 方法
    def _uncheck(self, element):
        logger.info(f"取消勾选页面元素: {element}")
        self.page.uncheck(element)

    #  封装等待动作(1s=1000)
    def _wait(self, time):
        self.page.wait_for_timeout(time * 1000)

    # 封装 等待元素方法
    def _wait_for_selector(self, element):
        logger.info(f"等待元素{element}出现 ")
        self.page.wait_for_selector(element)

    # 封装 上传文件/文件夹方法
    def _upload(self, element, path):
        logger.info(f"上传的元素：{element},上传文件的路径：{path}")
        self.page.set_input_files(element, path)

    # 封装 键盘输入方法
    def _keyboard_input(self, text):
        logger.info(f"模拟键盘输入：{text}")
        self.page.keyboard.type(text)

    # 封装 键盘点击方法
    def _keyboard_click(self, key):
        logger.info(f"模拟键盘点击：{key}")
        self.page.keyboard.press(key)

    # 封装 输入的排序方式转换
    def _input_sort(self, text):
        sort_dict = {
            "综合排序": "comprehensive_sort",
            "更新时间": "update_time_sort",
            "素材热度": "material_heat_sort",
            "历史总活跃": "history_total_activity_sort",
            "素材名称": "material_name_sort",
            "名称排序": "material_name_sort",
            "创建时间": "create_time_sort",
            "文件大小": "file_size_sort",
            "最近打开": "recently_opened_sort"
        }
        tmp = sort_dict.get(text)
        return tmp

    # 封装 输入权限类型方式方法
    def _input_permission(self, text):
        permission_dict = {
            "企业内外部全员可下载": "company_inside_and_outside_all_download",
            "企业全员通用素材": "company_all_download",
            "部门管控类素材": "department_control",
            "部门私有素材": "department_private",
            "个人管理素材": "personal_management",
            "个人管控类素材": "personal_control",
            "自定义权限": "custom"
        }
        tmp = permission_dict.get(text)
        return tmp

    # 封装 是否全选的状态
    def _check_asset_all_selected(self, element):
        pass

    # 读取元素方法
    def read_yaml_element(self, element, path=ui_conf_path):
        result = yaml.safe_load(open(os.path.dirname(__file__) + path))[f'{type(self).__name__}'][element]
        return result

    # 断言:message
    def _assert(self, function, element, asserts):
        '''断言：massage'''
        try:
            selector = function.read_yaml_element(element)
            assert function._text_content(selector) == asserts
            print('-----断言成功-----')
        except Exception as err:
            raise err

    # 鼠标移动
    def _mouse_move(self, x, y):
        logger.info(f"鼠标移动到{x, y}")
        self.page.mouse.move(x, y)

    # 鼠标左键点击
    def _mouse_left_click(self, x, y):
        logger.info(f"鼠标左键点击{x, y}")
        self.page.mouse.click(x, y)

    def _expect_download(self):
        logger.info(f"开始执行下载任务")
        self.page.expect_download()

    def _down(self, key):
        logger.info(f"长按{key}键")
        self.page.keyboard.down(key)

    def _up(self, key):
        logger.info(f"释放{key}键")
        self.page.keyboard.up(key)

    # 获取元素的属性值
    def _get_attribute(self, element, name):
        logger.info(f'获取元素{element}属性{name}的值')
        return self.page.get_attribute(element, name)

    # 浏览器关闭
    def _close(self):
        self.page.close()

    # 元素是否可点击
    def _is_enable(self, element):
        logger.info(f"元素{element}可点击")
        return self.page.is_enabled(element)

    # 判断checkbox是否勾选主要用于断言
    def _is_check(self, element):
        logger.info(f"元素checkbox {element} 已被勾选")
        return self.page.is_checked(element)

    # 判断元素是否可见
    def _is_visible(self, element):
        logger.info(f"判断 {element} 是否可见")
        return self.page.is_visible(element)

    # 判断元素是否被隐藏
    def _is_hidden(self, element):
        logger.info(f"元素{element}被隐藏 ")
        return self.page.is_hidden(element)

    # 判断元素被禁用
    def _is_disabled(self, element):
        logger.info(f"元素{element}被禁用")
        return self.page.is_disabled(element)

    # 封装没有input输入元素时，上传文件的方法，通过filechooser上传
    def _upload_file_chooser(self, element, path):
        logger.info(f"上传的元素：{element},上传文件的路径：{path}")
        with self.page.expect_file_chooser() as fc_info:
            self.page.click(element)
        file_chooser = fc_info.value
        file_chooser.set_files(path)

    # 右键
    def _right_click(self, element):
        logger.info(f"在{element}区域点击鼠标右键")
        self.page.click(element, button='right')

    # 获取iframe
    def _iframe(self, element):
        logger.info(f"获取iframe{element}")
        return self.page.query_selector(element).content_frame()

    def _db_click(self, element):
        logger.info(f"在{element}区域双击")
        self.page.dblclick(element)

    def _focus(self, element):
        logger.info(f"在{element}处聚焦")
        self.page.focus(element)

