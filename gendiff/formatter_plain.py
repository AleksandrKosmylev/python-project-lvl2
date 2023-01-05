from formatter_stringify import Removed, Added, Updated, Both_dict
# flake8: noqa: C901

def get_plain_diff(x):
    def walk(value, acc, list_acc):
        for key_of_dict in value.keys():
            status_value = list(value[key_of_dict].values())[0]
            list_childs = list(value[key_of_dict].values())[2]
            list_values = list(value[key_of_dict].values())[1]
            list_old_values = list(value[key_of_dict].values())[3]
            if status_value == Both_dict:
                acc.append(str(key_of_dict) + ".")
                walk(list_childs, acc, list_acc)
                acc = acc[:-2]
            if status_value == Added:
                acc.append(str(key_of_dict))
                list_acc.extend(["Property ", repr(''.join(acc)),
                                 " ", status_value, " with value: "])
                if type(list_values) is not dict:
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
                    if type(i) is dict:
                        bank.append("[complex value]")
                    if type(i) is not dict:
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
        for index, piece in enumerate(list_acc):
            check_dict = {'True': "true", 'False': "false", 'None': "null"}
            if piece in list(check_dict.keys()):
                list_acc[index] = check_dict[piece]
        return "".join(list_acc)[:-1]
    return walk(x, [], [])
