#!/usr/bin/env python
import argparse
# import yaml
from gendiff.scripts.get_diffs import get_dict_from_file,\
    get_dicts_difference,\
    stringify,\
    get_plain_diff


def generate_diff(path_1, path_2):
    dict_1 = get_dict_from_file(path_1)
    dict_2 = get_dict_from_file(path_2)
    result = get_dicts_difference(dict_1, dict_2)
#   return "{\n" + str(yaml.dump(result, sort_keys=False)) + "}"
    return result


def print_result():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    parser.add_argument("-f", '--format [type]', default='stylish',
                        action="store_true",
                        help=' output format (default: stylish)')

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    a = args.first_file
    b = args.second_file
    stringify(generate_diff(a, b))
 #   get_plain_diff(generate_diff(a, b))


def main():
    print_result()


if __name__ == '__main__':
    main()
