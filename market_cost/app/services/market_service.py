from utils import file_utils
from utils.i18n import i18n


# 获取所有商品
def get_all_items():
    dict_path = "scripts\market_dict.py"
    dict_data = file_utils(dict_path)
    list = []
    for item in dict_data:
        list.append(i18n.t(item))
    return list


# 根据物品名构建折线图数据
def build_view_data():
    return
