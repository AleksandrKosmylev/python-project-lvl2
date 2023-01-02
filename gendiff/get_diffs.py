from gendiff.get_dicts_diff import get_dicts_diff, get_dict_from_file
from gendiff.formatters import stringify, get_plain_diff
import json

# Stylish = 'stylish'
Plain = 'plain'
Json = 'json'


def generate_diff(path_1, path_2, formatter="stylish"):
    dict_1 = get_dict_from_file(path_1)
    dict_2 = get_dict_from_file(path_2)
    result = get_dicts_diff(dict_1, dict_2)
    if formatter == 'stylish':
        print(stringify(result))
        return stringify(result)
    elif formatter == Plain:
        print(get_plain_diff(result))
        return get_plain_diff(result)
    elif formatter == Json:
        output_json = json.dumps(result)
        print(output_json)
        return output_json
