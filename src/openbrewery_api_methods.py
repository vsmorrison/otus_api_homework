import requests


class OpenBreweryMethods:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_single_brewery(self, brewery):
        url = f'{self.base_url}/{brewery}'
        response = requests.get(url)
        response.raise_for_status()
        return response

    def get_list_of_breweries(self, payload=None):
        url = f'{self.base_url}'
        response = requests.get(url, payload)
        response.raise_for_status()
        return response

    def search_breweries(self, payload=None):
        url = f'{self.base_url}/search'
        response = requests.get(url, payload)
        response.raise_for_status()
        return response

    def search_breweries_w_autocomplete(self, payload=None):
        url = f'{self.base_url}/autocomplete'
        response = requests.get(url, payload)
        response.raise_for_status()
        return response
