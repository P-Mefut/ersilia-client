import requests
import json


class ErsiliaClient(object):

    def __init__(self, model_id=None, url=None):
        self.url = url
        self.model_id = model_id
        self.info = self._info()

    def _info(self):
        url = self.url+"/info"
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json"
        }
        data = "{}"
        response = requests.post(url, headers=headers, data=data)
        return response.text

    def _detect_input_type(self, input_data):
        if type(input_data) is str:
            if input_data.endswith(".csv"):
                return "csv"
            if input_data.endswith(".tsv"):
                return "tsv"
            return None
        else:
            return "list"
        
    def _serialize_to_json(self, input_data):
        json_data = [{"input": x} for x in input_data]
        return json_data

    def _post(self, input_data):
        url = self.url+"/calculate" # TODO: change to /run
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, json=input_data)
        return response.text

    def run(self, input_data):
        input_type = self._detect_input_type(input_data=input_data)
        input_data = self._serialize_to_json(input_data=input_data)
        result = self._post(input_data=input_data)
        return result
    

if __name__ == "__main__":
    ec = ErsiliaClient(url="http://localhost:32769")
    r = ec.run(["CCCCOCCC"])
    print(r)
