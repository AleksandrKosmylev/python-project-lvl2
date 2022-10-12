#!/usr/bin/env python

import argparse


from gendiff.scripts.get_diffs import generate


def generate_diff():
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
        generate(a, b, 'plain')
#        os.remove("gendiff/output.json")
    elif args.format == 'stylish':
        generate(a, b)
#        os.remove("gendiff/output.json")
    elif args.format == 'json':
        generate(a, b, 'json')
#        os.remove("gendiff/output.json")
    else:
        generate(a, b)
#        os.remove("gendiff/output.json")


def main():
    generate_diff()


if __name__ == '__main__':
    main()
