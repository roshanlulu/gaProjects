# Project 1 - Problem 1

# Include import modules
import pytest
import string

# Data provided
input_dict = {
    'list': [1, 2, 3, 4],
    'tuple': ('cat', 'dog'),
    'integer': 1,
    'float': 99.99,
    1: 'integer',
    2: 'integer_2',
    'Uppercase_string': 'ABCD',
    'CHARACTER': 'C'
}



'''************************ FUNCTION DEFINITIONS *************************'''
# Print dictionary function
def print_dict(input_dict):
    # Print dictionary
    for key, value in input_dict.items():
        print(key, ' : ', value)


# Modify the dictionary value based on the 1st letter of the Key values.
def iterate_dict(input_dict):
    lowercase = string.ascii_lowercase
    vowels = 'aeiou'
    updated_dict = {}
    for key in input_dict:
        key_char = str(key)[0].lower()
        if key_char in vowels:
            updated_dict.update({key : 'vowel'})
        elif key_char in lowercase:
            updated_dict.update({key : 'consonant'})
        else:
            ''' Nothing to do '''
    return updated_dict


'''************************ MAIN *************************'''

# Print contents of the dictionary. Modify & re-print the updated dictionary
print ('Given Dictionary')
print_dict(input_dict)
print ()
print ('Modified Dictionary \n')
print_dict (iterate_dict (input_dict))


'''************************ END OF FILE *************************'''