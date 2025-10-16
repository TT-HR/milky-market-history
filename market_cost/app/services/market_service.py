from utils import file_utils
from utils.i18n import i18n
import os, glob, json
from datetime import datetime


# 获取所有商品
def get_all_items():
    dict_path = "scripts\market_dict.py"
    dict_data = file_utils(dict_path)
    list = []
    for item in dict_data:
        list.append(i18n.t(item))
    return list


# 根据物品名构建折线图数据
# 暂时做成单选，后续优化多选
def build_view_data(names: list[str], start_time, ent_time):
    files = glob.glob("data/*.json")
    # 返回的数据
    dates = []
    records = []
    for file_name in files:
        timestamp = int(os.path.splitext(os.path.basename(file_name))[0])
        if start_time <= timestamp <= ent_time:
            continue
        # 时间
        item_time = datetime.fromtimestamp(timestamp).strftime("%m-%d %H时")
        dates.append(item_time)

        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)

        for name in names:
            # 组装数据
            isExist = get_value(name, records)
            # 总数据
            value = get_value(name, data)

            if isExist:
                # 更新已存在的记录
                for item in isExist:
                    # 买入
                    a_data = item.setdefault("a", {}).setdefault("data", [])
                    a_data.extend(value.get("a", ""))

                    # 卖出
                    b_data = item.setdefault("b", {}).setdefault("data", [])
                    b_data.extend(value.get("b", ""))
            else:
                records.append(
                    {
                        "key": name,
                        "name": "买入",
                        "type": "line",
                        "stack": "Total",
                        "data": value.get("a"),
                    },
                    {
                        "key": name,
                        "name": "卖出",
                        "type": "line",
                        "stack": "Total",
                        "data": value.get("b"),
                    },
                )
    return {"data": dates, "series": records}


def get_value(k: str, data: json):
    for item in data:
        if k in item:
            value = item[k]
            return value
