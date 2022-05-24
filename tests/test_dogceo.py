import pytest


def test_get_all_breeds(get_all_breeds):
    assert get_all_breeds.status_code == 200


def test_get_random_image(get_random_image):
    assert get_random_image.status_code == 200


@pytest.mark.parametrize('set_breed', ['boxer'], indirect=True)
def test_get_images_by_breed(get_images_by_breed):
    assert get_images_by_breed.status_code == 200


@pytest.mark.parametrize('set_sub_breed', ['boston'], indirect=True)
@pytest.mark.parametrize('set_breed', ['bulldog'], indirect=True)
def test_get_images_by_sub_breed(get_images_by_sub_breed):
    assert get_images_by_sub_breed.status_code == 200
