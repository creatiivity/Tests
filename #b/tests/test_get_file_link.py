
import os
import re
import unittest
from parameterized import parameterized
from TearDown import tear_down
from ya_api_app.yandex_api_functions import YandexDisk


FIXTURES1 = [("New folder 100", "New image File 1"),
             ("Images 99", "Cat 15")]

FIXTURES2 = [("//New folder_4", "//New image_22"),
             ("Image999", "//Cat301"),
             ("//New folder1212", "Cat554")]

URL_PATTERN = re.compile(r'(https://)*(disk.yandex.net:443/upload-target)*', re.IGNORECASE)


class TestFunctions(unittest.TestCase):
    @parameterized.expand(FIXTURES1)
    def test_get_file_link1(self, album_name, file_name):
        token = os.environ.get("ya_t")
        ya_disk = YandexDisk(ya_token=token)
        album_response, link = ya_disk.get_file_link(album_name, file_name)
        self.assertTrue(URL_PATTERN.match(link))

        if album_response.status_code == 201:
            tear_down(album_name)

    @parameterized.expand(FIXTURES2)
    def test_get_file_link2(self, album_name, file_name):
        token = os.environ.get("ya_t")
        ya_disk = YandexDisk(ya_token=token)
        album_response, link = ya_disk.get_file_link(album_name, file_name)
        self.assertEqual(link, None)

        if album_response.status_code == 201:
            tear_down(album_name)

    def test_get_file_link3(self, album_name="album_name", file_name="file_name"):
        token = os.environ.get("wrong_token")
        ya_disk = YandexDisk(ya_token=token)
        self.assertRaises(SystemExit, ya_disk.get_file_link, album_name, file_name)
