import json
import yaml

# flake8: noqa: C901
output_path = "gendiff/output.json"


def get_dict_from_file(path_to_file):
    if path_to_file.endswith(".json") is True:
        f = json.load(open(path_to_file))
        return dict(f.items())
    elif path_to_file.endswith(".yaml") is True:
        f = yaml.load(open(path_to_file), Loader=yaml.FullLoader)
        return dict(f.items())
    elif path_to_file.endswith(".yml") is True:
        f = yaml.load(open(path_to_file), Loader=yaml.FullLoader)
        return dict(f.items())
    else:
        return {}


def sigh(mark):
    if mark == 'was added':
        return '+'
    elif mark == 'was removed':
        return '-'
    elif mark == 'no changes':
        return ' '
    elif mark == 'was updated':
        return ' '


def get_dicts_diff(dict_1, dict_2):
    result = {}
    a = dict_1
    b = dict_2
    # convert dicts in sets of keys
    keys1 = set(a.keys())
    keys2 = set(b.keys())
    # unioned and sorted in alphabetical order sets
    unioned_keys = sorted(keys1 | keys2, reverse=False)
    removed = 'was removed'
    added = 'was added'
    for i in unioned_keys:
        if i in keys1 and i not in keys2:
            result[i] = {
                'type': removed,
                'value': a[i],
                'childs': "",
                "old_value": a[i]}
            if type(a[i]) is dict:
                result[i] = {
                    'type': removed,
                    'value': "", 'childs': a[i],
                    "old_value": a[i]
                }
            elif type(a[i]) is not dict:
                result[i] = {
                    'type': removed,
                    'value': "", 'childs': "",
                    "old_value": a[i]
                }
        elif i in keys2 and i not in keys1:
            if type(b[i]) is dict:
                result[i] = {
                    'type': added,
                    'value': b[i], 'childs': b[i],
                    "old_value": ""
                }
            else:
                result[i] = {
                    'type': added,
                    'value': b[i], 'childs': "",
                    "old_value": ""
                }
        elif i in keys1 and i in keys2:
            if (type(a[i]) is dict) is True and (type(b[i]) is dict) is True:
                result[i] = (get_dicts_diff(a[i], b[i]))
            elif (type(a[i]) is dict) is False or (type(b[i]) is dict) is False:
                if a[i] != b[i]:
                    if (type(a[i]) is dict) and (type(b[i]) is dict):
                        result[i] = {'type': 'was updated',
                                     'value': b[i], 'childs': '[**]',
                                     "old_value": a[i]}
                    elif (type(a[i]) is not dict) and (type(b[i]) is dict):
                        result[i] = {'type': 'was updated',
                                     'value': b[i], 'childs': '[_*]',
                                     "old_value": a[i]
                                     }
                    elif (type(a[i]) is dict) and (type(b[i]) is not dict):
                        result[i] = {'type': 'was updated',
                                     'value': b[i], 'childs': '[*_]',
                                     "old_value": a[i]}
                    elif (type(a[i]) is not dict) and (type(b[i]) is not dict):
                        result[i] = {'type': 'was updated',
                                     'value': b[i], 'childs': '[__]',
                                     "old_value": a[i]}
                else:
                    result[i] = {
                        'type': 'no changes',
                        'value': b[i],
                        'childs': "",
                        "old_value": a[i]
                    }
    return result
