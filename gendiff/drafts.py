import json
import yaml
from gendiff.scripts.gendiff import generate_diff
import json
import copy

path_1_j = r'/home/aleksandr/hexlet/projects/python-project-lvl2/gendiff/scripts/fixtures/file1_1.json'
path_2_j = r'/home/aleksandr/hexlet/projects/python-project-lvl2/gendiff/scripts/fixtures/file2_1.json'

path_1_y = r'/home/aleksandr/hexlet/projects/python-project-lvl2/gendiff/scripts/fixtures/file1.yaml'
path_2_y = r'/home/aleksandr/hexlet/projects/python-project-lvl2/gendiff/scripts/fixtures/file2.yaml'



x = generate_diff(path_1_j, path_2_j)
y = generate_diff(path_1_y, path_2_y)
z = generate_diff(path_1_j, path_2_y)


def get_dict_from_file(path_to_file):
    if path_to_file.endswith(".json") is True:
        f = json.load(open(path_to_file))
    elif path_to_file.endswith(".yaml") is True:
        f = yaml.load(open(path_to_file), Loader=yaml.FullLoader)
    return dict(f.items())

first = get_dict_from_file(path_1_y)
second = get_dict_from_file(path_2_y)


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
            if (type(dict_1[i]) is dict) is True and (type(dict_2[i]) is dict) is True:
                result[i] = (get_dicts_difference(a[i], b[i]))
            elif (type(dict_1[i]) is dict) is False or (type(dict_2[i]) is dict) is False:
                if a[i] != b[i]:
                    result["-" + i] = a[i]
                    result["+" + i] = b[i]
                else:
                    result[" " + i] = a[i]
    return result
 #   return "{\n" + str(yaml.dump(result, sort_keys=False)) + "}"
#    return  str(yaml.dump(result, sort_keys=False))
 #   return "{\n" + str(yaml.dump(result, sort_keys=False)) + "}"
path_to_file_1_json = "/home/aleksandr/hexlet/projects/python-project-lvl2/tests/fixtures/file1.json"
path_to_file_2_json = "/home/aleksandr/hexlet/projects/python-project-lvl2/tests/fixtures/file2.json"
first = get_dict_from_file(path_1_j)
second = get_dict_from_file(path_2_j)

g = get_dicts_difference(first, second)
p = "{\n" + str(yaml.dump(get_dicts_difference(first, second), sort_keys=False)) + "}"
x = yaml.dump(g, sort_keys=False)
#print(g)
#print()
#print(p)
result = first.copy()


def stringify(x, spaces=' ', count = 1):
    def walk(value, acc):
        if (type(value) is dict) is True:
            for i in value.keys():
                print(spaces, end="")
                if (type(value[i]) is dict) is True:
                    print(spaces * count * acc, i, ':', '{', '\n', end='')
                    acc += 1
                    walk(value[i], acc)
                    print(spaces*acc *count, '}')
                elif (type(value[i]) is dict) is False:
                    print(spaces * count * acc, i, ':', value[i])
        elif (type(value) is dict) is False:
            print(repr(value).replace('\'', ''))
    if (type(x) is dict) is True:
        print('{')
        return walk(x,0), print('}')
    else:
        return walk(x, 0)

#stringify(g)


# almost working version ####################

def diff_comment(a, b):
    def walk(dict_1, dict_2, result):
#        result = "Property "
        keys1 = set(dict_1.keys())
        keys2 = set(dict_2.keys())
    #    print('k1=', keys1, 'k2=', keys2)
        unioned_keys = sorted(keys1 | keys2, reverse=False)
        for i in unioned_keys:
            result += str(i) + ' '
            if i in keys1 and i not in keys2:
                result += "was removed"
                print("Property " + result)
                result = '(1) '
            elif i in keys2 and i not in keys1:
                if type(dict_2[i]) is dict:
                    result += "was updated with: [complex value]"
                    print("Property " + result)
                    result = '(2) '
                elif type(dict_2[i]) is not dict:
                    result += "was added with value: " + str(dict_2[i])
                    print("Property " + result)
                    result ='(3) '
            elif i in keys1 and i in keys2:
                if type(dict_2[i]) is not dict and type(dict_1[i]) is not dict:
                    if dict_1[i] == dict_2[i]:
                        result = '(4) '
                    elif dict_1 != dict_2:
                        result += 'was updated. From ' + str(dict_1[i]) + ' to ' + str(dict_2[i])
                        print("Property "+ result)
                        result = '(5) '
                elif type(dict_2[i]) is dict and type(dict_1[i]) is dict:
                    result += '(6) '
                    walk(dict_1[i], dict_2[i], result)
                else:
                    result += 'was updated. From ' + "[complex value]" + ' to ' + str(dict_2[i])
                    print("Property " + result)
    walk(a, b, "")
  #  return str(yaml.dump(result, sort_keys=False))
comm = diff_comment(first, second)
print(comm)
