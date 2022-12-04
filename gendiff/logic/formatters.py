from gendiff.logic.get_dicts_diff import sign
# flake8: noqa: C901


def stringify(y, spaces='  '):
    def walk(value, acc, x):
        tab = spaces * acc
        keys_of_tree = ['type', 'value', 'childs', 'old_value']
        if type(value) is dict:
            for dict_key in value.keys():
                if type(value[dict_key]) is dict:
                    if keys_of_tree != list(value[dict_key].keys()):
                        acc += 1
                        tab = spaces * acc
                        x.extend([tab, dict_key, ": {\n"])
                        walk(value[dict_key], acc + 1, x)
                        acc -= 1
                        tab = spaces * acc
                    elif keys_of_tree == list(value[dict_key].keys()):
                        values_list = list(value[dict_key].values())
                        values_list = values_list
                        dict_type = values_list[0]
                        # branches that depend on type
                        # was added.
                        # check children: if no childs.
                        # list(value[dict_key].values())[2] == 'childs': ""
                        # (list(value[dict_key].values())[1]) == 'value': ""
                        # symbols for childs, if they are dicts:
                        # '[**]' - both are dicts, '[_*]' - 2nd is a dict,
                        # '[*_]' - 1st is a dict, '[__]' - no dicts
                        added = 'was added'
                        no_changes = 'no changes'
                        removed = 'was removed'
                        dict_children = values_list[2]
                        list_1 = [tab, sign(dict_type), dict_key, ": "]
                        if dict_children == '':
                            if dict_type == added:
                                x.extend(list_1)
                                x.extend([values_list[1], "\n"])
                            elif dict_type == no_changes:
                                x.extend(list_1)
                                x.extend([values_list[1], "\n"])
                            elif dict_type == removed:
                                x.extend(list_1)
                                x.extend([values_list[3], '\n'])
                        if dict_children != '':
                            if dict_type != 'was updated':
                                x.extend(list_1)
                                x.append("{\n")
                                acc += 1
                                walk(dict_children, acc + 1, x)
                                acc -= 1
                                tab = spaces * acc
                            elif dict_type == 'was updated':
                                if dict_children == '[**]':
                                    x.extend([tab, "- ", dict_key, ": {\n"])
                                    walk(values_list[3], acc + 1, x)
                                    x.extend([tab, "+ ", dict_key, ": "])
                                    walk(values_list[1], acc + 1, x)
                                elif dict_children == '[_*]':
                                    x.extend([tab, "- ", dict_key, ": "])
                                    x.extend([values_list[3], "\n"])
                                    x.extend([tab, "+ ", dict_key, ": {\n"])
                                    acc += 1
                                    walk(values_list[1], acc + 1, x)
                                    acc -= 1
                                    tab = spaces * acc
                                elif dict_children == '[*_]':
                                    x.extend([tab, "- ", dict_key, ": {\n"])
                                    acc += 1
                                    walk(values_list[3], acc + 1, x)
                                    acc -= 1
                                    tab = spaces * acc
                                    x.extend([tab, '+ ', dict_key,
                                              ': ', values_list[1], "\n"])
                                elif dict_children == '[__]':
                                    x.extend([tab, "- ", dict_key, ": ",
                                              values_list[3], "\n"])
                                    x.extend([tab, "+ ", dict_key, ": ",
                                              values_list[1], "\n"])
                if type(value[dict_key]) is not dict:
                    acc += 1
                    tab = spaces * acc
                    x.extend([tab, dict_key, ": ", value[dict_key], "\n"])
                    acc -= 1
                    tab = spaces * acc
        acc -= 1
        tab = spaces * acc
        x.extend([tab, '}\n'])
        for index, piece in enumerate(x):
            check_dict = {"True": "true", "False": "false", "None": "null"}
            if str(piece) in list(check_dict.keys()):
                x[index] = check_dict[str(piece)]
        z = [str(i) for i in x]
        s = "".join(z)
        return s[:-1]
    return walk(y, 1, ["{\n"])


def get_plain_diff(x):
    def walk(value, acc, list_acc):
        keys_of_tree = ['type', 'value', 'childs', 'old_value']
        for key_of_dict in value.keys():
            if type(value[key_of_dict]) is dict:
                if keys_of_tree != list(value[key_of_dict].keys()):
                    acc.append(str(key_of_dict) + ".")
                    walk(value[key_of_dict], acc, list_acc)
                    acc = acc[:-1]
                if keys_of_tree == list(value[key_of_dict].keys()):
                    status_value = list(value[key_of_dict].values())[0]
                    # branches that depend on status
                    # was added.
                    # check children: if no childs.
                    # list(value[key_of_dict].values())[2] == 'childs': ""
                    # (list(value[key_of_dict].values())[1]) == 'value': ""
                    list_childs = list(value[key_of_dict].values())[2]
                    list_values = list(value[key_of_dict].values())[1]
                    if status_value == "was added":
                        # check children: if childs exist.
                        # list(value[key_of_dict].values())[2] ==
                        # 'childs': "{, }
                        acc.append(str(key_of_dict))
                        list_acc.extend([
                            "Property ", repr(''.join(acc)), " ",
                            status_value, " with value: "])
                        if list_childs == '':
                            list_acc.extend([
                                repr(list_values), '\n'
                            ])
                            acc = acc[:-1]
                        elif list_childs != '':
                            list_acc.extend([
                                "[complex value]", "\n"
                            ])
                            acc = acc[:-1]
                    elif status_value == "was updated":
                        list_old_values = list(value[key_of_dict].values())[3]
                        if list_childs == '[**]':
                            walk(list_old_values, acc, list_acc)
                            acc = acc[:-1]
                            walk(list_values, acc, list_acc)
                            acc = acc[:-1]
                        elif list_childs == '[_*]':
                            acc.append(str(key_of_dict))
                            list_acc.extend([
                                "Property ", repr(''.join(acc)),
                                " was updated. From ",
                                repr(list_old_values),
                                ' to [complex value]', "\n"
                            ])
                            acc = acc[:-1]
                        elif list_childs == '[*_]':
                            acc.append(str(key_of_dict))
                            list_acc.extend([
                                "Property ", repr(''.join(acc)),
                                " was updated. From ",
                                "[complex value] to ",
                                repr(list_values),
                                "\n"
                            ])
                            acc = acc[:-1]
                        elif list_childs == '[__]':
                            acc.append(str(key_of_dict))
                            list_acc.extend([
                                "Property ", repr(''.join(acc)),
                                " was updated. From ",
                                repr(list_old_values),
                                " to ", repr(list_values), "\n"
                            ])
                            acc = acc[:-1]
                    elif status_value == "was removed":
                        acc.append(str(key_of_dict))
                        list_acc.extend([
                            "Property ", repr(''.join(acc)), " ",
                            status_value, "\n"
                        ])
                        acc = acc[:-1]
                else:
                    acc = acc[:-1]
        for index, piece in enumerate(list_acc):
            check_dict = {'True': "true", 'False': "false", 'None': "null"}
            if piece in list(check_dict.keys()):
                list_acc[index] = check_dict[piece]
        return "".join(list_acc)[:-1]
    return walk(x, [], [])
