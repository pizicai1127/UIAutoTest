

# from pages.user.UserBasePage import UserBasePage
# # from common.conf import ui_conf_path
# class MaterialGroupPage(UserBasePage):

    # #素材组页面元素：
    # selectors = {
    #     "company-pic" : "[class='icon-mask']",
    #     "into_group" : "._3jLs_>div>div:nth-child(3)>div>div>div",
    #     "navbar_title" : "[test-id = 'TAB_DAM_APPROVED_LIST']",
    #     "add_Materialgroup_button" : ".layout_userlist_button",
    #     "group_name_input" : "[id='groupName']",
    #     "group_description_input" : "[id='description']",
    #     "button" : "[class='tz-btn ml-20 type-primary shape-round']",
    #     "..." : "i[class='anticon layout_drop_declear_icon']>svg",
    #     "group_delete_button" : "[class='ant-dropdown ant-dropdown-placement-bottomLeft']>ul>li:nth-child(5)",
    #     "confirm_delete_button" : "div[class='foot-action action-ok type-danger']"
    # }
    # # selectors = read_yaml(ui_conf_path)["MaterialGroupPage"]["into_group"]
    # #新增素材组
    # def add_material(self,text_name,text_description):
    #     #进入素材组页面
    #     self._click(MaterialGroupPage.selectors["into_group"])
    #     # self._click(read_yaml(ui_conf_path)["MaterialGroupPage"]["into_group"])
    #     self._click(MaterialGroupPage.selectors["add_Materialgroup_button"])
    #     self._fill(MaterialGroupPage.selectors["group_name_input"], text_name)
    #     self._fill(MaterialGroupPage.selectors["group_description_input"], text_description)
    #     self._click(MaterialGroupPage.selectors["button"])
    #
    # #删除素材组
    # def group_delete(self):
    #     #回到主素材组页面
    #     # self._click("[aria-current='page']")
    #     # #进入素材组
    #     # self._click("div[class='react-draggable react-draggable-dragged']>div>div>div>div>div>div")
    #     #执行删除操作
    #     self._hover(MaterialGroupPage.selectors["..."])
    #     # self.page.wait_for_timeout(600)
    #     # selectors = read_yaml()
    #     self._click(MaterialGroupPage.selectors["group_delete_button"])
    #
    #     selector = read_yaml('/common/ui_locators.yaml')["MaterialGroupPage"]["confirm_delete_button"]
    #     self._click(selector)


