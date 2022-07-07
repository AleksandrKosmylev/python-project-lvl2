from gendiff.scripts.get_diffs import get_dict_from_file, get_dicts_difference


control_result = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False}
path_to_file_1 = "gendiff/tests/fixtures/file1.json"
path_to_file_2 = "gendiff/tests/fixtures/file2.json"
path = 'gendiff/tests/fixtures/result_get_dicts_difference.yaml'


def test_get_dict_from_file():
    assert get_dict_from_file(path_to_file_1) == control_result


def test_get_dicts_difference():
    assert get_dicts_difference(get_dict_from_file(path_to_file_1),
                                get_dict_from_file(path_to_file_2))
# assert get_dicts_difference(path_to_file_1, path_to_file_2) == open()


# open(path_to_file_1)
"""
print(get_dicts_difference(get_dict_from_file(path_to_file_1),
 get_dict_from_file(path_to_file_2)))
"""
