import problem1


output_p1 = {
    'list':'consonant',
    'tuple':'consonant',
    'integer':'vowel',
    'float':'consonant',
    'Uppercase_string':'vowel',
    'CHARACTER':'consonant'
}

def test_problem1():
    assert problem1.iterate_dict(problem1.input_dict) == output_p1
    print(output_p1)