#!/usr/bin/env python
import argparse


def main():
    print('Welcome to the gendiff!')





if __name__ == '__main__':
    main()

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument("-f", "--format",
help = "set format of output")
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
args = parser.parse_args()
if args.format:
    print(args.first_file)
else:
    print(args.second_file)



