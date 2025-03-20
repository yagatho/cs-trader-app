# Basic RECT requests

import requests


def get_json(url: str, err: dict, params: dict, headers: dict):
    """ Basic RECT get request """

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    if response.status_code in err:
        print(err[response.status_code])

    return response.json()
