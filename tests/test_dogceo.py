import pytest


def test_get_all_breeds(get_all_breeds):
    assert get_all_breeds.status_code == 200


def test_get_random_image(get_random_image):
    assert get_random_image.status_code == 200


@pytest.mark.parametrize('get_all_pictures_by_breed', ['boxer'])
def test_get_all_pictures_by_breed(get_all_pictures_by_breed):
    print(get_all_pictures_by_breed)
    assert get_all_pictures_by_breed.status_code == 200

