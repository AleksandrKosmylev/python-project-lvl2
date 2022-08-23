import json
import yaml


def get_dict_from_file(path_to_file):
    if path_to_file.endswith(".json") is True:
        f = json.load(open(path_to_file))
        return dict(f.items())
    elif path_to_file.endswith(".yaml") is True:
        f = yaml.load(open(path_to_file), Loader=yaml.FullLoader)
        return dict(f.items())


def sigh(mark):
    if mark == 'was added':
        return '+'
    elif mark == 'was removed':
        return '-'
    elif mark == 'no changes':
        return ' '
    elif mark == 'was updated':
        return ' '


def get_dicts_difference(dict_1, dict_2):
    result = {}
    a = dict_1
    b = dict_2
    # convert dicts in sets of keys
    keys1 = set(a.keys())
    keys2 = set(b.keys())
    # unioned and sorted in alphabetical order sets
    unioned_keys = sorted(keys1 | keys2, reverse=False)
    for i in unioned_keys:
        if i in keys1 and i not in keys2:
            result[i] = {'status': 'was removed', 'value': a[i], 'childs': "", "old_value": a[i]}
            if type(a[i]) is dict:
                result[i] = {'status': 'was removed', 'value': "", 'childs': a[i], "old_value": a[i]}
            elif type(a[i]) is not dict:
                result[i] = {'status': 'was removed', 'value': "", 'childs': "", "old_value": a[i]}
        elif i in keys2 and i not in keys1:
            if type(b[i]) is dict:
                result[i] = {'status': 'was added', 'value': b[i], 'childs': b[i], "old_value": ""}
            else:
                result[i] = {'status': 'was added', 'value': b[i], 'childs': "", "old_value": ""}
        elif i in keys1 and i in keys2:
            if (type(a[i]) is dict) is True and (type(b[i]) is dict) is True:
                result[i] = (get_dicts_difference(a[i], b[i]))
            elif (type(a[i]) is dict) is False or (type(b[i]) is dict) is False:
                if a[i] != b[i]:
                    if (type(a[i]) is dict) and (type(b[i]) is dict):
                        result[i] = {'status': 'was updated', 'value': b[i], 'childs': '[**]', "old_value": a[i]}
                    elif (type(a[i]) is not dict) and (type(b[i]) is dict):
                        result[i] = {'status': 'was updated', 'value': b[i], 'childs': '[_*]', "old_value": a[i]}
                    elif (type(a[i]) is dict) and (type(b[i]) is not dict):
                        result[i] = {'status': 'was updated', 'value': b[i], 'childs': '[*_]', "old_value": a[i]}
                    elif (type(a[i]) is not dict) and (type(b[i]) is not dict):
                        result[i] = {'status': 'was updated', 'value': b[i], 'childs': '[__]', "old_value": a[i]}
                else:
                    result[i] = {'status': 'no changes', 'value': b[i], 'childs': "", "old_value": a[i]}
    return result


def stringify(x, spaces=' ', count=1):
    def walk(value, acc):
        tabulation = spaces * count * acc
        keys_of_tree = ['status', 'value', 'childs', 'old_value']
        if type(value) is dict:
            for key_of_dict in value.keys():
                if type(value[key_of_dict]) is dict and keys_of_tree != list(value[key_of_dict].keys()):
                    print(tabulation, key_of_dict, ": {")
                    acc += 1
                    walk(value[key_of_dict], acc)
                elif type(value[key_of_dict]) is dict and keys_of_tree == list(value[key_of_dict].keys()):
                    status_value = list(value[key_of_dict].values())[0]
                    # branches that depend on status
                    # was added.
                    # check children: if no childs.
                    # list(value[key_of_dict].values())[2] == 'childs': ""
                    # (list(value[key_of_dict].values())[1]) == 'value': ""
                    if status_value == 'was added' and list(value[key_of_dict].values())[2] == '':
                        print(tabulation, sigh(status_value), key_of_dict, ": ", end='')
                        print(list(value[key_of_dict].values())[1])
                    # check children: if childs exist.
                    # list(value[key_of_dict].values())[2] == 'childs': "{, }"
                    elif status_value == 'was added' and list(value[key_of_dict].values())[2] != '':
                        print(tabulation, sigh(status_value), key_of_dict, ": {")
                        acc += 1
                        walk(list(value[key_of_dict].values())[2], acc)
                    elif status_value == 'no changes' and list(value[key_of_dict].values())[2] == '':
                        print(tabulation, sigh(status_value), key_of_dict, ": ", end='')
                        print(list(value[key_of_dict].values())[1])
                    elif status_value == 'no changes' and list(value[key_of_dict].values())[2] != '':
                        print(tabulation, sigh(status_value), key_of_dict, ":")
                        acc += 1
                        walk(list(value[key_of_dict].values())[2], acc)
                    # list(value[key_of_dict].values())[3] == 'old_value': ''
                    elif status_value == 'was updated':
                        if list(value[key_of_dict].values())[2] == '[**]':
                            print(tabulation, '-', key_of_dict, ": {")
                            acc += 1
                            walk(list(value[key_of_dict].values())[3], acc)
                            print(tabulation, '+', key_of_dict, ":")
                            walk(list(value[key_of_dict].values())[1], acc)
                        elif list(value[key_of_dict].values())[2] == '[_*]':
                            print(tabulation, '-', key_of_dict, ":")
                            print(list(value[key_of_dict].values())[3])
                            print(tabulation, '+', key_of_dict, ":{")
                            acc += 1
                            walk(list(value[key_of_dict].values())[1], acc)
                        elif list(value[key_of_dict].values())[2] == '[*_]':
                            print(tabulation, '-', key_of_dict, ": {")
                            acc += 1
                            walk(list(value[key_of_dict].values())[3], acc)
                            print(tabulation, '+', key_of_dict, ": ", end='')
                            print(list(value[key_of_dict].values())[1])
                        elif list(value[key_of_dict].values())[2] == '[__]':
                            print(tabulation, '-', key_of_dict, ": ", end='')
                            print(list(value[key_of_dict].values())[3])
                            print(tabulation, '+', key_of_dict, ": ", end='')
                            print(list(value[key_of_dict].values())[1])
                    elif status_value == 'was updated' and list(value[key_of_dict].values())[2] != '':
                        print(tabulation, '-', key_of_dict, ":")
                        print(tabulation, '+', key_of_dict, ":")
                    elif status_value == 'was removed' and list(value[key_of_dict].values())[2] == '':
                        print(tabulation, sigh(status_value), key_of_dict, ": ", end='')
                        print(list(value[key_of_dict].values())[3])
                    elif status_value == 'was removed' and list(value[key_of_dict].values())[2] != '':
                        print(tabulation, sigh(status_value), key_of_dict, ": {")
                        acc += 1
                        walk(list(value[key_of_dict].values())[2], acc)
                if type(value[key_of_dict]) is not dict:
                    print(tabulation, key_of_dict, ':', value[key_of_dict])
            print(tabulation, '}')
    print("{")
    return walk(x, 0)
