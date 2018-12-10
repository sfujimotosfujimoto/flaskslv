import sqlite3
from sqlite3 import Connection, Cursor
from typing import List
from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password) -> None:
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username) -> "UserModel":
        connection: Connection = sqlite3.connect("data.db")
        cursor: Cursor = connection.cursor()

        query: str = "SELECT * FROM users WHERE username=?"
        result: Cursor = cursor.execute(query, (username,))
        row: List = result.fetchone()

        if row:
            user: UserModel = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id) -> "UserModel":
        connection: Connection = sqlite3.connect("data.db")
        cursor: Cursor = connection.cursor()

        query: str = "SELECT * FROM users WHERE id=?"
        result: Cursor = cursor.execute(query, (id,))
        row: List = result.fetchone()

        if row:
            user: "UserModel" = cls(*row)
        else:
            user = None

        connection.close()
        return user

