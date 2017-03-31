# Function to calculate Mean
def calc_mean(numbers):
    sum = 0
    for num in numbers:
        sum += num
    mean_of_num = sum / len(numbers)
    return round(mean_of_num,2)


# Function to calculate Median
def calc_median(numbers):
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        median_of_num = calc_mean([numbers[int((length-1)/2)], numbers[int(length/2)]])
    else:
        median_of_num = numbers[int((length-1) /2)]
    return median_of_num


# Main Function
def calc_stats(i, numbers):
    print ('Iteration i = ', i)
    print ('\tMean: ', calc_mean(numbers))
    print ('\tMedian: ', calc_median(numbers))


# Provided for loop for i and numbers:
for i in range(1, 15, 2):
    numbers = [x if not x % i == 0 else 0 for x in range(101)]
    # Call your function here using i and numbers:
    calc_stats(i, numbers)
