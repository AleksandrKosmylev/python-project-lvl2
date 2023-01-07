from gendiff.get_dicts_diff import get_dicts_diff
from gendiff.formatters.formatter_stringify import stringify
from gendiff.formatters.formatter_plain import get_plain_diff
from gendiff.utils.data_read import get_dict_from_file
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
    elif formatter not in ['stylish', 'plain', 'json']:
        raise Exception('You\'ve chosen wrong format. '
                        'Try \'stylish\', \'plain\', \'json\'')
