from flask import Flask, jsonify, request

api = Flask(__name__)


# 获取所有物品
@api.route("/api/items", methodes=["GET"])
def get_all_items():
    return


# 获取选中物品的价格
@api.route("/api/items", methodes=["GET"])
def get_item_cost():
    names_param = request.args.get("names")

    return
