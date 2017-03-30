# Given Data
first_dict = {'A':(1,2), 'B':[1,2,3,4,4], 'C':[0,9], 1:(1,1,1), 12:None, 'D':None, 'E':12.777}
second_dict = {'1':('a','b'), 2:{1:23.3}, 3:'four', 4:'five', 'five':['six', 'seven'], 8:'nine'}


def check_kvtype(key, key_type, value, value_type):
    if type(key) is key_type and type(value) is value_type:
        return True
    else:
        return False


def string_intlist_cleaner(dict):
    clean_dict = {}
    for key, value in dict.items():
        if check_kvtype(key, str, value, list):
            clean_dict.update({key: value})
            # del clean_dict[key] - Why dint del work?
    return clean_dict


def int_string_cleaner(dict):
    clean_dict = {}
    [clean_dict.update({key: value})
        if check_kvtype(key, int, value, str) else None
        for key, value in dict.items()]
    return clean_dict


def dict_cleaner(first_dict, second_dict):
    print ('Dictionary 1: ', first_dict)
    print('Dictionary 2: ', second_dict)
    clean_merge_dict = {}
    clean_merge_dict.update(string_intlist_cleaner(first_dict))
    clean_merge_dict.update(int_string_cleaner(second_dict))
    return clean_merge_dict


print(dict_cleaner(first_dict, second_dict))
