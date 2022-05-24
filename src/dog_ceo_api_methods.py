import requests


class DogCeoMethods:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_breeds(self):
        url = f'{self.base_url}/list/all'
        response = requests.get(url)
        response.raise_for_status()
        return response

    def get_random_image(self):
        url = f'{self.base_url}/image/random'
        response = requests.get(url)
        response.raise_for_status()
        return response

    def get_all_pictures_by_breed(self, breed):
        url = f'{self.base_url}/{breed}/images'
        response = requests.get(url)
        response.raise_for_status()
        return response

    def get_sub_breed_list(self, breed):
        url = f'{self.base_url}/{breed}/list'
        response = requests.get(url)
        response.raise_for_status()
        return response

    def get_image_by_sub_breed(self, breed, sub_breed):
        url = f'{self.base_url}/{breed}/{sub_breed}/images'
        response = requests.get(url)
        response.raise_for_status()
        return response
