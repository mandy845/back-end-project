import hmac
import sqlite3
import datetime

from flask_cors import CORS

from flask import Flask, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity


def init_user_table():
    conn = sqlite3.connect('blog.db')
    print("Opened database successfully")

    conn.execute("CREATE TABLE IF NOT EXISTS user(user_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                 "first_name TEXT NOT NULL,"
                 "last_name TEXT NOT NULL,"
                 "username TEXT NOT NULL,"
                 "password TEXT NOT NULL)")
    print("user table created successfully")
    conn.close()

