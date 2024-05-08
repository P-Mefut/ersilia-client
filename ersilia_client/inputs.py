import csv


class BaseInput(object):
    def __init__(self, input_data):
        self._input_data = input_data

    def _is_csv_file(self):
        if type(self._input_data) is not str:
            return False
        if self._input_data.endswith(".csv"):
            return True
        else:
            return False

    def _is_tsv_file(self):
        if type(self._input_data) is not str:
            return False
        if self._input_data.endswith(".tsv"):
            return True
        else:
            return False

    def _is_list(self):
        if type(self._input_data) is list:
            return True
        else:
            return False

    def _is_string_input(self):
        if type(self._input_data) is not str:
            return False
        if self._is_tsv_file():
            return False
        if self._is_csv_file():
            return False
        return True

    def _parse_onecolumn_file_as_list(self, delimiter):
        with open(self._input_data, "r") as f:
            reader = csv.reader(f, delimiter=delimiter)
            data = []
            for r in reader:
                if len(r) > 1:
                    raise Exception
                data += r
        return data

    def _parse_onecolumn_csv_as_list(self):
        return self._parse_onecolumn_file_as_list(delimiter=",")

    def _parse_onecolumn_tsv_as_list(self):
        return self._parse_onecolumn_file_as_list(delimiter="\t")

    def _parse_twocolumn_file_as_list(self, delimiter):
        with open(self._input_data, "r") as f:
            reader = csv.reader(f, delimiter=delimiter)
            data = []
            for r in reader:
                if len(r) != 2:
                    raise Exception
                data += r
        return data

    def _parse_twocolumn_csv_as_list(self):
        return self._parse_twocolumn_file_as_list(delimiter=",")

    def _parse_twocolumn_tsv_as_list(self):
        return self._parse_twocolumn_file_as_list(delimiter="\t")


class CompoundInput(BaseInput):
    def __init__(self, input_data, input_shape):
        BaseInput.__init__(self, input_data=input_data)
        self._input_shape = input_shape

    def _is_shape_single(self):
        if self._input_shape == "Single":
            return True
        else:
            return False

    def _is_shape_pair(self):
        if self._input_shape == "Pair":
            return True
        else:
            return False

    def _is_shape_list(self):
        if self._input_shape == "List":
            return True
        else:
            return False

    def _is_shape_pair_of_lists(self):
        if self._input_shape == "Pair of Lists":
            return True
        else:
            return False

    def _is_shape_list_of_lists(self):
        if self._input_shape == "List of Lists":
            return True
        else:
            return False

    def _parse_onecolumn_file(self):
        if self._is_csv_file():
            data = self._parse_onecolumn_csv_as_list()
        if self._is_tsv_file():
            data = self._parse_onecolumn_tsv_as_list()
        if data[0].lower() != "smiles":
            raise Exception
        return data[1:]

    def _parse_twocolumn_file(self):
        if self._is_csv_file():
            data = self._parse_twocolumn_csv_as_list()
        if self._is_tsv_file():
            data = self._parse_twocolumn_tsv_as_list()
        if "smiles" not in data[0][0].lower() and "smiles" not in data[0][1].lower():
            raise Exception
        return data[1:]

    def parse(self):
        if self._is_shape_single():
            if self._is_string_input():
                return [self._input_data]
            if self._is_csv_file() or self._is_tsv_file():
                return self._parse_onecolumn_file()
            if self._is_list():
                return self._input_data
            return None
        else:
            raise Exception


class MasterInput(object):
    def __init__(self, input_data, input_type, input_shape):
        if input_type == ["Compound"]:
            self.inp = CompoundInput(input_data=input_data, input_shape=input_shape)

    def parse(self):
        return self.inp.parse()
