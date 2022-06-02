import pytest
from src import dog_ceo_api_methods
from src import openbrewery_api_methods
from src import jsonplaceholder_api_methods


@pytest.fixture(scope="module")
def set_base_urls():
    urls = {
        'dog_ceo_url': 'https://dog.ceo/api',
        'openbrewery_url': 'https://api.openbrewerydb.org/breweries',
        'jsonplaceholder_url': 'https://jsonplaceholder.typicode.com'
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
def create_dogceo(set_base_urls):
    dogceo = dog_ceo_api_methods.DogCeoMethods(
        set_base_urls['dog_ceo_url']
    )
    return dogceo


@pytest.fixture(scope="module")
def create_openbrewery(set_base_urls):
    openbrewery = openbrewery_api_methods.OpenBreweryMethods(
        set_base_urls['openbrewery_url']
    )
    return openbrewery


@pytest.fixture(scope="module")
def create_jsonplaceholder(set_base_urls):
    jsonplaceholder = jsonplaceholder_api_methods.JsonPlaceholderMethods(
        set_base_urls['jsonplaceholder_url']
    )
    return jsonplaceholder
