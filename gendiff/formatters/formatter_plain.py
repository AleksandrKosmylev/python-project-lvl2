from gendiff.utils.constants import Removed, Added, Updated, Both_dict
from gendiff.utils.converter import convert
# flake8: noqa: C901

def get_plain_diff(raw_dict):
    def walk(value, acc, list_acc):
        for key_of_dict in value.keys():
            status_value, list_values, list_childs, list_old_values = list(value[key_of_dict].values())
            if status_value == Both_dict:
                acc.append(str(key_of_dict) + ".")
                walk(list_childs, acc, list_acc)
                acc = acc[:-2]
            if status_value == Added:
                acc.append(str(key_of_dict))
                list_acc.extend(["Property ", repr(''.join(acc)),
                                 " ", status_value, " with value: "])
                if not isinstance(list_values, dict):
                    list_acc.extend([repr(list_values), '\n'])
                else:
                    list_acc.extend(["[complex value]", "\n"])
                acc = acc[:-1]
            elif status_value == Updated:
                acc.append(str(key_of_dict))
                list_acc.extend(["Property ", repr(''.join(acc)),
                                 " was updated. From "])
                bank = []
                for i in [list_old_values,
                          list(list_values.values())[0]["value"]]:
                    if isinstance(i, dict):
                        bank.append("[complex value]")
                    else:
                        bank.append(repr(i))
                list_acc.extend([bank[0], " to ",
                                 bank[1], '\n'])
                acc = acc[:-1]
            elif status_value == Removed:
                acc.append(str(key_of_dict))
                list_acc.extend([
                    "Property ", repr(''.join(acc)), " ",
                    status_value, "\n"])
                acc = acc[:-1]
        convert(list_acc)
        return "".join(list_acc)[:-1]
    return walk(raw_dict, [], [])
