from gendiff.utils.constants import Removed, Added, Updated, Both_dict, No_changes
# flake8: noqa: C901


def get_dicts_diff(data_1, data_2):
    def walk(dict_1, dict_2, result):
        keys1 = set(dict_1.keys())
        keys2 = set(dict_2.keys())
        unioned_keys = sorted(keys1 | keys2, reverse=False)
        for key in unioned_keys:
            if key in keys2 and key not in keys1:
                result[key] = {
                    'type': Added,
                    'value': dict_2[key],
                    'childs': "",
                    "old_value": ""
                }
            elif key in keys1 and key not in keys2:
                result[key] = {
                    'type': Removed,
                    'value': "",
                    'childs': "",
                    "old_value": dict_1[key]
                }
            else:
                if isinstance(dict_1[key], dict) \
                        and isinstance(dict_2[key], dict):
                    result[key] = {
                        'type': Both_dict,
                        'value': "",
                        'childs': walk(dict_1[key], dict_2[key], {}),
                        "old_value": ""
                    }
                else:
                    if dict_1[key] != dict_2[key]:
                        result[key] = {
                            'type': Updated,
                            'value': {key: {
                                'type': Added,
                                'value': dict_2[key],
                                'childs': "",
                                "old_value": ""
                            }},
                            'childs': "",
                            "old_value": dict_1[key]
                        }
                    else:
                        result[key] = {
                            'type': No_changes,
                            'value': dict_2[key],
                            'childs': "",
                            "old_value": dict_1[key]
                        }
        return result
    return walk(data_1, data_2, {})
