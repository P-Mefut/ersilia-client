import requests
import json
import pandas as pd

from inputs import MasterInput
from outputs import MasterOutput


class ErsiliaClient(object):
    def __init__(self, model_id=None, url=None):
        self.url = url
        self.model_id = model_id
        self.info = self._info()

    def _info(self):
        url = self.url + "/info"
        headers = {"accept": "*/*", "Content-Type": "application/json"}
        data = "{}"
        response = requests.post(url, headers=headers, data=data)
        return json.loads(response.text)

    def _serialize_to_json(self, input_data):
        json_data = [{"input": x} for x in input_data]
        return json_data

    def _post(self, input_data):
        url = self.url + "/run"  # TODO: change to /run
        headers = {"accept": "*/*", "Content-Type": "application/json"}
        response = requests.post(url, headers=headers, json=input_data)
        return json.loads(response.text)

    def run(self, input_data):
        input_type = self.info["metadata"]["Input"]
        input_shape = self.info["metadata"]["Input Shape"]
        output_type = self.info["metadata"]["Output Type"]
        output_shape = self.info["metadata"]["Output Shape"]
        input_data = MasterInput(
            input_data=input_data, input_type=input_type, input_shape=input_shape
        ).parse()
        input_data_json = self._serialize_to_json(input_data=input_data)
        result = self._post(input_data=input_data_json)
        output_data = MasterOutput(
            output=result, output_shape=output_shape, output_type=output_type
        ).parse()
        result = pd.DataFrame({"input": input_data})
        return pd.concat([result, output_data], axis=1)


if __name__ == "__main__":
    ec = ErsiliaClient(url="http://localhost:32772")
    r = ec.run(["CCCCOCCCCC", "CCCOCCC"])
    print(r)
