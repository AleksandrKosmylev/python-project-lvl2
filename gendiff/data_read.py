import json
import yaml


def get_dict_from_file(path_to_file):
    if path_to_file.endswith(".json"):
        f = json.load(open(path_to_file))
        return dict(f.items())
    elif path_to_file.endswith(".yaml") or \
            path_to_file.endswith(".yml"):
        f = yaml.load(open(path_to_file), Loader=yaml.FullLoader)
        return dict(f.items())
    else:
        return {}
