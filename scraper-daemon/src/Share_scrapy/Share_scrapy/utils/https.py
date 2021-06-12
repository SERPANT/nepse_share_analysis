import requests

def post(url, headers, body): 
    # need to add return
    # so that my code finds out that it was successfull
    # needs to be a promise
    # needs to be async otherwise too slow
    requests.post(url, data = body)

