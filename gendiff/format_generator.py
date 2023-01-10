from gendiff.diff_generator import get_dicts_diff
from gendiff.formatters.formatter_stringify import stringify
from gendiff.formatters.formatter_plain import get_plain_diff
from gendiff.formatters.formatter_json import get_json
from gendiff.utils.data_read import get_dict_from_file


def generate_diff(path_1, path_2, formatter='stylish'):
    dict_1 = get_dict_from_file(path_1)
    dict_2 = get_dict_from_file(path_2)
    diff_data = get_dicts_diff(dict_1, dict_2)
    return get_data_by_format(diff_data, formatter)


def get_data_by_format(data, formatter='stylish'):
    if formatter == 'stylish':
        return stringify(data)
    elif formatter == 'plain':
        return get_plain_diff(data)
    elif formatter == 'json':
        return get_json(data)
    else:
        raise Exception('You\'ve chosen wrong format. '
                        'Try \'stylish\', \'plain\', \'json\'')
