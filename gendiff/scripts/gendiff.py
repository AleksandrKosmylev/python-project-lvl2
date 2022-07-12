#!/usr/bin/env python
import argparse
# import yaml
from gendiff.scripts.get_diffs import get_dict_from_file, get_dicts_difference


def generate_diff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument("-f", "--format",
                        help="set format of output")
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    a = args.first_file
    b = args.second_file
    result = get_dicts_difference(get_dict_from_file(a), get_dict_from_file(b))
    print(result)
#    print(yaml.dump(result))


def main():
    generate_diff()


if __name__ == '__main__':
    main()
