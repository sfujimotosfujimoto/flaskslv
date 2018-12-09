from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
CORS(app)
app.secret_key = "sf"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

items = []


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")


from flask import render_template, request


@app.route("/")
def index():
    data = "Hello World!"
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# app.run(port=5000, debug=True)
