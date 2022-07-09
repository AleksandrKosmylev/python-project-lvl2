import json


def get_dict_from_file(path_to_file):
    f = json.load(open(path_to_file))
    return dict(f.items())


def get_dicts_difference(dict_1, dict_2):
    result = {}
    # convert dicts in sets of keys
    keys1 = set(dict_1.keys())
    keys2 = set(dict_2.keys())
    # unioned and sorted in alphabetical order sets
    unioned_keys = sorted(keys1 | keys2)
    # adding pairs if key-value in result dict
    for i in unioned_keys:
        if i in keys1 and i in keys2:
            if dict_1[i] == dict_2[i]:
                result[i] = dict_1[i]
            else:
                result['-' + i] = dict_1[i]
                result['+' + i] = dict_2[i]
        elif i in keys1 and i not in keys2:
            result['-' + i] = dict_1[i]
        else:
            result['+' + i] = dict_2[i]
#    return yaml.dump(result)
    return result
