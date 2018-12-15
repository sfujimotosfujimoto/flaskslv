from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app)
app.secret_key = "sf"
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")


from flask import render_template, request


@app.route("/")
def index():
    data = "Hello World!"
    return render_template("index.html", data=data)


if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(host="0.0.0.0", port=5000)