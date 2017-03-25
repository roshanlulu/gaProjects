# Project1 - Review Python Syntax Structure and Concepts

## Review Problem 1

    For this problem you will be writing a function that the supplied dictionary input_dict and operates on it.
    Define a function that:
    - Accepts 1 argument, which will be a dictionary.
    - Prints the dictionary.
    - Iterates through the key:value pairs of the dictionary:
    - For pairs where the key starts with a lowercase vowel, change the value to “vowel”.
    - For pairs where the key starts with a lowercase consonant, change the value to “consonant”.
    - Remove all other pairs from the dictionary.
    - Prints the modified dictionary.
    - Returns the modified dictionary.

    Notes/Hints:
    - You can check if a character is in a string with in.
    ex: if ch in st:
    - You can create a new dictionary to store the modified return values or operate on the input dictionary.
    - You can check types using the `type()` python function:
    type(1) == int
    type(1.2) == float
    type('ab') == str
    type((1,2)) == tuple
    type([3,2]) == list
    type({'a':'b'}) == dict
    
## Review Problem 2

    Write a function that operates on a dictionary and an optional list of numbers.
    Define a function that:
    - Accepts a dictionary as its first argument. The values of the dictionary should be a list of numbers.
    - Accepts an optional keyword argument that will be a list. The default should be an empty list. Name the optional keyword list remainder.
    - If remainder is empty: append a 2 to remainder.
    - Print the dictionary as well as remainder.
    - Iterate though they key:value pairs in the dictionary:
    - For each value list of numbers, calculate the remainder of each number for each number in the remainder list.
    - Create a dictionary where the keys are the numbers in the value list, and the values are the remainders of that number from the remainder list.
    - ex: if a value in the dictionary is [10,9] and remainder is [2,3], the new dictionary would be: {10:[0, 1], 9:[1, 0]}
    - Keep the original key of the input dictionary, but change the value to the new dictionary of remainders.
    - Print out the final output dictionary.
    - Return the output dictionary.
    Notes/Hints:
    - keyword arguments are specified in functions like so:
    - def example_function(arg1, kwarg1=default_value):
    - The operator for finding the remainder of two values is “modulus”: `%`
    14 % 5 == 4
