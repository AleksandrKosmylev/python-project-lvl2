import json
import yaml
import sys
import os


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
    for i in unioned_keys:
        if i in keys1 and i not in keys2:
            result[i] = {
                'status': 'was removed',
                'value': a[i],
                'childs': "",
                "old_value": a[i]}
            if type(a[i]) is dict:
                result[i] = {
                    'status': 'was removed',
                    'value': "", 'childs': a[i],
                    "old_value": a[i]
                }
            elif type(a[i]) is not dict:
                result[i] = {
                    'status': 'was removed',
                    'value': "", 'childs': "",
                    "old_value": a[i]
                }
        elif i in keys2 and i not in keys1:
            if type(b[i]) is dict:
                result[i] = {
                    'status': 'was added',
                    'value': b[i], 'childs': b[i],
                    "old_value": ""
                }
            else:
                result[i] = {
                    'status': 'was added',
                    'value': b[i], 'childs': "",
                    "old_value": ""
                }
        elif i in keys1 and i in keys2:
            if (type(a[i]) is dict) is True and (type(b[i]) is dict) is True:
                result[i] = (get_dicts_diff(a[i], b[i]))
            elif (type(a[i]) is dict) is False or (type(b[i]) is dict) is False:
                if a[i] != b[i]:
                    if (type(a[i]) is dict) and (type(b[i]) is dict):
                        result[i] = {'status': 'was updated',
                                     'value': b[i], 'childs': '[**]',
                                     "old_value": a[i]}
                    elif (type(a[i]) is not dict) and (type(b[i]) is dict):
                        result[i] = {'status': 'was updated',
                                     'value': b[i], 'childs': '[_*]',
                                     "old_value": a[i]
                                     }
                    elif (type(a[i]) is dict) and (type(b[i]) is not dict):
                        result[i] = {'status': 'was updated',
                                     'value': b[i], 'childs': '[*_]',
                                     "old_value": a[i]}
                    elif (type(a[i]) is not dict) and (type(b[i]) is not dict):
                        result[i] = {'status': 'was updated',
                                     'value': b[i], 'childs': '[__]',
                                     "old_value": a[i]}
                else:
                    result[i] = {
                        'status': 'no changes',
                        'value': b[i],
                        'childs': "",
                        "old_value": a[i]
                    }
    return result


def stringify(x, spaces='  '):
    def walk(value, acc):
        tab = spaces * acc
        keys_of_tree = ['status', 'value', 'childs', 'old_value']
        if type(value) is dict:
            for dict_key in value.keys():
                if type(value[dict_key]) is dict:
                    if keys_of_tree != list(value[dict_key].keys()):
                        acc += 1
                        tab = spaces * acc
                        print(f'{tab}{dict_key}:', "{")
                        walk(value[dict_key], acc + 1)
                        acc -= 1
                        tab = spaces * acc
                    elif keys_of_tree == list(value[dict_key].keys()):
                        values_list = list(value[dict_key].values())
                        values_list = values_list
                        status = values_list[0]
                        # branches that depend on status
                        # was added.
                        # check children: if no childs.
                        # list(value[dict_key].values())[2] == 'childs': ""
                        # (list(value[dict_key].values())[1]) == 'value': ""
                        if status == 'was added' and\
                                values_list[2] == '':
                            print(f'{tab}'
                                  f'{sigh(status)} {dict_key}: ',
                                  end='')
                            print(values_list[1])
                        # check children: if childs exist.
                        # list(value[dict_key].values())[2] ==
                        # 'childs': "{, }"
                        elif status == 'was added' and\
                                values_list[2] != '':
                            print(f'{tab}'
                                  f'{sigh(status)} {dict_key}:', "{")
                            acc += 1
                            walk(values_list[2], acc + 1)
                            tab = spaces * acc
                            acc -= 1
                        elif status == 'no changes' and\
                                values_list[2] == '':
                            print(f' {tab}'
                                  f'{sigh(status)}'
                                  f'{dict_key}: ', end='')
                            print(values_list[1])
                        elif status == 'no changes' and\
                                values_list[2] != '':
                            print(f'{tab}'
                                  f'{sigh(status)}'
                                  f'{dict_key}:')
                            walk(values_list[2], acc + 1)
                        elif status == 'was updated':
                            if values_list[2] == '[**]':
                                print(f'{tab}- {dict_key}: ', " {")
                                walk(values_list[3], acc + 1)
                                print(f'{tab}+ {dict_key}: ')
                                walk(values_list[1], acc + 1)
                            elif values_list[2] == '[_*]':
                                print(f'{tab}- {dict_key}: ', end='')
                                print(values_list[3])
                                print(f'{tab}+ {dict_key}:', "{")
                                acc += 1
                                walk(values_list[1], acc + 1)
                                acc -= 1
                                tab = spaces * acc
                            elif values_list[2] == '[*_]':
                                print(f'{tab}- {dict_key}:', "{")
                                acc += 1
                                walk(values_list[3], acc + 1)
                                acc -= 1
                                tab = spaces * acc
                                print(f'{tab}+ {dict_key}: ', end='')
                                print(values_list[1])
                            elif values_list[2] == '[__]':
                                print(f'{tab}- {dict_key}:', end='')
                                if values_list[3] == "":
                                    print(" ")
                                else:
                                    print("", values_list[3])
                                print(f'{tab}+ {dict_key}:', end='')
                                if values_list[1] == "":
                                    print(" ")
                                else:
                                    print("", values_list[1])
                        elif status == 'was updated' and\
                                values_list[2] != '':
                            print(f'{tab}- {dict_key} :')
                            print(f'{tab}+ {dict_key} :')
                        elif status == 'was removed' and\
                                values_list[2] == '':
                            print(f'{tab}{sigh(status)} {dict_key}: ', end='')
                            print(values_list[3])
                        elif status == 'was removed' and\
                                values_list[2] != '':
                            print(f'{tab}{sigh(status)} {dict_key}:', "{")
                            acc += 1
                            walk(values_list[2], acc + 1)
                            acc -= 1
                            tab = spaces * acc
                    else:
                        print('***')
                if type(value[dict_key]) is not dict:
                    acc += 1
                    tab = spaces * acc
                    print(f'{tab}{dict_key}:', value[dict_key])
                    acc -= 1
                    tab = spaces * acc
        acc -= 1
        tab = spaces * acc
        print(tab + '}')
    print("{")
    return walk(x, 1)


