import uuid
from flask import Flask
from flask import request

from db.store import stores


app = Flask(__name__)


@app.get("/stores")
def get_stores():
    return {"stores": list(stores.values())}, 200


@app.get("/stores/<int:store_id>")
def get_store(store_id):
    try:
        store = stores[store_id]
        return {"store": store}, 200
    except:
        return {"message": "NOT_FOOUND:store not found"}, 404


@app.post("/stores")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {"id": store_id, **store_data, "items": []}
    stores[store_id] = store
    return {"store": store}, 201


@app.post("/items/<int:store_id>/create")
def create_item(store_id):
    try:
        item_data = request.get_json()
        item = {**item_data, "store_id": store_id}
        stores[store_id]["items"].append(item)
        return {"item": item}, 201
    except:
        return {"message": "NOT_FOOUND:store not found"}, 404


@app.get("/items/<int:store_id>")
def get_store_item(store_id):
    try:
        item = stores[store_id]["items"]
        return {"item": item}, 200
    except:
        return {"message": "NOT_FOOUND:store not found"}, 404
