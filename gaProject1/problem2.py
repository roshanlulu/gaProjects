
# Data provided
test_dict = {
    'A':[1,2,3,4,5],
    'B':[12.1, 14.2, 20.3, 25.4],
    'C':[10, 25.5, 50.9, 101]
}

optional_remainder = [2,3,4,5]


# Print dictionary function
def print_dict(input_dict):
    # Print dictionary
    for key, value in input_dict.items():
        print(key, ' : ', value)

# This function sets the reminder list and calls the iterate dictionary function
def iterate_dict(dict_of_lists, remainder = []):
    # Append 2 if no valid list is passed
    if len(remainder) == 0:
        remainder.append(2)
    # Print Dictionary and list
    print_dict(dict_of_lists)
    print (remainder)
    # Iterate through the dictionary
    modify_dict(dict_of_lists, remainder)

# Function that modifies the dictionary contents
def modify_dict(dict_of_lists, remainder):
    new_dict = {}
    for key, value in dict_of_lists.items():
        nested_dict = {}
        for value_item in value:
            list_of_rem = []
            for remainder_item in remainder:
                val = value_item % remainder_item
                if type(val) == float:
                    val = round(val, 1)
                list_of_rem.append(val)
            nested_dict[value_item] = list_of_rem
        new_dict[key] = [nested_dict]
    print_dict(new_dict)
    return (new_dict)


iterate_dict(test_dict, optional_remainder)

