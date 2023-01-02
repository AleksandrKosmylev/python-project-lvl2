import argparse
from gendiff.get_diffs import generate_diff


def print_result():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        add_help=False)
    parser.add_argument("-V", '--version', action='version', version='1.0')
    parser.add_argument("-f", '--format', metavar='',
                        help='output format (default: "stylish")')
    parser.add_argument('-h', '--help', action='help',
                        default=argparse.SUPPRESS,
                        help='display help for command')
    parser.add_argument('filepath1', type=str, help=argparse.SUPPRESS)
    parser.add_argument('filepath2', type=str, help=argparse.SUPPRESS)
    args = parser.parse_args()
    a = args.filepath1
    b = args.filepath2
    print(generate_diff(a, b, args.format))
