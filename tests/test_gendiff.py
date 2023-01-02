from gendiff.get_dicts_diff import get_dict_from_file, get_dicts_diff
from gendiff.formatters import stringify, get_plain_diff


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
"""
path_to_file_1_json = "fixtures/flat/file1.json"
path_to_file_2_json = "fixtures/flat/file2.json"
path_stringify_flat_json = "fixtures/flat/test_stringify.json"

path_to_file_1_1json = "fixtures/nested/file1.json"
path_to_file_2_1json = "fixtures/nested/file2.json"
path_to_file_1_1yaml = "fixtures/nested/file1.yaml"
path_to_file_2_1yaml = "fixtures/nested/file2.yaml"
path_stringify_json = "fixtures/nested/test_stringify.json"
path_plain_json = "fixtures/nested/test_plain.json"
"""


def test_get_dict_from_file():
    assert get_dict_from_file(path_to_file_1_json) == control_result


def test_stringify_flat_json():
    dict_1 = get_dict_from_file(path_to_file_1_json)
    dict_2 = get_dict_from_file(path_to_file_2_json)
    y = get_dicts_diff(dict_1, dict_2)
    data_1 = str(stringify(y, spaces='  '))
    with open(path_stringify_flat_json, 'r') as file_1:
        data_2 = file_1.read()
    assert data_1 == data_2


def test_stringify_json():
    dict_1 = get_dict_from_file(path_to_file_1_1json)
    dict_2 = get_dict_from_file(path_to_file_2_1json)
    y = get_dicts_diff(dict_1, dict_2)
    data_1 = str(stringify(y, spaces='  '))
    with open(path_stringify_json, 'r') as file_1:
        data_2 = file_1.read()
    assert data_1 == data_2


def test_stringify_yaml():
    dict_1 = get_dict_from_file(path_to_file_1_1yaml)
    dict_2 = get_dict_from_file(path_to_file_2_1yaml)
    y = get_dicts_diff(dict_1, dict_2)
    data_1 = str(stringify(y, spaces='  '))
    with open(path_stringify_json, 'r') as file_1:
        data_2 = file_1.read()
    assert data_1 == data_2


def test_plain():
    dict_1 = get_dict_from_file(path_to_file_1_1yaml)
    dict_2 = get_dict_from_file(path_to_file_2_1yaml)
    y = get_dicts_diff(dict_1, dict_2)
    data_1 = str(get_plain_diff(y))
    with open(path_plain_json, 'r') as file_1:
        data_2 = file_1.read()
    assert data_1 == data_2
