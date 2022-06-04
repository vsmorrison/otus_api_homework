import pytest


@pytest.mark.parametrize('post_id', ['10'])
def test_get_resource(create_jsonplaceholder, post_id):
    response = create_jsonplaceholder.get_resource(post_id)
    assert response.status_code == 200
    assert response.json()['id'] == int(post_id)


def test_create_resource(create_jsonplaceholder):
    data = {
        'title': 'Test',
        'body': 'Simple Test',
        'userId': '10'
    }
    response = create_jsonplaceholder.create_resource(data=data)
    assert response.status_code == 201
    created_data = response.json()
    assert created_data['title'] == data['title']
    assert created_data['body'] == data['body']
    assert created_data['userId'] == data['userId']


@pytest.mark.parametrize('post_id', ['50'])
def test_update_resource(create_jsonplaceholder, post_id):
    data = {
        'title': 'My Post',
        'body': 'Cute post for myself <3',
        'userId': '10',
    }
    response = create_jsonplaceholder.update_resource(post_id, data)
    assert response.status_code == 200
    updated_data = response.json()
    assert updated_data['title'] == data['title']
    assert updated_data['body'] == data['body']
    assert updated_data['userId'] == data['userId']
    assert updated_data['id'] == int(post_id)


@pytest.mark.parametrize('post_id', ['50'])
def test_delete_resource(create_jsonplaceholder, post_id):
    response = create_jsonplaceholder.delete_resource(post_id)
    assert response.status_code == 200


@pytest.mark.parametrize('set_query_params', ['userId=9'], indirect=True)
def test_filter_resources(create_jsonplaceholder, set_query_params):
    response = create_jsonplaceholder.get_all_resources(set_query_params)
    assert response.status_code == 200
    posts = response.json()
    for post in posts:
        assert post['userId'] == 9
