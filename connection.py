# import datetime

# from flask import Flask, request
import os

import connexion
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.exc import NoResultFound
# from marshmallow import Schema, fields, ValidationError, pre_load

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/user.db"
# db = SQLAlchemy(app)

# app.run(debug=True, port=8080)


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = "sqlite:////" + os.path.join(basedir, "user.db")

connex_app = connexion.App(__name__, specification_dir=basedir)
app = connex_app.app

app.config["SQLALCHEMY_DATABASE_URI"] = db_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
