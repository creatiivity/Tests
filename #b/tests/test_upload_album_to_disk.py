
import os
import unittest
from parameterized import parameterized
from TearDown import tear_down
from ya_api_app.yandex_api_functions import YandexDisk


FIXTURES1 = [('New folder55'),
             ('Images7')]

FIXTURES2 = [('New folder30///'),
             ('///Images4')]


class TestFunctions(unittest.TestCase):
    @parameterized.expand(FIXTURES1)
    def test_upload_album_to_disk1(self, album_name):
        token = os.environ.get("ya_t")
        ya_disk = YandexDisk(ya_token=token)
        album_response = ya_disk.upload_album_to_disk(album_name)
        try:
            self.assertEqual(200, album_response.status_code)
        except AssertionError:
            self.assertEqual(201, album_response.status_code)

        if album_response.status_code == 201:
            tear_down(album_name)

    @parameterized.expand(FIXTURES2)
    def test_upload_album_to_disk2(self, album_name):
        token = os.environ.get("ya_t")
        ya_disk = YandexDisk(ya_token=token)
        album_response = ya_disk.upload_album_to_disk(album_name)
        self.assertEqual(404, album_response.status_code)

    def test_upload_album_to_disk3(self, album_name="album_name"):
        token = os.environ.get("wrong_token")
        ya_disk = YandexDisk(ya_token=token)
        self.assertRaises(SystemExit, ya_disk.upload_album_to_disk, album_name)
