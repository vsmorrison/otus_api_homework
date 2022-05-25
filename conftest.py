import pytest
from src import dog_ceo_api_methods
from src import openbrewery_api_methods


@pytest.fixture(scope="module")
def set_base_urls():
    urls = {
        'dog_ceo_url': 'https://dog.ceo/api',
        'openbrewery_url': 'https://api.openbrewerydb.org/breweries'
    }
    return urls


@pytest.fixture(scope="module")
def set_breed(request):
    return request.param


@pytest.fixture(scope="module")
def set_sub_breed(request):
    return request.param


@pytest.fixture(scope="module")
def set_query_params(request):
    params = request.param
    return params


@pytest.fixture(scope="module")
def get_all_breeds(set_base_urls):
    dog_ceo_url = dog_ceo_api_methods.DogCeoMethods(set_base_urls['dog_ceo_url'])
    return dog_ceo_url.get_all_breeds()


@pytest.fixture(scope="module")
def get_random_image(set_base_urls):
    dog_ceo_url = dog_ceo_api_methods.DogCeoMethods(set_base_urls['dog_ceo_url'])
    return dog_ceo_url.get_random_image()


@pytest.fixture(scope="module")
def get_images_by_breed(set_base_urls, set_breed):
    dog_ceo_url = dog_ceo_api_methods.DogCeoMethods(set_base_urls['dog_ceo_url'])
    return dog_ceo_url.get_all_pictures_by_breed(set_breed)


@pytest.fixture(scope="module")
def get_images_by_sub_breed(set_base_urls, set_breed, set_sub_breed):
    dog_ceo_url = dog_ceo_api_methods.DogCeoMethods(set_base_urls['dog_ceo_url'])
    return dog_ceo_url.get_image_by_sub_breed(set_breed, set_sub_breed)


@pytest.fixture(scope="module")
def get_single_brewery(set_base_urls, request):
    openbrewery = openbrewery_api_methods.OpenBreweryMethods(
        set_base_urls['openbrewery_url']
    )
    return openbrewery.get_single_brewery(request.param)


@pytest.fixture(scope="module")
def get_breweries(set_base_urls, set_query_params):
    openbrewery = openbrewery_api_methods.OpenBreweryMethods(
        set_base_urls['openbrewery_url']
    )
    return openbrewery.get_list_of_breweries(set_query_params)
