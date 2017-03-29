'''***********************************************************************'''
'''***************************** PROJECT 1 *******************************'''
'''***************************** PROBLEM 3 *******************************'''

'''*************************** INCLUDE MODULES ***************************'''
import pytest
'''************************** INPUT DEFINITIONS **************************'''
list1 = [1.5,3.5,5.5,7.5]
list2 = [0,4,8,12]
'''************************ FUNCTION DEFINITIONS *************************'''

def print_list(list1, list2):
    print(list1, list2)

def iterate_list(list1, list2):
    index_outer_loop = 1
    while(True):
        exit_outer_loop = False
        print('\nIteration: ', index_outer_loop)
        for (list1_val, list2_val) in zip(list1, list2):
            multiplied = list1_val * list2_val
            print('Value 1 == ', list1_val, 'and Value 2 ==', list2_val, ' Product == ', multiplied)
            if multiplied > 300:
                exit_outer_loop = True
                break
        if exit_outer_loop == True:
            break
        else:
            index_outer_loop += 1
            list1 = [value * 2 for value in list1]
            list2 = [value * 2 for value in list2]
    print ('\nFunction complete')

'''******************************** MAIN *********************************'''

iterate_list(list1, list2)
'''***************************** END OF FILE *****************************'''