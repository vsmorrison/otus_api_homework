import pytest
from src import dog_ceo_api_methods


@pytest.fixture(scope="module")
def set_base_urls():
    urls = {
        'dog_ceo_url': 'https://dog.ceo/api/breeds'
    }
    return urls


@pytest.fixture(scope="module")
def get_all_breeds(set_base_urls):
    dog_ceo_url = dog_ceo_api_methods.DogCeoMethods(set_base_urls['dog_ceo_url'])
    return dog_ceo_url.get_all_breeds()


@pytest.fixture(scope="module")
def get_random_image(set_base_urls):
    dog_ceo_url = dog_ceo_api_methods.DogCeoMethods(set_base_urls['dog_ceo_url'])
    return dog_ceo_url.get_random_image()


@pytest.fixture(scope="module")
def get_all_pictures_by_breed(request):
    dog_ceo_url = dog_ceo_api_methods.DogCeoMethods(set_base_urls['dog_ceo_url'])
    abc = dog_ceo_url.get_all_pictures_by_breed(request.param)
    return abc


