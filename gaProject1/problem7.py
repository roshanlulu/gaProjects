# Import standard modules
import numpy


# Given data
predictions = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

true_values = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]


def calc_rmse(true_values, predictions):
    # Two ways of calculating error are given below - 1. Converting given lists to arrays 2. Using zip on the given lists
    # errors = [numpy.array(predictions) - numpy.array(true_values)]
    errors = [value_predicted - value_observed  for (value_predicted, value_observed) in zip(predictions, true_values)]
    sq_errors =  [ error ** 2 for error in errors]
    avg_sq_error = numpy.mean(sq_errors)
    rmse = numpy.sqrt(avg_sq_error)
    print('RMSE = ', rmse)
    return rmse


calc_rmse(true_values, predictions)
