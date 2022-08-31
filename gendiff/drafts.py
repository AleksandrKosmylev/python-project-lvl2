import json
import yaml
from gendiff.scripts.gendiff import generate_diff
import json
import copy
import os

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

print(g)
#print()
#print(p)
result = first.copy()

#print(type(g))

"""
def abc(dictionary, acc, cycle = 0):
    keys = list(dictionary.keys())
    for i in keys:
        acc.append(i)
        if type(dictionary[i]) is dict:
            print( acc, '- acc before def\n')
            cycle +=1
            print(cycle, ' -cycle def')
            abc(dictionary[i], acc, cycle)
            l = len(str(dictionary[i]))
            print('- acc after def - ', acc)
            if cycle == 0:
                acc = acc[1:]
                print("*")
            else:
                print("**")
                l = len(str(i))
                acc = acc[cycle+1:]
                pass
            print('- acc after def(!!!1) - ', acc)
        else:
           # cycle -= 1
            print(cycle, ' -cycle')
            print('-')
            acc.append(dictionary[i])
            l = len(str(dictionary[i]) + str(i))
            print(acc, '- acc without def(1)\n')
            acc = acc[1:]
    #        print(' -acc without def(2) - ', acc)
abc(g, [])
"""
"""
def xyz(res_acc):
    def abc(dictionary, acc, cycle,res):
        keys = list(dictionary.keys())
        for i in keys:
            acc += i
            if type(dictionary[i]) is dict:
      #          print('+')
                print( acc,'\n')
                res += acc
        #        print( res, '- res before def\n')
                cycle +=1
             #   print(cycle, ' -cycle def')
                abc(dictionary[i], acc, cycle, res)
                l = len(str(dictionary[i]))
      #          print('- acc after def - ', acc)
                if cycle == 0:
                    acc = acc[:-l]
                    res += acc
     #               print("*")
                else:
    #                print("**")
                    l = len(str(i))
                    acc = acc[:-l]
                    res += acc
                    pass
      #          print('- acc after def(!!!1) - ', acc)
            else:
                cycle -= 1
         #       print(cycle, ' -cycle')
     #           print('-')
                acc += (': ' + str(dictionary[i]))
                l = len(str(dictionary[i]) + str(i))
         #       print(cycle, ' -cycle after def')
                print(acc, '\n')
                res += acc
         #       print(res, '- res without def(1)\n')
                acc = acc[:-(l + 2)]
        #        print(' -acc without def(2) - ', acc)
    #    print('==',res)
        return acc
 #   abc(g, ' ', 0, res_acc)
    print('----', abc(g, ' ', 0, res_acc))
xyz('')
"""

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

first_form = stringify(g)
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

first_form = stringify(g)


"""
# almost working version ####################

def diff_comment(a, b):
    def walk(dict_1, dict_2, result):
        keys1 = set(dict_1.keys())
        keys2 = set(dict_2.keys())
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
comm = diff_comment(first, second)

"""
"""
def stringify(x, spaces=' ', count=1):
    def walk(value, acc):
        tabulation = spaces * count * acc
        keys_of_tree = ['status', 'value', 'childs', 'old_value']
        if type(value) is dict:
            for key_of_dict in value.keys():
                if type(value[key_of_dict]) is dict and keys_of_tree != list(value[key_of_dict].keys()):
                    print(tabulation, key_of_dict, ": {")
                    acc.append(str(key_of_dict))
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
                        acc.append(str(key_of_dict))
                        walk(list(value[key_of_dict].values())[2], acc)
                    elif status_value == 'no changes' and list(value[key_of_dict].values())[2] == '':
                        print(tabulation, sigh(status_value), key_of_dict, ": ", end='')
                        print(list(value[key_of_dict].values())[1])
                    elif status_value == 'no changes' and list(value[key_of_dict].values())[2] != '':
                        print(tabulation, sigh(status_value), key_of_dict, ":")
                        acc.append(str(key_of_dict))
                        walk(list(value[key_of_dict].values())[2], acc)
                    # list(value[key_of_dict].values())[3] == 'old_value': ''
                    elif status_value == 'was updated':
                        if list(value[key_of_dict].values())[2] == '[**]':
                            print(tabulation, '-', key_of_dict, ": {")
                            acc.append(str(key_of_dict))
                            walk(list(value[key_of_dict].values())[3], acc)
                            print(tabulation, '+', key_of_dict, ":")
                            walk(list(value[key_of_dict].values())[1], acc)
                        elif list(value[key_of_dict].values())[2] == '[_*]':
                            print(tabulation, '-', key_of_dict, ":")
                            print(list(value[key_of_dict].values())[3])
                            print(tabulation, '+', key_of_dict, ":{")
                            acc.append(str(key_of_dict))
                            walk(list(value[key_of_dict].values())[1], acc)
                        elif list(value[key_of_dict].values())[2] == '[*_]':
                            print(tabulation, '-', key_of_dict, ": {")
                            acc.append(str(key_of_dict))
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
                        acc.append(str(key_of_dict))
                        walk(list(value[key_of_dict].values())[2], acc)
                if type(value[key_of_dict]) is not dict:
                    print(tabulation, key_of_dict, ':', value[key_of_dict])
            print(tabulation, '}')
    print("{")
    return walk(x, " ")

"""

