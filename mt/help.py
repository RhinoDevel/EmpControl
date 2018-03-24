
def get_first_dict_index(dict_list, key, val):
    for i, dict in enumerate(dict_list):
        if dict[key] == val:
            return i
    return -1
