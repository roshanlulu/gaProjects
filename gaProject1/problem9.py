'''***********************************************************************'''
'''***************************** PROJECT 1 *******************************'''
'''***************************** PROBLEM 9 *******************************'''

'''*************************** INCLUDE MODULES ***************************'''

'''************************** INPUT DEFINITIONS **************************'''

'''************************ FUNCTION DEFINITIONS *************************'''

'''******************************** MAIN *********************************'''

# Read the csv file
raw_file = ''
with open('./pokedex_basic.csv', 'r') as pokefile:
    raw_file = pokefile.read()

##################################### 9A ###################################

# Initialize a list
poke_list9A = []
# Loop through each line in the file
for row in raw_file.splitlines():
    # Split the contents of the line
    row = row.split(',')
    poke_sublist = []
    for word in row:
        # Delete double quotes in a word
        word = word.replace('"', '')
        if word.isdigit() == True:
            # Convert digits to floats
            word = float(word)
        elif len(word.strip()) == 0:
            # Replace blank cells with -1
            print('found u')
            word = -1
        # Append word to the sub list
        poke_sublist.append(word)
    # Append sublist to the list
    poke_list9A.append(poke_sublist)

# Print Pokedex list
print(poke_list9A)

##################################### 9B ###################################

# List comprehension equivalent of 9A
poke_list9B = [([float(word.replace('"', '')) if word.replace('"', '').isdigit()
                    else -1 if len(word.replace('"', '').strip()) == 0
                    else word.replace('"', '')
                    for word in row.split(',')])
                    for row in raw_file.splitlines()]


################################## ASSERT ###################################

assert (poke_list9A == poke_list9B)

'''***************************** END OF FILE *****************************'''