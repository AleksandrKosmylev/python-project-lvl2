import json
import yaml


def get_dict_from_file(path_to_file):
    if path_to_file.endswith(".json") is True:
        f = json.load(open(path_to_file))
    elif path_to_file.endswith(".yaml") is True:
        f = yaml.load(open(path_to_file), Loader=yaml.FullLoader)
    return dict(f.items())


'''
# old version
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
'''

# flake8: noqa: C901
def get_dicts_difference(dict_1, dict_2):
    result = {}
    # convert dicts in sets of keys
    a = dict_1
    b = dict_2
    keys1 = set(a.keys())
    keys2 = set(b.keys())
    # unioned and sorted in alphabetical order sets
    unioned_keys = sorted(keys1 | keys2, reverse=False)
    for i in unioned_keys:
        if i in keys1 and i not in keys2:
            result["-" + i] = a[i]
        elif i in keys2 and i not in keys1:
            result["+" + i] = b[i]
        elif i in keys1 and i in keys2:
            if type(dict_1[i]) is dict and type(dict_2[i]) is dict:
                result[i] = (get_dicts_difference(a[i], b[i]))
            elif (type(dict_1[i]) is not dict) or (type(dict_2[i]) is not dict):
                if a[i] != b[i]:
                    result["-" + i] = a[i]
                    result["+" + i] = b[i]
                else:
                    result[" " + i] = a[i]
    return result


def stringify(x, spaces=' ', count=1):
    def walk(value, acc):
        if type(value) is dict:
            for i in value.keys():
                print(spaces, end="")
                if type(value[i]) is dict:
                    print(spaces * count * acc, i, ':', '{', '\n', end='')
                    acc += 1
                    walk(value[i], acc)
                    print(spaces * acc * count, '}')
                elif type(value[i]) is not dict:
                    print(spaces * count * acc, i, ':', value[i])
        elif type(value) is not dict:
            print(repr(value).replace('\'', ''))
    if type(x) is dict:
        print('{')
        return walk(x, 0), print('}')
    else:
        return walk(x, 0)
