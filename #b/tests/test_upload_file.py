
import os
import unittest
from parameterized import parameterized
from TearDown import tear_down
from ya_api_app.yandex_api_functions import YandexDisk


FIXTURES1 = [("Upload Folder", "Upload File"),
             ("Image Folder", "Cat file")]

FIXTURES2 = [("New folder1///", "New cat image"),
             ("Images Folder 1", "///Cat"),
             ("///Images3", "///New Cat5")]


data = open('1.jpg', 'rb').read()


class TestFunctions(unittest.TestCase):
    @parameterized.expand(FIXTURES1)
    def test_upload_file1(self, album_name, file_name):
        token = os.environ.get("ya_t")
        ya_disk = YandexDisk(ya_token=token)
        album_response, file_creation_response = ya_disk.upload_file(data, album_name, file_name)
        self.assertEqual(file_creation_response.status_code, 201)

        if album_response.status_code == 201:
            tear_down(album_name)
        else:
            name_path = "/" + album_name + "/" + file_name
            tear_down(name_path)

    @parameterized.expand(FIXTURES2)
    def test_upload_file2(self, album_name, file_name):
        token = os.environ.get("ya_t")
        ya_disk = YandexDisk(ya_token=token)
        album_response, file_creation_response = ya_disk.upload_file(data, album_name, file_name)
        self.assertEqual(None, file_creation_response)

        if album_response.status_code == 201:
            tear_down(album_name)

    def test_upload_file3(self, album_name="album_name", file_name="file_name"):
        token = os.environ.get("wrong_token")
        ya_disk = YandexDisk(ya_token=token)
        self.assertRaises(SystemExit, ya_disk.upload_file, data, album_name, file_name)
