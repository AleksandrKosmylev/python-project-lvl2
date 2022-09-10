import yaml

from gendiff.scripts.get_diffs import get_dict_from_file, get_dicts_difference
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.get_diffs import stringify
import sys
import json

from tests import fixtures



control_result = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False}


path_to_file_1_json = r"fixtures/file1.json"
path_to_file_2_json = r"fixtures/file2.json"




"""
original_stdout = sys.stdout
file_json = open("stringify_output.json", 'w')
sys.stdout = file_json
first = get_dict_from_file(path_to_file_1_json)
second = get_dict_from_file(path_to_file_2_json)
g = get_dicts_difference(first, second)
stringify(g)
file_json.close()
file_json_read = open(r"tests/fixtures/stringify_output.json")
"""


def test_get_dict_from_file():
    assert get_dict_from_file(path_to_file_1_json) == control_result

def test_stringify_flat_json():
    file_json = open("stringify_output.json", 'w')
    sys.stdout = file_json
    first = get_dict_from_file(path_to_file_1_json)
    second = get_dict_from_file(path_to_file_2_json)
    g = get_dicts_difference(first, second)
    stringify(g)
    file_json.close()
    with open("stringify_output.json", 'r') as file_1:
        with open("fixtures/flat.json", 'r') as file_2:
            data_1 = file_1.read()
            data_2 = file_2.read()
            assert data_1 == data_2
with open("stringify_output.json", 'r') as fileinput:
   for line in fileinput:
       line = line.lower()
"""
def test_get_dicts_difference():
    a = get_dicts_difference(get_dict_from_file(path_to_file_1_json),
                                get_dict_from_file(path_to_file_2_json))
    assert a == f
#    assert str(yaml.dump(a, sort_keys=False)) == f
#    assert get_dicts_difference(get_dict_from_file(path_to_file_1_json),
#                                get_dict_from_file(path_to_file_2_json)) == f
"""
"""
def test_generate_diff_is_str():
    g = generate_diff(path_to_file_1_json, path_to_file_2_json)
    assert (isinstance(g, str)) is True





    file_json.close()
    with open(path_to_file_1_json,'r') as file_1:
        with open(path_to_file_2_json, 'r') as file_2:
            same = set(file_1).difference(file_2)
"""