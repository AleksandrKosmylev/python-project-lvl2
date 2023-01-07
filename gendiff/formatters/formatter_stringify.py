from gendiff.utils.constants import Removed, Added, Updated, Both_dict, No_changes, Keys_of_tree
from gendiff.utils.converter import convert
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


def stringify(raw_dict, spaces='  '):
    def walk(package, acc, acc_dict):
        tab = spaces * acc
        if type(package) is dict:
            if Keys_of_tree == list(package.keys()):
                values_list = list(package.values())
                dict_type, dict_values, dict_children, dict_old = values_list
                if dict_type == Both_dict:
                    if type(dict_children) is dict:
                        acc_dict.append("{")
                        walk(dict_children, acc + 1, acc_dict)
                        acc -= 1
                        acc_dict.extend(["\n", tab, "}"])
                    else:
                        walk(dict_children, acc + 1, acc_dict)
                        acc -= 1
                elif dict_type == Added:
                    if type(dict_values) is dict:
                        acc_dict.append("{")
                        walk(dict_values, acc + 1, acc_dict)
                        acc_dict.extend(["\n", tab, "}"])
                    elif type(dict_values) is not dict:
                        walk(dict_values, acc + 1, acc_dict)
                elif dict_type == No_changes:
                    if type(dict_old) is dict:
                        acc_dict.append("{")
                        walk(dict_old, acc + 1, acc_dict)
                        acc_dict.append("\n}")
                    elif type(dict_old) is not dict:
                        walk(dict_old, acc + 1, acc_dict)
                elif dict_type == Removed:
                    if type(values_list[3]) is dict:
                        acc_dict.append("{")
                        walk(dict_old, acc + 1, acc_dict)
                        acc_dict.extend(["\n", tab, "}"])
                    elif type(dict_old) is not dict:
                        walk(dict_old, acc + 1, acc_dict)
                elif dict_type == Updated:
                    if type(dict_old) is dict:
                        acc_dict.append("{")
                        walk(dict_old, acc + 1, acc_dict)
                        acc_dict.extend(["\n", tab, "}"])
                        walk(dict_values, acc - 1, acc_dict)
                    elif type(dict_old) is not dict:
                        walk(dict_old, acc - 1, acc_dict)
                        walk(dict_values, acc - 1, acc_dict)
            elif Keys_of_tree != list(package.keys()):
                for dict_key in package.keys():
                    if type(package[dict_key]) is not dict:
                        acc_dict.extend(["\n", tab, "  ",
                                         dict_key, ': ', package[dict_key]])
                    if type(package[dict_key]) is dict:
                        if len(package[dict_key]) == 1:
                            for_sign = list(package[dict_key].values())[0]
                            acc_dict.extend(["\n", tab, "",
                                             sign(for_sign), dict_key, ': {'])
                            walk(package[dict_key], acc + 2, acc_dict)
                            acc_dict.extend(["\n", tab, "  }"])
                        else:
                            for_sign = list(package[dict_key].values())[0]
                            acc_dict.extend(["\n", tab,
                                             sign(for_sign), dict_key, ': '])
                            walk(package[dict_key], acc + 1, acc_dict)
        else:
            acc -= 1
            acc_dict.extend([package])
        convert(acc_dict)
        z = [str(i) for i in acc_dict]
        s = "".join(z)
        return s + "\n}"
    return walk(raw_dict, 1, ["{"])
