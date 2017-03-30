
def calc_mean(i, numbers):
    sum = 0
    length = len(numbers)
    for num in numbers:
        sum += num
    mean_of_num = sum / len(numbers)
    return mean_of_num

def calc_median(i, numbers):
    numbers.sort()
    median_of_num = 0
    length = len(numbers)
    if length % 2 == 0:
        median_of_num = numbers[(int((length - 1) / 2) + int(length / 2))]
    else:
        median_of_num = numbers[int((length -1) /2)]
    return median_of_num


def calc_stats(i, numbers):
    print ('Iteration i = ', i)
    print ('Mean: ', calc_mean(i, numbers))
    print ('Median: ', calc_median(i, numbers))
