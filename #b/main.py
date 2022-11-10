
import os
from ya_api_app.yandex_api_functions import YandexDisk


if __name__ == '__main__':
    token = os.environ.get("ya_t")
    data = open('1.jpg', 'rb').read()
    alb_n = 'CATS'
    file_name = 'cat_pic.jpg'

    ya_disk = YandexDisk(ya_token=token)
    ya_disk.upload_file(data, alb_n, file_name)
