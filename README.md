# Difference calculator
### Description
Python module shows difference between two *.json/*.yaml files.
The difference can be returned in 3 variants, depending on the selected format.<br />
Format options:
- 'stylish' - return result as a "tree" of difference
- 'plain' - returns result in the form of a string
- 'json' - raw structure of difference file

### Requirements

- python3 version  3.9.x
- poetry versiob >= 1.0.0

### Installation and usage
- clone repository to directory on your computer
- enter "make install" to instal poetry 
- enter "make package-install" to install the difference calculator module
-  enter gendiff -f (format) (path to the first file) (path to the second file)"

Example: <br />
gendiff -f stylish tests/fixtures/nested/file1.json tests/fixtures/nested/file2.json

### Links

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [flake8](https://flake8.pycqa.org/en/latest/)                               | "Python linter"


### Hexlet tests and linter status:
[![Actions Status](https://github.com/AleksandrKosmylev/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/AleksandrKosmylev/python-project-lvl2/actions)
[![Github Actions Status](https://github.com/AleksandrKosmylev/python-project-lvl2/workflows/my_linter/badge.svg)](https://github.com/AleksandrKosmylev/python-project-lvl2/actions)
<a href="https://codeclimate.com/github/AleksandrKosmylev/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/704e005c09d2fde798db/maintainability" /></a>
<a href="https://codeclimate.com/github/AleksandrKosmylev/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/704e005c09d2fde798db/test_coverage" /></a>
<a href="https://asciinema.org/a/imybU39RvX12tvVTLke35rvbU" target="_blank"><img src="https://asciinema.org/a/imybU39RvX12tvVTLke35rvbU.svg" /></a>
