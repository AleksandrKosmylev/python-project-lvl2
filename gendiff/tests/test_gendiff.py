from gendiff.scripts.get_diffs import get_dict_from_file


path = '/home/aleksandr/hexlet/projects/python-project-lvl2/gendiff/scripts/fixtures/file1.json'
control_result = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}


def test_get_dict_from_file():
    assert get_dict_from_file(path) == control_result
