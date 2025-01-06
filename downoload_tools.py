from requests_tools import get_response


def download_image(url, save_path, params=None):
    response = get_response(url, params)
    with open(save_path, 'wb') as f:
        f.write(response.content)
