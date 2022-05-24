import requests


class JsonPlaceholderMethods:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_resource(self, post_id=None):
        url = f'{self.base_url}/{post_id}'
        response = requests.get(url)
        response.raise_for_status()
        return response

    def create_resource(self, data=None, json=None):
        url = f'{self.base_url}'
        response = requests.post(url, data, json)
        response.raise_for_status()
        return response

    def update_resource(self, post_id=None, data=None):
        url = f'{self.base_url}/{post_id}'
        response = requests.put(url, data)
        response.raise_for_status()
        return response

    def patch_resource(self, post_id=None, data=None):
        url = f'{self.base_url}/{post_id}'
        response = requests.patch(url, data)
        response.raise_for_status()
        return response

    def delete_resource(self, post_id=None):
        url = f'{self.base_url}/{post_id}'
        response = requests.delete(url)
        response.raise_for_status()
        return response
