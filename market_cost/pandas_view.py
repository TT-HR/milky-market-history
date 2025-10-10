import os, glob, json
from datetime import datetime
import streamlit as st
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# reads all files name
files = glob.glob("data/*.json")

# for reads all files
records = []
for file_name in files:
    timestamp = int(os.path.splitext(os.path.basename(file_name))[0])
    item_time = datetime.fromtimestamp(timestamp).strftime("%m-%d %H时")

    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    for item in data:
        for k, v in item.items():
            records.append(
                {
                    "时间": item_time,
                    "物品": k,
                    "买入价": v.get("a"),
                    "卖出价": v.get("b"),
                }
            )


df = pd.DataFrame(records)
market_dict_path = "market_dict.json"
with open(market_dict_path, "r", encoding="utf-8") as f:
    market_data_list = json.load(f)

for market_key in market_data_list.keys():
    df_item = df[df["物品"] == market_key]
    # melt 把 buy/sell 拆成两条线
    df_melted = df_item.melt(
        id_vars=["时间"],
        value_vars=["买入价", "卖出价"],
        var_name="类型",
        value_name="出价",
    )
    fig = px.line(
        df_melted, x="时间", y="出价", color="类型", title=f"{market_key} 价格走势"
    )

# Dash 应用
app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1("物品价格走势"),
        dcc.Dropdown(
            id="item-dropdown",
            options=[{"label": i, "value": i} for i in df["物品"].unique()],
            value="acrobatic_hood",
        ),
        dcc.Graph(id="price-graph", figure=fig),
    ]
)


@app.callback(Output("price-graph", "figure"), Input("item-dropdown", "value"))
def update_graph(selected_item):
    dff = df[df["物品"] == selected_item]
    dff = dff.melt(
        id_vars=["时间"],
        value_vars=["买入价", "卖出价"],
        var_name="类型",
        value_name="出价",
    )
    fig = px.line(
        dff, x="时间", y="出价", color="类型", title=f"{selected_item} 价格走势"
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
