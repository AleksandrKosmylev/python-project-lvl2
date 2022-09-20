#!/usr/bin/env python
import argparse
import json
import os


from gendiff.scripts.get_diffs import get_dict_from_file,\
    get_dicts_difference, stringify,\
    get_plain_diff, convert_to_file, print_file_content
#from gendiff.scripts.get_diffs import *


def generate_diff(path_1, path_2):
    dict_1 = get_dict_from_file(path_1)
    dict_2 = get_dict_from_file(path_2)
    result = get_dicts_difference(dict_1, dict_2)
    return result


def print_result():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument("-f", '--format',
                        help='set format of output')
    parser.add_argument('filepath1', type=str)
    parser.add_argument('filepath2', type=str)
    args = parser.parse_args()
    a = args.filepath1
    b = args.filepath2
    data = generate_diff(a, b)
    if args.format == 'plain':
        convert_to_file(get_plain_diff, data)
        print_file_content()
        os.remove("gendiff/output.json")
    elif args.format == 'stylish':
        convert_to_file(stringify, data)
        print_file_content()
        os.remove("gendiff/output.json")
    elif args.format == 'json':
        jsonStr = json.dumps(data)
        print(jsonStr)
    else:
        convert_to_file(stringify, data)
        print_file_content()
        os.remove("gendiff/output.json")


def main():
    print_result()


if __name__ == '__main__':
    main()