import json
import yaml
# flake8: noqa: C901


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


Removed = 'was removed'
Added = 'was added'
Updated = 'was updated'
Both_dict = 'both_dict'
No_changes = 'no changes'


def sign(mark):
    if mark == Added:
        return '+ '
    elif mark == Removed:
        return '- '
    elif mark == No_changes:
        return '  '
    elif mark == Updated:
        return '- '
    elif mark == Both_dict:
        return '  '
    else:
        return '  '


def get_dicts_diff(in_1, in_2):
    def walk(dict_1, dict_2, result):
        a = dict_1
        b = dict_2
        keys1 = set(a.keys())
        keys2 = set(b.keys())
        unioned_keys = sorted(keys1 | keys2, reverse=False)
        for i in unioned_keys:
            if i in keys2 and i not in keys1:
                result[i] = {
                    'type': Added,
                    'value': b[i],
                    'childs': "",
                    "old_value": ""
                }
            elif i in keys1 and i not in keys2:
                result[i] = {
                    'type': Removed,
                    'value': "",
                    'childs': "",
                    "old_value": a[i]
                }
            elif i in keys1 and i in keys2:
                if ((type(a[i]) is dict) and (type(b[i]) is dict)) is True:
                    result[i] = {
                        'type': Both_dict,
                        'value': "",
                        'childs': walk(a[i], b[i], {}),
                        "old_value": ""
                    }
                elif (type(a[i]) is dict) is False\
                        or (type(b[i]) is dict) is False:
                    if a[i] != b[i]:
                        result[i] = {
                            'type': Updated,
                            'value': {i: {
                                'type': Added,
                                'value': b[i],
                                'childs': "",
                                "old_value": ""
                            }},
                            'childs': "",
                            "old_value": a[i]
                        }
                    else:
                        result[i] = {
                            'type': No_changes,
                            'value': b[i],
                            'childs': "",
                            "old_value": a[i]
                        }
        return result
    return walk(in_1, in_2, {})