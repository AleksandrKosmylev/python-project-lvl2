from gendiff.logic.get_dicts_diff import get_dicts_diff, get_dict_from_file
from gendiff.logic.formatters import stringify, get_plain_diff


def generate_diff(path_1, path_2, formatter='stylish'):
    dict_1 = get_dict_from_file(path_1)
    dict_2 = get_dict_from_file(path_2)
    result = get_dicts_diff(dict_1, dict_2)
    if formatter == 'stylish':
        print(stringify(result))
    elif formatter == 'plain':
        print(get_plain_diff(result))
    elif formatter == 'json':
        print(result)
