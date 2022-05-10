import pytest

from connection import connex_app


@pytest.fixture(scope='module')
def client():
    test_app = connex_app

    # configure the DB
    # in-memory sqlite DB for development purposes, will need file backing for persistence
    test_app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    test_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from connection import db
    db.init_app(test_app.app)
    test_app.add_api('swagger.yaml')

    # create DB tables
    with test_app.app.app_context():
        db.create_all()

    test_app.app.config['DEBUG'] = True
    test_app.app.config['TESTING'] = True
    with test_app.app.test_client() as c:
        yield c
