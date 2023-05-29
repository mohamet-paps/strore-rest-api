# import uuid
from flask import Flask
# from flask import request
from flask_smorest import Api

# from db.store import stores

from ressources.item import blp as ItemBlueprint
from ressources.store import blp as StoreBlueprint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST APT"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"

api = Api(app)


@app.get("/")
def healf_check():
    return {"message": "hello you"}, 200


api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)

# @app.get("/stores")
# def get_stores():
#     return {"stores": list(stores.values())}, 200


# @app.get("/stores/<int:store_id>")
# def get_store(store_id):
#     try:
#         store = stores[store_id]
#         return {"store": store}, 200
#     except:
#         abort(404, message="NOT_FOOUND:store not found")


# @app.post("/stores")
# def create_store():
#     store_data = request.get_json()
#     store_id = uuid.uuid4().hex
#     store = {"id": store_id, **store_data, "items": []}
#     stores[store_id] = store
#     return {"store": store}, 201


# @app.post("/items/<int:store_id>/create")
# def create_item(store_id):
#     try:
#         item_data = request.get_json()
#         item = {**item_data, "store_id": store_id}
#         stores[store_id]["items"].append(item)
#         return {"item": item}, 201
#     except:
#         abort(404, message="NOT_FOOUND:store not found")


# @app.get("/items/<int:store_id>")
# def get_store_item(store_id):
#     try:
#         item = stores[store_id]["items"]
#         return {"item": item}, 200
#     except:
#         abort(404, message="NOT_FOOUND:store not found")
