import json
import yaml


def get_file_extension(path_to_file):
    if path_to_file.endswith(".json"):
        f = json.load(open(path_to_file))
    elif path_to_file.endswith(".yaml") or \
            path_to_file.endswith(".yml"):
        f = yaml.load(open(path_to_file), Loader=yaml.FullLoader)
    else:
        f = {}
    return f


def get_dict_from_file(f):
    file = get_file_extension(f)
    result = dict(file.items())
    return result
