import pytest

from server import connex_app


class TestConnexion:
    """The base test providing auth and flask clients to other tests
    """

    @pytest.fixture(scope='session')
    def client(self):
        connex_app.app.config.update({
            "TESTING": True,
        })
        with connex_app.app.test_client() as c:
            yield c
