import requests
from tools import download_img


def fetch_hubble(img_folder, collection='printshop'):
    url = 'http://hubblesite.org/api/v3/images'
    payload = {"page": "all", "collection_name": collection}
    collection_response = requests.get(url, params=payload)
    ids = [response['id'] for response in collection_response.json()]

    for img_id in ids:
        hubble_url = 'http://hubblesite.org/api/v3/image/{}'.format(img_id)
        response = requests.get(hubble_url)
        img_raw_url = response.json()['image_files'][-1]['file_url'].replace('//', 'https://')

        img_url = requests.get(img_raw_url, verify=False).url

        img_name = response.json()['name']

        filename = img_url.split('/')[-1].replace('full_jpg', img_name)

        download_img(img_url, filename, img_folder)
