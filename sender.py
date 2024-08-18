import requests

import configuration
import data

def create_order(body):
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER
    return requests.post(url=url, json=body, headers=data.headers)

def get_order_by(track):
    url = configuration.URL_SERVICE + configuration.GET_ORDER + f"?t={track}"
    return requests.get(url=url, headers=data.headers)
