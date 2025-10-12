import requests
import json
import os

url = "https://www.milkywayidle.com/game_data/marketplace.json"


# 获取源文件
def get_mete_data():
    req = requests.get(url=url)
    meat_json = req.json()
    # 处理数据
    data = build_data(meat_json)
    # 写入json文件
    file_name = f"data/{meat_json["timestamp"]}.json"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# 取对应key的第一条数据
def build_data(data):
    data_list = []
    for item_key, inner in data["marketData"].items():
        if not inner:
            continue
        first_key = next(iter(inner))
        first_value = inner[first_key]
        if first_value is None:
            continue
        item_data = {item_key.replace("/items/", ""): first_value}
        # item_data = {item_key: {first_key: first_value}}
        data_list.append(item_data)
    return data_list


if __name__ == "__main__":
    get_mete_data()
