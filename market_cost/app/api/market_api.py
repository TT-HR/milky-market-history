from flask import Flask, jsonify, request
from services.market_service import get_all_items, build_view_data

api = Flask(__name__)


# 获取所有物品
@api.route("/api/items", methodes=["GET"])
def get_all_items():
    return get_all_items()


# 获取选中物品的价格
@api.route("/api/items", methodes=["GET"])
def get_item_cost():
    names_param = request.args.getlist("names")
    if not names_param:
        return []
    return build_view_data(
        names_param,
        request.args.get("start_time", ""),
        request.args.get("end_time", ""),
    )
