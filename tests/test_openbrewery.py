import pytest


@pytest.mark.parametrize('query_param', ['bay-brewing-company-miami'])
@pytest.mark.parametrize('get_single_brewery', ['bay-brewing-company-miami'], indirect=True)
def test_get_single_brewery(get_single_brewery, query_param):
    assert get_single_brewery.status_code == 200
    assert query_param in get_single_brewery.json()['id']


@pytest.mark.parametrize('set_query_params', ['by_city=san_diego&per_page=3'], indirect=True)
def test_get_3_breweries_by_city(get_breweries):
    assert len(get_breweries.json()) == 3
    assert get_breweries.status_code == 200


@pytest.mark.parametrize('query_param', ['cooper'])
@pytest.mark.parametrize('set_query_params', ['by_name=cooper'], indirect=True)
def test_filter_breweries_by_name(get_breweries, query_param):
    assert get_breweries.status_code == 200
    breweries = get_breweries.json()
    for brewery in breweries:
        assert query_param in brewery['id']


@pytest.mark.parametrize('query_param', ['Alabama'])
@pytest.mark.parametrize('set_query_params', ['by_state=alabama'], indirect=True)
def test_filter_breweries_by_state(get_breweries, query_param):
    assert get_breweries.status_code == 200
    breweries = get_breweries.json()
    for brewery in breweries:
        assert query_param in brewery['state']


@pytest.mark.parametrize('query_param', ['California'])
@pytest.mark.parametrize('set_query_params', ['by_postal=90222'], indirect=True)
def test_filter_breweries_by_state(get_breweries, query_param):
    assert get_breweries.status_code == 200
    breweries = get_breweries.json()
    for brewery in breweries:
        assert query_param in brewery['state']


