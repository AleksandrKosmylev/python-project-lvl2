from gendiff.get_dicts_diff import get_dicts_diff, get_dict_from_file
from gendiff.formatter_stringify import stringify, get_plain_diff
import json


def generate_diff(path_1, path_2, formatter='stylish'):
    dict_1 = get_dict_from_file(path_1)
    dict_2 = get_dict_from_file(path_2)
    result = get_dicts_diff(dict_1, dict_2)
    if formatter == 'stylish':
        return stringify(result)
    elif formatter == 'plain':
        return get_plain_diff(result)
    elif formatter == 'json':
        output_json = json.dumps(result)
        return output_json
    else:
        return stringify(result)
"""
    else:
        raise Exception('You\'ve chosen wrong format. '
                        'Try \'stylish\', \'plain\', \'json\'')
"""
