from flask import Flask, request
from services.market_service import get_all_items, build_view_data

api = Flask(__name__)


# 获取所有物品
@api.route("/api/items", methodes=["GET"])
def all_items():
    return get_all_items()


# 获取选中物品的价格
@api.route("/api/item_cost", methodes=["GET"])
def get_item_cost():
    foods = request.args.get("foods")
    if not foods:
        foods = ["egg"]
    return build_view_data(
        foods,
        request.args.get("start_time", ""),
        request.args.get("end_time", ""),
    )
