import pandas as pd


class MasterOutput(object):
    def __init__(self, output, output_type, output_shape):
        self._output = output
        self._output_type = output_type
        self._output_shape = output_shape

    def parse_as_dataframe(self):
        if self._output_type == ["Float"] and self._output_shape == "Single":
            if "result" in self._output.keys():
                result = self._output["result"]
                data = []
                for r in result:
                    for k,v in r.items():
                        header = k
                        data += [v]
                return pd.DataFrame({header: data})
            else:
                header = [x for x in self._output[0].keys()][0]
                data = [float(x[header]) for x in self._output]
                return pd.DataFrame({header: data})
        if self._output_type == ["String"] and self._output_shape == "Single":
            header = [x for x in self._output[0].keys()][0]
            data = [str(x[header]) for x in self._output]
            return pd.DataFrame({header: data})
        if self._output_type == ["Integer"] and self._output_shape == "Single":
            header = [x for x in self._output[0].keys()][0]
            data = [int(x[header]) for x in self._output]
            return pd.DataFrame({header: data})
        if self._output_type == ["Float"] and self._output_shape == "List":
            if type(self._output) is dict:
                if len(self._output) == 2:
                    result = self._output["result"]
                    meta = self._output["meta"]
                    if type(result[0]) is dict:
                        key = [x for x in result[0].keys()][0]
                        R = []
                        for r in result:
                            R += [r[key]]
                        return pd.DataFrame(R, columns=meta[key])
                    else:
                        raise Exception
                else:
                    raise Exception

    def parse(self):
        df = self.parse_as_dataframe()
        return df
