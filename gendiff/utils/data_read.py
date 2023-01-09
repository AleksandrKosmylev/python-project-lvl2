import json
import yaml


def get_extension(file):
    return file.split('.')[1]


def get_data_from_file(path_to_file):
    if get_extension(path_to_file) == "json":
        data = json.load(open(path_to_file))
    elif get_extension(path_to_file) in ("yaml", "yml"):
        data = yaml.load(open(path_to_file), Loader=yaml.FullLoader)
    else:
        raise Exception("Wrong file format")
    return data


def get_dict_from_file(data):
    file = get_data_from_file(data)
    result = dict(file.items())
    return result
