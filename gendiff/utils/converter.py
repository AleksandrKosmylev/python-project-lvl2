def convert(x):
    for index, piece in enumerate(x):
        check_dict = {"True": "true", "False": "false", "None": "null"}
        if str(piece) in list(check_dict.keys()):
            x[index] = check_dict[str(piece)]
    return x
