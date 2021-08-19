import requests

def get(url, headers = {}):
    return requests.get(url, headers=headers)
