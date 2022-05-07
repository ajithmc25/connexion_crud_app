from datetime import datetime

from models import User


def test_new_user():
    user = User(id=1, checked=True, name='John Wick', type='Admin', age=29, description='Sample description', date=datetime.now())
    assert user.id == 1
    assert user.checked is True
    assert user.name == 'John Wick'
    assert user.type == 'Admin'
    assert user.age == 29
    assert user.description == 'Sample description'
    assert type(user.date) == datetime