def get_plain_diff(x):
    def walk(value, acc):
        keys_of_tree = ['status', 'value', 'childs', 'old_value']
        if type(value) is dict:
            for key_of_dict in value.keys():
                if type(value[key_of_dict]) is dict and keys_of_tree != list(value[key_of_dict].keys()):
                    acc.append(str(key_of_dict) + '.')
                    print(acc, '-1')
                    walk(value[key_of_dict], acc)
                    print(acc, '0')
                    acc = acc[:-1]
                    print(acc,'1')
#                    acc = acc[:-len(acc)]
                elif type(value[key_of_dict]) is dict and keys_of_tree == list(value[key_of_dict].keys()):
                    status_value = list(value[key_of_dict].values())[0]
                    # branches that depend on status
                    # was added.
                    # check children: if no childs.
                    # list(value[key_of_dict].values())[2] == 'childs': ""
                    # (list(value[key_of_dict].values())[1]) == 'value': ""
                    if status_value == 'was added' and list(value[key_of_dict].values())[2] == '':
                        acc.append(str(key_of_dict))
                        print(repr(''.join(acc)), status_value, "with value", end=' ')
                        print(repr(list(value[key_of_dict].values())[1]))
                        print(acc, '-2')
                        acc = acc[:-1]
                        print(acc,'2')
                    # check children: if childs exist.
                    # list(value[key_of_dict].values())[2] == 'childs': "{, }"
                    elif status_value == 'was added' and list(value[key_of_dict].values())[2] != '':
                        acc.append(str(key_of_dict))
                        print(repr(''.join(acc)), "was added with value : [complex value]")
                        acc = acc[:-1]
                        print(acc, '3')
                    elif status_value == 'was updated':
                        if list(value[key_of_dict].values())[2] == '[**]':
                            walk(list(value[key_of_dict].values())[3], acc)
                            walk(list(value[key_of_dict].values())[1], acc)
                        elif list(value[key_of_dict].values())[2] == '[_*]':
                            acc.append(str(key_of_dict) + '.')
                            print(repr(''.join(acc)), status_value, 'from', end=' ' )
                            print(repr(list(value[key_of_dict].values())[1]), 'to', end=' ')
                            print('[complex value]')
                            acc = acc[:-1]
                            print(acc, '4')
                        elif list(value[key_of_dict].values())[2] == '[*_]':
                            acc.append(str(key_of_dict))
                            print(repr(''.join(acc)), repr(status_value), 'from', end=' ' )
                            print('[complex value] to', end=' ')
                            print(repr(list(value[key_of_dict].values())[1]))
                            acc = acc[:-1]
                            print(acc, '5')
                        elif list(value[key_of_dict].values())[2] == '[__]':
                            acc.append(str(key_of_dict))
                            print(repr(''.join(acc)), status_value, 'from', end=' ' )
                            print(repr(list(value[key_of_dict].values())[3]), 'to', end=' ')
                            print(repr(list(value[key_of_dict].values())[1]))
                            acc = acc[:-1]
                            print(acc, '6')
                    elif status_value == 'was removed':
                        acc.append(str(key_of_dict))
                        print(repr(''.join(acc)), status_value)
                        print(acc, '-7')
                        acc = acc[:-1]
                        print(acc, '7')
                if type(value[key_of_dict]) is not dict:
                    print('something else')
                    print(':', value[key_of_dict])
                    acc = acc[:-1]
                    print(acc, '8')


        else:
            print('else')
    return walk(x, [])

plain = get_plain_diff(x)
