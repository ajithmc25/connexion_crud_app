def test_create_users(client):
    # CREATE
    user_data = {'name': 'William'}
    response = client.post('/users/', json=user_data)
    assert response.json == {'age': None, 'checked': None, 'date': None, 'description': None, 'id': 1, 'name': 'William', 'type': None}


def test_create_user_with_same_name(client):
    # CREATE
    user_data = {'name': 'William'}
    response = client.post('/users/', json=user_data)
    assert response.json['detail'] == 'User William exists already'


def test_list_users_api(client):
    # READ
    response = client.get('/users/')
    print(response.json)
    assert response.json == [{'age': None, 'checked': None, 'date': None, 'description': None, 'id': 1, 'name': 'William', 'type': None}]


def test_retrieve_user_api(client):
    # READ
    response = client.get('/users/1/')
    assert response.json['id'] == 1


def test_update_user_api(client):
    # UPDATE
    user_data = {'checked': True}
    response = client.patch('/users/1/', json=user_data)
    assert response.json['checked'] is True


def test_update_invalid_user(client):
    # UPDATE
    user_data = {'checked': True}
    response = client.patch('/users/10/', json=user_data)
    assert response.json['detail'] == 'User not found for Id: 10'


def test_delete_user_api(client):
    # DELETE
    response = client.delete('/users/1/')
    assert response.status == '200 OK'


def test_delete_invalid_user(client):
    # DELETE
    response = client.delete('/users/10/')
    assert response.json['detail'] == 'User not found for Id: 10'
