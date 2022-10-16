#!/usr/bin/env python

import argparse


from gendiff.scripts.get_diffs import generate_diff



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
    if args.format == 'plain':
        generate_diff(a, b, 'plain')
#        os.remove("gendiff/output.json")
    elif args.format == 'stylish':
        generate_diff(a, b)
#        os.remove("gendiff/output.json")
    elif args.format == 'json':
        generate_diff(a, b, 'json')
#        os.remove("gendiff/output.json")
    else:
        generate_diff(a, b)
#        os.remove("gendiff/output.json")


def main():
    print_result()


if __name__ == '__main__':
    main()
