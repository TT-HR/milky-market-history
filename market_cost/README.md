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