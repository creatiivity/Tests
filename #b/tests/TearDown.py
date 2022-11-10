
import os
import requests
from ya_api_app.yandex_api_functions import YandexDisk


def tear_down(name):
    token = os.environ.get("ya_t")
    ya_disk = YandexDisk(ya_token=token)
    headers = ya_disk.get_headers()
    params = {"path": name, "force_async": False, "permanently": False}
    requests.delete(ya_disk.ya_url, headers=headers, params=params)
