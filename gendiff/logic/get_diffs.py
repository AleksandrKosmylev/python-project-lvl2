import json
import yaml
import sys
import os
from gendiff.logic.get_dicts_diff import get_dicts_diff, get_dict_from_file, sigh
from gendiff.logic.formatters import stringify, get_plain_diff

# flake8: noqa: C901


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
