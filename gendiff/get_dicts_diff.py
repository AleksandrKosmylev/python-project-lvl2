import json
import yaml
# flake8: noqa: C901


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
        keys1 = set(dict_1.keys())
        keys2 = set(dict_2.keys())
        unioned_keys = sorted(keys1 | keys2, reverse=False)
        for i in unioned_keys:
            if i in keys2 and i not in keys1:
                result[i] = {
                    'type': Added,
                    'value': dict_2[i],
                    'childs': "",
                    "old_value": ""
                }
            elif i in keys1 and i not in keys2:
                result[i] = {
                    'type': Removed,
                    'value': "",
                    'childs': "",
                    "old_value": dict_1[i]
                }
            elif i in keys1 and i in keys2:
                if ((type(dict_1[i]) is dict) and (type(dict_2[i]) is dict)) is True:
                    result[i] = {
                        'type': Both_dict,
                        'value': "",
                        'childs': walk(dict_1[i], dict_2[i], {}),
                        "old_value": ""
                    }
                elif (type(dict_1[i]) is dict) is False\
                        or (type(dict_2[i]) is dict) is False:
                    if dict_1[i] != dict_2[i]:
                        result[i] = {
                            'type': Updated,
                            'value': {i: {
                                'type': Added,
                                'value': dict_2[i],
                                'childs': "",
                                "old_value": ""
                            }},
                            'childs': "",
                            "old_value": dict_1[i]
                        }
                    else:
                        result[i] = {
                            'type': No_changes,
                            'value': dict_2[i],
                            'childs': "",
                            "old_value": dict_1[i]
                        }
        return result
    return walk(in_1, in_2, {})