def get_plain_diff(x):
    def walk(value, acc):
        keys_of_tree = ['status', 'value', 'childs', 'old_value']
        for key_of_dict in value.keys():
            if type(value[key_of_dict]) is dict:
                if keys_of_tree != list(value[key_of_dict].keys()):
                    acc.append(str(key_of_dict) + '.')
                    walk(value[key_of_dict], acc)
                    acc = acc[:-1]
                if keys_of_tree == list(value[key_of_dict].keys()):
                    status_value = list(value[key_of_dict].values())[0]
                    # branches that depend on status
                    # was added.
                    # check children: if no childs.
                    # list(value[key_of_dict].values())[2] == 'childs': ""
                    # (list(value[key_of_dict].values())[1]) == 'value': ""
                    if status_value == 'was added':
                        # check children: if childs exist.
                        # list(value[key_of_dict].values())[2] ==
                        # 'childs': "{, }
                        if list(value[key_of_dict].values())[2] == '':
                            acc.append(str(key_of_dict))
                            print("Property", repr(''.join(acc)),
                                  status_value, "with value:",
                                  end=' ')
                            print(repr(list(value[key_of_dict].values())[1]))
                            acc = acc[:-1]
                        elif list(value[key_of_dict].values())[2] != '':
                            acc.append(str(key_of_dict))
                            print("Property", repr(''.join(acc)),
                                  status_value, "with value:", end=' ')
                            print('[complex value]')
                            acc = acc[:-1]
                    elif status_value == 'was updated':
                        if list(value[key_of_dict].values())[2] == '[**]':
                            walk(list(value[key_of_dict].values())[3], acc)
                            acc = acc[:-1]
                            walk(list(value[key_of_dict].values())[1], acc)
                            acc = acc[:-1]
                        elif list(value[key_of_dict].values())[2] == '[_*]':
                            acc.append(str(key_of_dict))
                            print("Property", repr(''.join(acc)),
                                  'was updated. From', end=' ')
                            print(repr(list(value[key_of_dict].values())[3]),
                                  'to', end=' ')
                            print('[complex value]')
                            acc = acc[:-1]
                        elif list(value[key_of_dict].values())[2] == '[*_]':
                            acc.append(str(key_of_dict))
                            print("Property", repr(''.join(acc)),
                                  'was updated. From', end=' ')
                            print('[complex value] to', end=' ')
                            print(repr(list(value[key_of_dict].values())[1]))
                            acc = acc[:-1]
                        elif list(value[key_of_dict].values())[2] == '[__]':
                            acc.append(str(key_of_dict))
                            print("Property", repr(''.join(acc)),
                                  'was updated. From', end=' ')
                            print(repr(list(value[key_of_dict].values())[3]),
                                  'to', end=' ')
                            print(repr(list(value[key_of_dict].values())[1]))
                            acc = acc[:-1]
                    elif status_value == 'was removed':
                        acc.append(str(key_of_dict))
                        print("Property", repr(''.join(acc)), status_value)
                        acc = acc[:-1]
                else:
                    acc = acc[:-1]
    return walk(x, [])


def convert_to_file(func, file_difference):
    original_stdout = sys.stdout
    output_file = open("output.json", 'w')
    sys.stdout = output_file
    func(file_difference)
    output_file.close()
    sys.stdout = original_stdout
    with open("output.json", 'r') as file:
        filedata = file.read()
    to_replace = {'False': 'false', "True": "true", "None": "null"}
    for i in to_replace.keys():
        filedata = filedata.replace(i, to_replace[i])
    with open("output.json", 'w') as file:
        file.write(filedata)
    if func == stringify:
        with open("output.json", 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            file.writelines(lines[:-1])
        with open("output.json", 'a') as file:
            file.write('}')
    elif func == get_plain_diff:
        with open("output.json", 'rb+') as filehandle:
            filehandle.seek(-1, os.SEEK_END)
            filehandle.truncate()


def print_file_content():
    f = open("output.json", 'r')
    data = f.read()
    f.close()
    print(data)
    return data


def generate_diff(path_1, path_2, formatter='stylish'):
    dict_1 = get_dict_from_file(path_1)
    dict_2 = get_dict_from_file(path_2)
    result = get_dicts_diff(dict_1, dict_2)
    if formatter == 'stylish':
        convert_to_file(stringify, result)
        return print_file_content()
    elif formatter == 'plain':
        convert_to_file(get_plain_diff, result)
        return print_file_content()
    elif formatter == 'json':
        jsonstr = json.dumps(result)
        with open("output.json", 'w') as file:
            file.write(jsonstr)
        return print_file_content()
