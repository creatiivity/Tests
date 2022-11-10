
import requests
import sys


class YandexDisk:
    def __init__(self, ya_token):
        self.ya_token = ya_token
        self.ya_url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.ya_token}'
        }

    # create album
    def upload_album_to_disk(self, album_name):
        headers = self.get_headers()
        params = {"path": album_name}
        album_response = requests.get(self.ya_url, headers=headers, params=params)
        if album_response.status_code == 200:
            return album_response
        if album_response.status_code == 401:
            print("Authentication error")
            sys.exit()
        else:
            album_response = requests.put(self.ya_url, headers=headers, params=params)
            return album_response

    # get link for file upload
    def get_file_link(self, album_name, file_name):
        link = None
        album_response = self.upload_album_to_disk(album_name)
        if album_response.status_code == 200 or album_response.status_code == 201:
            get_link_for_file_url = f"{self.ya_url}/upload"
            headers = self.get_headers()
            params = {"path": "/" + album_name + "/" + file_name, "overwrite": "true"}
            link_res = requests.get(get_link_for_file_url, headers=headers, params=params).json()
            try:
                link = link_res['href']
                return album_response, link
            except KeyError:
                return album_response, link
        return album_response, link

    # upload file to link
    def upload_file(self, data, album_name, file_name):
        album_response, link = self.get_file_link(album_name, file_name)
        if link:
            file_creation_response = requests.put(link, data=data)
            return album_response, file_creation_response
        else:
            file_creation_response = None
            return album_response, file_creation_response
