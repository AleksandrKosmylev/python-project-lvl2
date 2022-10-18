from gendiff.scripts.get_diffs import get_dict_from_file, get_dicts_difference
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.get_diffs import stringify
from gendiff.scripts.get_diffs import get_plain_diff
from gendiff.scripts.get_diffs import convert_to_file
import os



control_result = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False}

test_directory = os.getcwd()

path_to_file_1_json = "tests/fixtures/first_stringify/file1.json"
path_to_file_2_json = "tests/fixtures/first_stringify/file2.json"
path_stringify_flat_json = test_directory + "/fixtures/first_stringify/test_stringify.json"
path_to_file_1_1json = test_directory + "/fixtures/second/file1.json"
path_to_file_2_1json = test_directory + "/fixtures/second/file2.json"
path_to_file_1_1yaml = test_directory + "/fixtures/second/file1.yaml"
path_to_file_2_1yaml = test_directory + "/fixtures/second/file2.yaml"
path_stringify_json = test_directory + "/fixtures/second/test_stringify.json"
path_plain_json = test_directory + "/fixtures/second/test_plain.json"





def test_get_dict_from_file():
    assert get_dict_from_file(path_to_file_1_json) == control_result


def test_stringify_flat_json():
    generate_diff(path_to_file_1_json, path_to_file_2_json)
    with open("tests/fixtures/first_stringify/file1.json", 'r') as file_1:
        with open(path_stringify_flat_json, 'r') as file_2:
            data_1 = file_1.read()
            data_2 = file_2.read()
            try:
                assert data_1 == data_2
            finally:
                os.remove(output_path)


def test_stringify_json():
    generate_diff(path_to_file_1_1json, path_to_file_2_1json)
    with open(output_path, 'r') as file_1:
        with open(path_stringify_json, 'r') as file_2:
            data_1 = file_1.read()
            data_2 = file_2.read()
            assert data_1 == data_2 , '{0} != {1}'.format(data_1, data_2)


def test_stringify_yaml():
    generate_diff(path_to_file_1_1yaml, path_to_file_2_1yaml)
    with open(output_path, 'r') as file_1:
        with open(path_stringify_json, 'r') as file_2:
            data_1 = file_1.read()
            data_2 = file_2.read()
            assert data_1 == data_2 , '{0} != {1}'.format(data_1, data_2)


def test_plain():
    generate_diff(path_to_file_1_1yaml, path_to_file_2_1yaml, "plain")
    with open(output_path, 'r') as file_1:
        with open(path_plain_json, 'r') as file_2:
            data_1 = file_1.read()
            data_2 = file_2.read()
            try:
                assert data_1 == data_2
            finally:
                os.remove(output_path)