from gendiff.logic.get_dicts_diff import get_dict_from_file
from gendiff.logic.get_diffs import generate_diff
import os


control_result = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False}


path_to_file_1_json = "tests/fixtures/flat/file1.json"
path_to_file_2_json = "tests/fixtures/flat/file2.json"
path_stringify_flat_json = "tests/fixtures/flat/test_stringify.json"
path_to_file_1_1json = "tests/fixtures/nested/file1.json"
path_to_file_2_1json = "tests/fixtures/nested/file2.json"
path_to_file_1_1yaml = "tests/fixtures/nested/file1.yaml"
path_to_file_2_1yaml = "tests/fixtures/nested/file2.yaml"
path_stringify_json = "tests/fixtures/nested/test_stringify.json"
path_plain_json = "tests/fixtures/nested/test_plain.json"


def test_get_dict_from_file():
    assert get_dict_from_file(path_to_file_1_json) == control_result


def test_stringify_flat_json():
    """"
    generate_diff(path_to_file_1_json, path_to_file_2_json)
    print(os.getcwd())
    with open("output.json", 'r') as file_1:
    """
    y = generate_diff(path_to_file_1_json, path_to_file_2_json)
    data_1 = stringify(y, spaces='  ')
    with open(path_stringify_flat_json, 'r') as file_1:
        data_2 = file_1.read()
        assert data_1 == data_2



def test_stringify_json():
    generate_diff(path_to_file_1_1json, path_to_file_2_1json)
    with open("output.json", 'r') as file_1:
        with open(path_stringify_json, 'r') as file_2:
            data_1 = file_1.read()
            data_2 = file_2.read()
            assert data_1 == data_2, '{0} != {1}'.format(data_1, data_2)


def test_stringify_yaml():
    generate_diff(path_to_file_1_1yaml, path_to_file_2_1yaml)
    with open("output.json", 'r') as file_1:
        with open(path_stringify_json, 'r') as file_2:
            data_1 = file_1.read()
            data_2 = file_2.read()
            assert data_1 == data_2, '{0} != {1}'.format(data_1, data_2)


def test_plain():
    generate_diff(path_to_file_1_1yaml, path_to_file_2_1yaml, "plain")
    with open("output.json", 'r') as file_1:
        with open(path_plain_json, 'r') as file_2:
            data_1 = file_1.read()
            data_2 = file_2.read()
            assert data_1 == data_2
