import os

import connexion
import pytest
from flask_sqlalchemy import SQLAlchemy

from connection import basedir


@pytest.fixture(scope='function')
def client():
    app = connexion.App(__name__, specification_dir=basedir)
    # using a separate db for test to preserve main db
    app.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + os.path.join(basedir, "test.db")
    app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy(app.app)
    app.app.config["TESTING"] = True
    app.app.testing = True

    client = app.app.test_client()
    app.add_api('swagger.yaml')
    db.create_all()
    db.session.commit()
    yield client
    # removing test db to get fresh db next time the tests are ran
    db.session.remove()
    db.drop_all()
    os.remove('test.db')
