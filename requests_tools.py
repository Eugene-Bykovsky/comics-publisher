from random import randint
from urllib.parse import urlparse

import requests

from constants import XKCD_URL


def get_response(url, params=None):
    response = requests.get(url, params)
    response.raise_for_status()
    return response


def fetch_latest_comic():
    return get_response(XKCD_URL).json()


def fetch_random_comic():
    parsed_url = urlparse(XKCD_URL)
    latest_comic = fetch_latest_comic()
    latest_num = latest_comic.get('num')
    random_comic_num = randint(1, latest_num)
    comics_url = (f'{parsed_url.scheme}://{parsed_url.netloc}/'
                  f'{random_comic_num}'
                  f'{parsed_url.path}')
    return get_response(comics_url).json()
