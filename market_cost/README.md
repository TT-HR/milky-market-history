## Plotly + Dash （推荐）
- Dash 是 Plotly 官方的 Web 框架，可以做交互 UI，比如下拉框选择要展示的 key。
- 示例：用户从下拉框选 "price" 或 "volume"，图表动态更新。

```
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "time": [1, 2, 3, 4],
    "price": [10, 12, 11, 14],
    "volume": [100, 120, 110, 150],
})

# 用户选择 key
key = st.selectbox("选择要展示的数据项", ["price", "volume"])

fig = px.line(df, x="time", y=key, title=f"{key} 走势")
st.plotly_chart(fig)


```

```
from flask import Flask, jsonify, request

app = Flask(__name__)

# 示例数据
data = {
    "abyssal_essence": {"a": 270, "b": 265},
    "acrobatic_hood": {"a": 66000000, "b": 62000000},
}

@app.route("/api/items", methods=["GET"])
def get_all_items():
    """返回所有物品的价格"""
    return jsonify(data)

@app.route("/api/item/<name>", methods=["GET"])
def get_item(name):
    """按名称获取单个物品"""
    item = data.get(name)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route("/api/update", methods=["POST"])
def update_item():
    """更新或新增物品"""
    new_data = request.json
    data.update(new_data)
    return jsonify({"status": "success", "updated": new_data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

```