# Import standard modules
import numpy
import math


# Given Data
X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]


# Print input lists
def print_lists(X, Y):
    print ('Length of x: ', len(X))
    print ('Length of y: ', len(Y))


def calc_correlation(X, Y):
    # Find Mean and Deviation of the lists
    X_mean = numpy.mean(X)
    X_deviation = [value_x - X_mean for value_x in X]
    Y_mean = numpy.mean(Y)
    Y_deviation = [value_y - Y_mean for value_y in Y]
    # Calculate Variance and Standard Deviation (Square root of Variance)
    X_variance = numpy.sum([value ** 2 for value in X_deviation])
    sqrt_X_deviation_sq = math.sqrt(X_variance)
    Y_variance = numpy.sum([value ** 2 for value in Y_deviation])
    sqrt_Y_deviation_sq = math.sqrt(Y_variance)
    # Calculate Covariance
    sum_XY_deviation = numpy.sum([(x_d * y_d) for (x_d, y_d) in zip(X_deviation, Y_deviation)])
    # Calculate pearson relation
    pearson_r = sum_XY_deviation / (sqrt_X_deviation_sq * sqrt_Y_deviation_sq)
    pearson_r_using_fn = numpy.corrcoef(X, Y)
    # Print correlation values
    print ('Pearson Coefficient Relation: ', pearson_r)
    print ('Numpy Correlation Coefficient Relation: ', pearson_r_using_fn)


print_lists(X, Y)
calc_correlation(X, Y)
