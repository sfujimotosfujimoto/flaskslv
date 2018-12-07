import sqlite3
from typing import List
from sqlite3 import Connection, Cursor
from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, username, password) -> None:
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username) -> "User":
        connection: Connection = sqlite3.connect("data.db")
        cursor: Cursor = connection.cursor()

        query: str = "SELECT * FROM users WHERE username=?"
        result: Cursor = cursor.execute(query, (username,))
        row: List = result.fetchone()

        if row:
            user: User = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id) -> "User":
        connection: Connection = sqlite3.connect("data.db")
        cursor: Cursor = connection.cursor()

        query: str = "SELECT * FROM users WHERE id=?"
        result: Cursor = cursor.execute(query, (id,))
        row: List = result.fetchone()

        if row:
            user: "User" = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username", type=str, required=True, help="This field cannot be left blank"
    )
    parser.add_argument(
        "password", type=str, required=True, help="This field cannot be left blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"  # NULL as id
        cursor.execute(query, (data["username"], data["password"]))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
