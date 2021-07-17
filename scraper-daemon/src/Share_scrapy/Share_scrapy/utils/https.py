import requests

def post(url, body): 
    # need to add return
    # so that my code finds out that it was successfull
    # needs to be a promise
    # needs to be async otherwise too slow
    headers = {'content-type': 'application/json'}
    requests.post(url, data = body, headers=headers)


def get(url):
    return requests.get(url)


def put(url, body):
    headers = {'content-type': 'application/json'}
    return requests.put(url, data = body, headers=headers)
    