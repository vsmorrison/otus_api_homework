import pytest
from src import dog_ceo_api_methods
from src import openbrewery_api_methods
from src import jsonplaceholder_api_methods
from src import custom_url_methods


@pytest.fixture(scope="module")
def set_base_urls():
    urls = {
        'dog_ceo_url': 'https://dog.ceo/api',
        'openbrewery_url': 'https://api.openbrewerydb.org/breweries',
        'jsonplaceholder_url': 'https://jsonplaceholder.typicode.com/posts'
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


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )
    parser.addoption(
        "--status_code",
        default=200,
        help="This is status code"
    )


@pytest.fixture(scope="module")
def get_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def get_status_code(request):
    return request.config.getoption("--status_code")


@pytest.fixture(scope="module")
def make_get_request(get_url):
    return custom_url_methods.make_get_request(get_url)
