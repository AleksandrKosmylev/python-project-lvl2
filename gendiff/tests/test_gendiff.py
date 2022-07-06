from gendiff.scripts.get_diffs import get_dict_from_file, get_dicts_difference


path = 'gendiff/scripts/fixtures/file1.json'
control_result = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
path_to_file_1 = "gendiff/tests/fixtures/file1.json"
path_to_file_2 = "gendiff/tests/fixtures/file2.json"


def test_get_dict_from_file():
    assert get_dict_from_file(path) == control_result

"""
def test_get_dicts_difference():
    assert get_dicts_difference(path_to_file_1, path_to_file_2)

with open(r'gendiff/tests/test_fixtures/result_get_dicts_difference.yaml') as file:
    doc = yaml.load(file, Loader=yaml.FullLoader)

    file = yaml.dump(doc, sort_keys=False)
    print(file)

print(get_dicts_difference(get_dict_from_file(path_to_file_1), get_dict_from_file(path_to_file_2)))


"""
