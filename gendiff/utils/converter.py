def convert(data):
    for index, piece in enumerate(data):
        check_dict = {"True": "true", "False": "false", "None": "null"}
        if str(piece) in list(check_dict.keys()):
            data[index] = check_dict[str(piece)]
    return data
