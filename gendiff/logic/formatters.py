from gendiff.logic.get_dicts_diff import sign
# flake8: noqa: C901

removed = 'was removed'
added = 'was added'
updated = 'was updated'
both_dict = 'both_dict'
no_changes = 'no changes'
status_list = [removed, added, updated, both_dict, no_changes ]
keys_of_tree = ['type', 'value', 'childs', 'old_value']


def stringify(y, spaces='  '):
    def walk(package, acc, x):
        tab = spaces * acc
        if type(package) is dict:
            if keys_of_tree == list(package.keys()):
                values_list = list(package.values())
                dict_type = values_list[0]
                dict_values = values_list[1]
                dict_children = values_list[2]
                dict_old = values_list[3]
                if dict_type == both_dict:
                    if type(dict_children) is dict:
                        x.append("{")
                        walk(dict_children, acc + 1, x)
                        acc -= 1
                        x.extend(["\n", tab, "}"])
                    else:
                        walk(dict_children, acc + 1, x)
                        acc -= 1
                elif dict_type == added:
                    if type(dict_values) is dict:
                        x.append("{")
                        walk(dict_values, acc + 1, x)
                        x.extend(["\n", tab, "}"])
                    elif type(dict_values) is not dict:
                        walk(dict_values, acc + 1, x)
                elif dict_type == no_changes:
                    if type(dict_old) is dict:
                        x.append("{")
                        walk(dict_old, acc + 1, x)
                        x.append("\n}")
                    elif type(dict_old) is not dict:
                        walk(dict_old, acc + 1, x)
                elif dict_type == removed:
                    if type(values_list[3]) is dict:
                        x.append("{")
                        walk(dict_old, acc + 1, x)
                        x.extend(["\n", tab, "}"])
                    elif type(dict_old) is not dict:
                        walk(dict_old, acc + 1, x) 
                elif dict_type == updated:
                    if type(dict_old) is dict:
                        x.append("{")
                        walk(dict_old, acc + 1 , x)
                        x.extend(["\n", tab, "}"])
                        walk(dict_values, acc -1 , x)
                    elif type(dict_old) is not dict:
                        walk(dict_old, acc - 1, x)
                        walk(dict_values, acc -1 , x)
            elif keys_of_tree != list(package.keys()):    
                for dict_key in package.keys():
                    if type(package[dict_key]) is not dict:
                        x.extend(["\n",tab, "  ", dict_key, ': ', package[dict_key]])
                    if type(package[dict_key]) is dict:
                        if len(package[dict_key]) == 1 :
                            for_sign = list(package[dict_key].values())[0] 
                            x.extend(["\n",tab,"", sign(for_sign), dict_key, ': {'])
                            walk(package[dict_key], acc + 2, x)
                            x.extend(["\n", tab, "  }"])
                        else:
                            for_sign = list(package[dict_key].values())[0] 
                            x.extend(["\n",tab, sign(for_sign), dict_key, ': '])
                            walk(package[dict_key], acc + 1, x)             
        else:
            acc -= 1
            x.extend([package])
        for index, piece in enumerate(x):
            check_dict = {"True": "true", "False": "false", "None": "null"}
            if str(piece) in list(check_dict.keys()):
                x[index] = check_dict[str(piece)]
        z = [str(i) for i in x]
        s = "".join(z)
        return s + "\n}\n"
    return walk(y, 1, ["{"])


def get_plain_diff(x):
    def walk(value, acc, list_acc):
        for key_of_dict in value.keys():
            status_value = list(value[key_of_dict].values())[0]
            list_childs = list(value[key_of_dict].values())[2]
            list_values = list(value[key_of_dict].values())[1]
            list_old_values = list(value[key_of_dict].values())[3]
            if status_value == both_dict:
                acc.append(str(key_of_dict) + "." )
                walk(list_childs, acc, list_acc)
                acc = acc[:-2]
            if status_value == "was added":
                acc.append(str(key_of_dict))
                list_acc.extend(["Property ", repr(''.join(acc)), " ",
                status_value, " with value: "])
                if type(list_values) is not dict:
                    list_acc.extend([repr(list_values), '\n'])
                else:
                    list_acc.extend(["[complex value]", "\n"])
                acc = acc[:-1]
            elif status_value == "was updated":
                acc.append(str(key_of_dict))
                list_acc.extend(["Property ", repr(''.join(acc))," was updated. From "])
                bank = []
                for i in [list_old_values, list(list_values.values())[0]["value"]]:
                    if type(i) is dict:
                        bank.append("[complex value]")
                    if type(i) is not dict:
                        bank.append(repr(i))
                list_acc.extend([bank[0],
                " to ", bank[1],'\n'])
                acc = acc[:-1]
            elif status_value == "was removed":
                acc.append(str(key_of_dict))
                list_acc.extend([
                    "Property ", repr(''.join(acc)), " ",
                    status_value, "\n"])
                acc = acc[:-1]
        for index, piece in enumerate(list_acc):
            check_dict = {'True': "true", 'False': "false", 'None': "null"}
            if piece in list(check_dict.keys()):
                list_acc[index] = check_dict[piece]
        return "".join(list_acc)[:-1]
    return walk(x, [], [])
