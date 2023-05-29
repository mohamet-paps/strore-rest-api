from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import request
import uuid
from db.store import stores


blp = Blueprint("Items", __name__, description="Items Api")


@blp.route("/items/<int:store_id>/create")
class Item(MethodView):
    def post(self, store_id):
        try:
            item_data = request.get_json()
            item = {**item_data, "store_id": store_id}
            stores[store_id]["items"].append(item)
            return {"item": item}, 201
        except:
            abort(404, message="NOT_FOOUND:store not found")


@blp.route("/items/<int:store_id>")
class ItemList(MethodView):
    def get(self, store_id):
        try:
            item = stores[store_id]["items"]
            return {"item": item}, 200
        except:
            abort(404, message="NOT_FOOUND:store not found")
