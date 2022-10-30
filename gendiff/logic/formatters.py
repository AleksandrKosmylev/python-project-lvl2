from gendiff.logic.get_dicts_diff import sigh


# flake8: noqa: C901


def stringify(x, spaces='  '):
    def walk(value, acc):
        tab = spaces * acc
        keys_of_tree = ['type', 'value', 'childs', 'old_value']
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
                        constant_type = values_list[0]
                        # branches that depend on type
                        # was added.
                        # check children: if no childs.
                        # list(value[dict_key].values())[2] == 'childs': ""
                        # (list(value[dict_key].values())[1]) == 'value': ""
                        # symbols for childs, if they are dicts:
                        # '[**]' - both are dicts, '[_*]' - 2nd is a dict, '[*_]' - 1st is a dict, '[__]' - no dicts
                        added = 'was added'
                        if constant_type == added and\
                                values_list[2] == '':
                            print(f'{tab}'
                                  f'{sigh(constant_type)} {dict_key}: ',
                                  end='')
                            print(values_list[1])
                        # check children: if childs exist.
                        # list(value[dict_key].values())[2] ==
                        # 'childs': "{, }"
                        elif constant_type == added and\
                                values_list[2] != '':
                            print(f'{tab}'
                                  f'{sigh(constant_type)} {dict_key}:', "{")
                            acc += 1
                            walk(values_list[2], acc + 1)
                            tab = spaces * acc
                            acc -= 1
                        elif constant_type == 'no changes' and\
                                values_list[2] == '':
                            print(f' {tab}'
                                  f'{sigh(constant_type)}'
                                  f'{dict_key}: ', end='')
                            print(values_list[1])
                        elif constant_type == 'no changes' and\
                                values_list[2] != '':
                            print(f'{tab}'
                                  f'{sigh(constant_type)}'
                                  f'{dict_key}:')
                            walk(values_list[2], acc + 1)
                        elif constant_type == 'was updated':
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
                        elif constant_type == 'was updated' and\
                                values_list[2] != '':
                            print(f'{tab}- {dict_key} :')
                            print(f'{tab}+ {dict_key} :')
                        elif constant_type == 'was removed' and\
                                values_list[2] == '':
                            print(f'{tab}{sigh(constant_type)} {dict_key}: ', end='')
                            print(values_list[3])
                        elif constant_type == 'was removed' and\
                                values_list[2] != '':
                            print(f'{tab}{sigh(constant_type)} {dict_key}:', "{")
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
        keys_of_tree = ['type', 'value', 'childs', 'old_value']
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
