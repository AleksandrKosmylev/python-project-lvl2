from gendiff.scripts.get_diffs import get_dict_from_file, get_dicts_difference
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.get_diffs import stringify
from gendiff.scripts.get_diffs import get_plain_diff
from gendiff.scripts.get_diffs import convert_to_file
import os
from gendiff.scripts.get_diffs import output_path


control_result = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False}


path_to_file_1_json = r"tests/fixtures/first_stringify/file1.json"
path_to_file_2_json = r"tests/fixtures/first_stringify/file2.json"
path_to_file_1_1json = r"tests/fixtures/second/file1.json"
path_to_file_2_1json = r"tests/fixtures/second/file2.json"
path_to_file_1_1yaml = r"tests/fixtures/second/file1.yaml"
path_to_file_2_1yaml = r"tests/fixtures/second/file2.yaml"


def test_get_dict_from_file():
    assert get_dict_from_file(path_to_file_1_json) == control_result


def test_stringify_flat_json():
    generate_diff(path_to_file_1_json, path_to_file_2_json)
    with open(output_path, 'r') as file_1:
        with open("tests/fixtures/first_stringify/test_stringify.json", 'r') as file_2:
            data_1 = file_1.read()
            data_2 = file_2.read()
            try:
                assert data_1 == data_2
            finally:
                os.remove(output_path)


def test_stringify_json():
    generate_diff(path_to_file_1_1json, path_to_file_2_1json)
    with open(output_path, 'r') as file_1:
        with open("tests/fixtures/second/test_stringify.json", 'r') as file_2:
            data_1 = file_1.read()
            data_2 = file_2.read()
            assert data_1 == data_2 , '{0} != {1}'.format(data_1, data_2)


def test_stringify_yaml():
    generate_diff(path_to_file_1_1yaml, path_to_file_2_1yaml)
    with open(output_path, 'r') as file_1:
        with open("tests/fixtures/second/test_stringify.json", 'r') as file_2:
            data_1 = file_1.read()
            data_2 = file_2.read()
            assert data_1 == data_2 , '{0} != {1}'.format(data_1, data_2)


def test_plain():
    generate_diff(path_to_file_1_1yaml, path_to_file_2_1yaml, "plain")
    with open(output_path, 'r') as file_1:
        with open("tests/fixtures/second/test_plain.json", 'r') as file_2:
            data_1 = file_1.read()
            data_2 = file_2.read()
            try:
                assert data_1 == data_2
            finally:
                os.remove(output_path)