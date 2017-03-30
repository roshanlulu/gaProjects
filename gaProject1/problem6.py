# Import standard modules
import numpy
import scipy.stats as stats


# Given Data
X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]


def get_covariance(X, Y):
    X_mean = numpy.mean(X)

    Y_mean = numpy.mean(Y)
    # Get deviation
    X_deviation = [x_value - X_mean for x_value in X]
    Y_deviation = [y_value - Y_mean for y_value in Y]
    XY_d = [xd * yd for xd, yd in zip(X_deviation, Y_deviation)]
    sum_XY_d = numpy.sum(XY_d)
    # Get Covariance
    XY_rank_cov = sum_XY_d / len(XY_d)
    return XY_rank_cov


def get_std_deviation(X):
    return numpy.std(X)


def calc_spearmans_rho(X, Y):
    # Rank the list data
    X_rank = stats.rankdata(X, method = 'ordinal')
    Y_rank = stats.rankdata(Y, method='ordinal')
    #Calculate covariance between the rank lists get_covariance
    XY_rank_cov = get_covariance(X_rank, Y_rank)
    # Get Std deviation of each rank lists
    X_std_dev = get_std_deviation(X_rank)
    Y_std_dev = get_std_deviation(Y_rank)
    # Evaluate SPCC
    XY_spearman = XY_rank_cov / (X_std_dev * Y_std_dev)
    # Evaluate SPCC using scipy library
    XY_scipy_spearman = stats.spearmanr(X, Y)
    print ('SPCC = ', XY_spearman)
    print('SPCC Scipy = ', XY_scipy_spearman)


calc_spearmans_rho(X, Y)
