import pytest


def test_get_all_breeds(create_dogceo):
    response = create_dogceo.get_all_breeds()
    assert response.status_code == 200
    assert response.json()['status'] == 'success'


def test_get_random_image(create_dogceo):
    response = create_dogceo.get_random_image()
    assert response.status_code == 200
    assert response.json()['status'] == 'success'


@pytest.mark.parametrize('set_breed', ['hound'], indirect=True)
def test_get_images_by_breed(create_dogceo, set_breed):
    response = create_dogceo.get_all_pictures_by_breed(set_breed)
    assert response.status_code == 200
    images = response.json()
    assert images['status'] == 'success'
    for image in images['message']:
        assert set_breed in image


@pytest.mark.parametrize('set_sub_breed', ['boston'], indirect=True)
@pytest.mark.parametrize('set_breed', ['bulldog'], indirect=True)
def test_get_images_by_sub_breed(create_dogceo, set_breed, set_sub_breed):
    response = create_dogceo.get_image_by_sub_breed(set_breed, set_sub_breed)
    assert response.status_code == 200
    images = response.json()
    assert images['status'] == 'success'
    for image in images['message']:
        assert set_breed in image
        assert set_sub_breed in image


@pytest.mark.parametrize('set_breed', ['mastiff'], indirect=True)
def test_check_sub_breeds(create_dogceo, set_breed):
    response = create_dogceo.get_sub_breed_list(set_breed)
    assert response.status_code == 200
    sub_breed_list = response.json()
    assert sub_breed_list['status'] == 'success'
    for sub_breed in sub_breed_list['message']:
        assert sub_breed in ['bull', 'english', 'tibetan']
