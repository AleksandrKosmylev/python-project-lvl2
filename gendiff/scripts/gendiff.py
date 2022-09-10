#!/usr/bin/env python
import argparse
import json

from gendiff.scripts.get_diffs import get_dict_from_file,\
    get_dicts_difference, stringify,\
    get_plain_diff, convert_to_file, print_file_content


def generate_diff(path_1, path_2):
    dict_1 = get_dict_from_file(path_1)
    dict_2 = get_dict_from_file(path_2)
    result = get_dicts_difference(dict_1, dict_2)
    return result


def print_result():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument("-f", '--format',
                        help=' output format (default: stylish)')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    a = args.first_file
    b = args.second_file
    data = generate_diff(a, b)
    json_object = json.dumps(data)
    if args.format == 'plain':
        convert_to_file(get_plain_diff, data)
        print_file_content()
    elif args.format == 'stylish':
        convert_to_file(stringify, data)
        print_file_content()
    elif args.format == 'json':
        json_object
    else:
        convert_to_file(get_plain_diff, data)
        print_file_content()

def main():
    print_result()


if __name__ == '__main__':
    main()
