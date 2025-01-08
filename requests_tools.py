from random import randint
from urllib.parse import urlparse

import requests

from constants import XKCD_URL


def fetch_random_comic():
    latest_comic_response = requests.get(XKCD_URL)
    latest_comic_response.raise_for_status()
    latest_comic = latest_comic_response.json()

    latest_num = latest_comic.get('num')
    random_comic_num = randint(1, latest_num)

    parsed_url = urlparse(XKCD_URL)
    random_comic_url = (f'{parsed_url.scheme}://{parsed_url.netloc}/'
                        f'{random_comic_num}'
                        f'{parsed_url.path}')

    random_comic_response = requests.get(random_comic_url)
    random_comic_response.raise_for_status()
    return random_comic_response
