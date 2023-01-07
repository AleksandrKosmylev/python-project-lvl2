from gendiff.constants import Removed, Added, Updated, Both_dict, No_changes, Keys_of_tree
# flake8: noqa: C901


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


def stringify(y, spaces='  '):
    def walk(package, acc, x):
        tab = spaces * acc
        if type(package) is dict:
            if Keys_of_tree == list(package.keys()):
                values_list = list(package.values())
                dict_type = values_list[0]
                dict_values = values_list[1]
                dict_children = values_list[2]
                dict_old = values_list[3]
                if dict_type == Both_dict:
                    if type(dict_children) is dict:
                        x.append("{")
                        walk(dict_children, acc + 1, x)
                        acc -= 1
                        x.extend(["\n", tab, "}"])
                    else:
                        walk(dict_children, acc + 1, x)
                        acc -= 1
                elif dict_type == Added:
                    if type(dict_values) is dict:
                        x.append("{")
                        walk(dict_values, acc + 1, x)
                        x.extend(["\n", tab, "}"])
                    elif type(dict_values) is not dict:
                        walk(dict_values, acc + 1, x)
                elif dict_type == No_changes:
                    if type(dict_old) is dict:
                        x.append("{")
                        walk(dict_old, acc + 1, x)
                        x.append("\n}")
                    elif type(dict_old) is not dict:
                        walk(dict_old, acc + 1, x)
                elif dict_type == Removed:
                    if type(values_list[3]) is dict:
                        x.append("{")
                        walk(dict_old, acc + 1, x)
                        x.extend(["\n", tab, "}"])
                    elif type(dict_old) is not dict:
                        walk(dict_old, acc + 1, x)
                elif dict_type == Updated:
                    if type(dict_old) is dict:
                        x.append("{")
                        walk(dict_old, acc + 1, x)
                        x.extend(["\n", tab, "}"])
                        walk(dict_values, acc - 1, x)
                    elif type(dict_old) is not dict:
                        walk(dict_old, acc - 1, x)
                        walk(dict_values, acc - 1, x)
            elif Keys_of_tree != list(package.keys()):
                for dict_key in package.keys():
                    if type(package[dict_key]) is not dict:
                        x.extend(["\n", tab, "  ",
                                  dict_key, ': ', package[dict_key]])
                    if type(package[dict_key]) is dict:
                        if len(package[dict_key]) == 1:
                            for_sign = list(package[dict_key].values())[0]
                            x.extend(["\n", tab, "",
                                      sign(for_sign), dict_key, ': {'])
                            walk(package[dict_key], acc + 2, x)
                            x.extend(["\n", tab, "  }"])
                        else:
                            for_sign = list(package[dict_key].values())[0]
                            x.extend(["\n", tab,
                                      sign(for_sign), dict_key, ': '])
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
        return s + "\n}"
    return walk(y, 1, ["{"])
