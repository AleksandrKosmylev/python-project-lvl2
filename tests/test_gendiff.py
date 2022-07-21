import yaml
from gendiff.scripts.get_diffs import get_dict_from_file, get_dicts_difference
from gendiff.scripts.gendiff import generate_diff


control_result = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False}


path_to_file_1_json = "tests/fixtures/file1.json"
path_to_file_2_json = "tests/fixtures/file2.json"


with open(r'tests/fixtures/result_get_dicts_difference.yaml') as file:
    f = yaml.load(file, Loader=yaml.FullLoader)


def test_get_dict_from_file():
    assert get_dict_from_file(path_to_file_1_json) == control_result


def test_get_dicts_difference():
    a = get_dicts_difference(get_dict_from_file(path_to_file_1_json),
                                get_dict_from_file(path_to_file_2_json))
    assert a == f
#    assert str(yaml.dump(a, sort_keys=False)) == f
#    assert get_dicts_difference(get_dict_from_file(path_to_file_1_json),
#                                get_dict_from_file(path_to_file_2_json)) == f

"""
def test_generate_diff_is_str():
    g = generate_diff(path_to_file_1_json, path_to_file_2_json)
    assert (isinstance(g, str)) is True

"""