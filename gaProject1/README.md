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

## Review Problem 3

    Write a function that will iterate through two lists and perform an operation.

    Define a function that:

    Accepts two arguments that are lists of numbers (either float or integer):
    - Print both of the lists.
    - Construct a while loop that:
    - Prints the current iteration number, starting at 1.
    - Iteration: 1
    - Iterates through each element of both lists at the same time using a for loop, assigning the number from list 1 to a variable value1 and the number from list 2 to a variable value2. For example, if list1 == [1, 2] and list2 == [3, 4], there will be two iterations through the for loop:
    - Iteration 1 will have `value1 == 1and ``value2 == 3```
    - Iteration 2 will have `value2 == 2and ``value2 == 4```
    - Within the for loop:
    - Multiply value1 and value2 together and assign it to variable multiplied.
    - Print multiplied.
    - If multiplied is greater than 300, break out of the for loop and while loop.
    - Otherwise, multiply each element of list 1 and list 2 by 2 before continuing through the while loop
    - Print “Function complete.”
    Notes/Hints:
    
    - To break out of a for loop or while loop at any time, use the break command.
    - ex:
    - for i in my_list: 
        if i > 10: 
            break
    - The zip() function will join lists/tuples element by element.
    - ex:
    - zip([1,2], [3,4]) == [(1, 3), (2, 4)]
    - In a for loop, you can assign multiple variables at a time:
    - for value1, value2 in zip(list1, list2):
    - while True can run a loop until a break condition is reached. Be careful!


## Review Problem 4
    
    Write a function that calculates summary statistics for distributions.
    
    Define a function that:
    
    - Accepts two arguments, i and numbers.
    - Prints a string indicating what the current i is.
    - Calculate, without using numpy, the mean of numbers.
    - Calculate, without using numpy, the median of numbers.
    - Print the mean and median, for example:
    - mean: 12
    - median: 9
    Notes/Hints:
    
    - You should define your function outside of the provided for loop, and then call it with i and numbers within the for loop.
    - for i in range(1, 15, 2) assigns i from 1 to 15 with a step size of 2.

## Review Problem 5
    Define a function that calculates the pearson correlation coefficient between two lists of numbers.

    Your function will:
    
    - Accept two arguments (the provided lists X and Y).
    - Print the length of X and Y like so:
    - Length of X: 40
    - Length of Y: 40
    Calculate the pearson correlation coefficient between the two lists and assign the value to variable pearson_r.
    - Create a variable X_deviation that is each element of X minus the mean of X.
    - Create a variable Y_deviation that is each element of Y minus the mean of Y.
    - Create a variable sqrt_X_deviation_sq that is the square root of the sum of the square of each element of X_deviation.
    - Create a variable sqrt_Y_deviation_sq that is the same thing you just did but for Y_deviation.
    - Create a variable sum_XY_deviation that is the sum of each element of X and Y multiplied by each other, in order. You can use the zip() function to iterate through two lists at the same time:
      `for x_d, y_d in zip(X_deviation, Y_deviation):`
    - pearson_r is equal to sum_XY_deviation divided by (sqrt_X_deviation_sq * sqrt_Y_deviation_sq).
    Print pearson_r.
    Check if it is the same as numpy's correlation function. Print np.corrcoef(X, Y)[0,1]

## Review Problem 6
    For this problem you will be defining a function that calculates the spearman rank correlation coefficient between two lists. Spearman's rho is a measure of how related two sets of numbers are.

    Your function will:
    
    - Accept the provided lists of numbers defined for problem 5, X and Y.
    - Calculate the rank of the numbers in the X and Y lists. The rank is a number that defines what index position each number would be if the list were in order.
        - For example: say list1 = [5,2,0,9,-5], then list1_rank = [3,2,1,4,0]
        - Calculating the rank is not trivial. You can use the rankdata() function from scipy.stats on a list to get the ranks of the numbers.
        - Assign the rank of list X to variable X_rank and list Y to variable Y_rank.
    - Manually calculate the covariance between X_rank and Y_rank as XY_rank_cov:
        - Calculate X_mean: the mean of X_rank using np.mean().
        - Calculate Y_mean: the mean of Y_rank using np.mean().
        - Calculate X_deviation: subtract X_mean from each element of X_rank.
        - Calculate Y_deviation: subtract Y_mean from each element of Y_rank.
        - Calculate XY_d: multiply X_deviation with Y_deviation, element by element. You can use pythons zip() function to iterate across lists at the same time:
            for xd, yd in zip(X_deviation, Y_deviation):
        - Calculate sum_XY_d: the sum of the elements in XY_d with np.sum.
        - Calculate XY_rank_cov: divide sum_XY_d by len(XY_d).
    - Calculate the standard deviations X_rank_std and Y_rank_std of the X_rank and Y_rank lists. You can use np.std().
    - Calculate the spearman rank correlation coefficient as XY_spearman: divide XY_rank_cov by (X_rank_std * Y_rank_std).
    - Print XY_spearman.
    - Compare your value to the scipy function for spearman: print out spearmanr(X, Y).

## Review Problem 7
    
    Write a function to calculate the root mean squared error, often written as RMSE. The RMSE is a popular measure of performance of predictions when you have a set of observed values and a set of predicted values. Your predicted values in this case are your “predictions” of what the true, observed values are.
    
    Your function will:
    
    - Accept two predefined lists as arguments: `true_valuesand ``predictions```.
    - Calculate the error between `predictionsand ``true_values` as variableerrors``:
        - Element by element, calculate the prediction minus the true value.
    - Calculate the square of each element in `errorsand assign this to variable ``sq_errors```.
    - Calculate `avg_sq_error, the mean of ``sq_errors```.
    - Calculate `rmse, the square root of ``avg_sq_error` usingnp.sqrt()``.
    - Print `rmse`.
    - Return `rmse`.

## Review Problem 8

## Review Problem 9

## Review Problem 10
