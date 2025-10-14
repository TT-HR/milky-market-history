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
def build_view_data(names: list[str]):
    files = glob.glob("data/*.json")
    # 返回的数据
    records = []
    for file_name in files:
        timestamp = int(os.path.splitext(os.path.basename(file_name))[0])
        # 时间
        item_time = datetime.fromtimestamp(timestamp).strftime("%m-%d %H时")

        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)

        for name in names:
            # 组装数据
            isExist = get_value(name, records)
            # 总数据
            value = get_value(name, data)

            if isExist:
                for item in isExist:
                    # 买入
                    a_data = item.setdefault("a", {}).setdefault("data", [])
                    a = value.get("a")
                    a_data = a_data + a

                    # 卖出
                    b_data = item.get("b", {}).get("data")
                    b = value.get("b")
                    b_data = b_data + b
                    records.append(
                        {
                            "key": name,
                            "name": "买入",
                            "type": "line",
                            "stack": "Total",
                            "data": a_data,
                        },
                        {
                            "key": name,
                            "name": "卖出",
                            "type": "line",
                            "stack": "Total",
                            "data": b_data,
                        },
                    )
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
    return records


def get_value(k: str, data: json):
    for item in data:
        if k in item:
            value = item[k]
            return value
