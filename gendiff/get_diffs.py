from gendiff.get_dicts_diff import get_dicts_diff, get_dict_from_file
from gendiff.formatters import stringify, get_plain_diff
import json

Stylish = 'stylish'
Plain = 'plain'
Json = 'json'


def generate_diff(path_1, path_2, formatter=Stylish):
    dict_1 = get_dict_from_file(path_1)
    dict_2 = get_dict_from_file(path_2)
    result = get_dicts_diff(dict_1, dict_2)
    if formatter == Stylish:
        return stringify(result)
    elif formatter == Plain:
        return get_plain_diff(result)
    elif formatter == Json:
        output_json = json.dumps(result)
        return output_json
    else:
        return stringify(result)
