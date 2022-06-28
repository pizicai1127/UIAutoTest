
from common.file_method import FileMethod
import os


'''Host'''
Host2 = 'https://asset-stage.tezign.com'

'''租户'''
T2 = 't2'
Appid='t2'
T8 = 't8'

'''账号'''
account = 'yanglun@tezign.com'
account_LZJ = 'liuzhijie@tezign.com'
account_LZJ_001 = 'UI_test_lzj_001@tezign.com'
account_LZJ_002 = 'UI_test_lzj_002@tezign.com'
account_LZJ_003 = 'UI_test_lzj_003@tezign.com'
account_LZJ_004 = 'UI_test_lzj_004@tezign.com'
account_LZJ_005 = 'UI_test_lzj_005@tezign.com'
account_LZJ_006 = 'UI_test_lzj_006@tezign.com'
account_LZJ_007 = 'UI_test_lzj_007@tezign.com'
account_LZJ_008 = 'UI_test_lzj_008@tezign.com'
account_LZJ_009 = 'UI_test_lzj_009@tezign.com'

account_RY = 'ruiyin@tezign.com'
password = 'qq111111'
password_LZJ = '111111'
password_LZJ_001 = '111111'
password_LZJ_002 = '111111'
password_LZJ_003 = '111111'
password_LZJ_004 = '111111'
password_LZJ_005 = '111111'
password_LZJ_006 = '111111'
password_LZJ_007 = '111111'
password_LZJ_008 = '111111'
password_LZJ_009 = '111111'

password_RY = 'qq123456'
account_ljh = 'liujiehui@tezign.com'
account_lsm = 'liushaoming@tezign.com'
account_ssm = 'shisenming@tezign.com'
account_sq = 'shiquan@tezign.com'
account_sm = 'shiming@tezign.com'
account_ss = 'shisen@tezign.com'

'''UI元素定位配置文件目录'''
ui_conf_path = '/../conf/ui_locators.yaml'
# ui_data_file_path = './data/test_file_001.jpg'
# ui_data_file_path = '/Users/tezign/PycharmProjects/tezign-watchmen/data/test_file_001.jpg'
ui_data_file_path = FileMethod().get_file_path('data', '', 'test_file_001.jpg')
ui_data_folder_path = './data/test_folder_001'
ui_data_enclosure_path = './data/test_enclosure_001.jpeg'
# 当前项目路径
Base_Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试文件夹上传路径
upload_folder = os.path.join(Base_Dir, 'data/test_folder/')

link = '链接: https://pan.baidu.com/s/1INA3rrKYb3n6iUGah83Vpg 提取码: evz2 复制这段内容后打开百度网盘手机App，操作更方便哦'


'''Url-各个页面的路径'''
url_homePage = f'{Host2}/web/bi/stat/workbench'         # 首页路径
url_assetPage = f'{Host2}/dam_enterprise/approved_list'        # 素材库路径
url_assetGroupPage = f'{Host2}/dam_enterprise/group'       # 素材组路径
url_myCollectionPage = f'{Host2}/dam_enterprise/group#3'        # 我收藏的路径
url_myCreatedPage = f'{Host2}/dam_enterprise/group#1'        # 我创建的路径
url_myCooperationPage = f'{Host2}/dam_enterprise/group#2'        # 与我协作的路径
url_pendingAreaPage = f'{Host2}/dam_enterprise/draft'     # 待入库路径
url_dam_external_page =f'{Host2}/base/company/external-contacts' # 外部联系人路径
url_dam_member_page =f'{Host2}/base/company/setting-member' # 成员信息路径
url_myCollectionPage_home = f'{Host2}/dam_enterprise/group/-1/3'    # 首页跳转的我的收藏的路径
url_recyclePage = f'{Host2}/dam_enterprise/recycle'     # 回收站路径
url_dam_external_page =f'{Host2}/base/company/external-contacts' #外部联系人路径
url_dam_member_page =f'{Host2}/base/company/setting-member' #成员信息路径
url_myCollectionPage_home = f'{Host2}/dam_enterprise/group/-1/3'    #首页跳转的我的收藏的路径
url_sharingGroupPage = f'{Host2}/dam_enterprise/group/3944'  # 分享落地页特定的素材组
url_lifecyclePage = f'{Host2}/dam_enterprise/life_cycle/manage'  # 有效期管理的路径
url_workflowPage = f'{Host2}/web/workflow/center/home'      # 工作流路径
url_log_history = f'{Host2}/dam_enterprise/log_history'  # 用户动态页面路径
url_dashboard = f'{Host2}/dam_enterprise/dashboard'   # 统计页面路径


'''网盘路径'''
link_baidu = 'https://pan.baidu.com/s/1dCnThqHDpeR8SrqcdVgcGQ'
password_baidu = 'nrgc'
link_muse = ''
password_muse = ''
baidu_transfer_link = "https://pan.baidu.com/s/1CUZAL7hwyU6OLs3CedsvuQ"
baidu_transfer_password = "en2a"

"""box导入路径"""


'''临时创建的数据'''
asset_name = 'UI自动化测试-素材名称'
group_name = 'UI自动化测试-我收藏的'
group_description = 'UI自动化测试-我收藏的描述'
asset_saved_filters_name = 'UI自动化测试-常用筛选001'
detail_comment_text = 'UI自动化测试-评论'



'''断言'''
login_success = "工作台"
assert_delete_success = "删除素材成功"
basket_empty_success = "清空素材篮成功"
upload_success = "入库成功"
asset_search_result = 'test_file_001'
asset_test_data = ['test_file_001', 'UI自动化测试']
update_time_sort_assert = '更新时间'
recently_opened_sort_assert = '最近打开'
material_heat_sort_assert = '素材热度'
history_total_activity_sort_assert = '历史总活跃'
material_name_sort_assert = '素材名称'
creat_time_sort_assert = '创建时间'
file_size_sort_assert = '文件大小'
basket_add_same_asset_assert = '该素材已存在于素材篮'
batch_share_message_text_assert = '链接创建并复制成功，快去分享吧～'
batch_edit_message_text_assert = '保存成功'
batch_rename_message_text_assert = '重命名成功'
batch_add_to_group_text_assert = '已成功添加到素材组'
asset_list_mode_assert = '字段配置'


# 分享落地页各种配置链接
# 互联网用户可下载-永久有效
visitor_can_download_url = f"{Host2}/s/gaEnmcMXtw/ 《分享落地页测试-石明（勿删除）》"
# 互联网用户可查看-永久有效
visitor_only_view_url = f"{Host2}/s/gaEht0ADPk/ 《分享落地页测试-石明（勿删除）》"
# 内部用户可下载-永久有效
internal_can_download_url = f"{Host2}/s/gaEq2z0Mnw/ 《分享落地页测试-石明（勿删除）》"
# 内部用户可查看-永久有效
internal_only_view_url = f"{Host2}/s/gaErrLbUBM/ 《分享落地页测试-石明（勿删除）》"

# 网页导入url
douyin_url_import = "https://v.douyin.com/FBGYCNf/"
url_import_baidu = "https://www.baidu.com/"