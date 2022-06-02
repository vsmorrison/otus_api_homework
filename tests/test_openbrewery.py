import pytest


@pytest.mark.parametrize('brewery', ['bay-brewing-company-miami'])
def test_get_single_brewery(create_openbrewery, brewery):
    response = create_openbrewery.get_single_brewery(brewery)
    assert response.status_code == 200
    assert brewery in response.json()['id']


@pytest.mark.parametrize('expect', ['San Diego'])
@pytest.mark.parametrize('set_query_params', ['by_city=san_diego&per_page=3'], indirect=True)
def test_get_3_breweries_by_city(create_openbrewery, set_query_params, expect):
    response = create_openbrewery.get_list_of_breweries(set_query_params)
    assert response.status_code == 200
    assert len(response.json()) == 3
    breweries = response.json()
    for brewery in breweries:
        assert brewery['city'] == expect


@pytest.mark.parametrize('expect', ['cooper'])
@pytest.mark.parametrize('set_query_params', ['by_name=cooper'], indirect=True)
def test_filter_breweries_by_name(create_openbrewery, set_query_params, expect):
    response = create_openbrewery.get_list_of_breweries(set_query_params)
    assert response.status_code == 200
    breweries = response.json()
    for brewery in breweries:
        assert expect in brewery['id']


@pytest.mark.parametrize('expect', ['Alabama'])
@pytest.mark.parametrize('set_query_params', ['by_state=alabama'], indirect=True)
def test_filter_breweries_by_state(create_openbrewery, set_query_params, expect):
    response = create_openbrewery.get_list_of_breweries(set_query_params)
    assert response.status_code == 200
    breweries = response.json()
    for brewery in breweries:
        assert expect in brewery['state']


@pytest.mark.parametrize('expect', ['California'])
@pytest.mark.parametrize('set_query_params', ['by_postal=90222'], indirect=True)
def test_filter_breweries_by_state(create_openbrewery, set_query_params, expect):
    response = create_openbrewery.get_list_of_breweries(set_query_params)
    assert response.status_code == 200
    breweries = response.json()
    for brewery in breweries:
        assert expect in brewery['state']
