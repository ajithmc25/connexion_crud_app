import pytest
from flask_sqlalchemy import SQLAlchemy

from connection import connex_app
from models import User


@pytest.fixture(scope='module')
def client():
    app = connex_app.create_app()

    app.config["TESTING"] = True
    app.testing = True

    # This creates an in-memory sqlite db
    # See https://martin-thoma.com/sql-connection-strings/
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    client = app.test_client()
    db = SQLAlchemy(app)
    with app.app_context():
        db.create_all()
        user1 = User(name="Cedric")
        db.session.add(user1)
        db.session.commit()
    yield client


def test_create_users(client):
    user_data = {'name': 'William'}
    response = client.post('/users/', json=user_data)
    print(response)
    print(response.json)
    assert response.json == {'age': None, 'checked': None, 'date': None, 'description': None, 'id': 1, 'name': 'William', 'type': None}


def test_list_users_api(client):
    response = client.get('/users/')
    print(response)
    print(response.json)
    assert response.json == [{'age': None, 'checked': None, 'date': None, 'description': None, 'id': 1, 'name': 'William', 'type': None}]


# def test_retrieve_user_api(client):
#     response = client.get('/users/1/')
#     assert response.json['id'] == 1
