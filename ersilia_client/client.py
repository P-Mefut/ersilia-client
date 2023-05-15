import requests
import json


class ErsiliaClient(object):

    def __init__(self, url):
        self.url = url

    def info(self):
        url = self.url+"/info"
        requests.get(url)
        return data

    def run(self, input):
        pass

        return data

