import json
import requests

# 请求最新数据
url = "https://www.milkywayidle.com/game_data/marketplace.json"
resp = requests.get(url)
data = resp.json()  # 返回的 JSON 转成 dict

# 生成字典
market_dict = {item.replace("/items/", ""): "" for item in data["marketData"]}

# 保存到文件
i18n_map_path = "market_dict.json"
with open(i18n_map_path, "w", encoding="utf-8") as f:
    json.dump(market_dict, f, ensure_ascii=False, indent=2)
