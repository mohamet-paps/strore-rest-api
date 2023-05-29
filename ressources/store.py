from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import request
import uuid
from db.store import stores
from validations.store_schema import StoreSchema

blp = Blueprint("Store", __name__, description="Store api")


@blp.route("/stores/<int:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            store = stores[store_id]
            return {"store": store}, 200
        except:
            abort(404, message="NOT_FOOUND:store not found")


@blp.route("/stores")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}, 200

    @blp.arguments(StoreSchema)
    def post(self, store_data):
      #   store_data = request.get_json()
        store_id = uuid.uuid4().hex
        store = {"id": store_id, **store_data, "items": []}
        stores[store_id] = store
        return {"store": store}, 201
