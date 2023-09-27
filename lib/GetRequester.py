import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
          URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

          response = requests.get(URL)
          return response.content

    def load_json(self):
        response = self.get_response_body()
        return response.json()