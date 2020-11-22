import numpy as np


def regularize_cov(covariance, epsilon):
    # regularize a covariance matrix, by enforcing a minimum
    # value on its singular values. Explanation see exercise sheet.
    #
    # INPUT:
    #  covariance: matrix
    #  epsilon:    minimum value for singular values
    #
    # OUTPUT:
    # regularized_cov: reconstructed matrix

    #####Insert your code here for subtask 6d#####
    # covariance matrix is a symmetric matrix
    n,m = covariance.shape
    # n and m must be equal to the dimension, d.
    
    regularized_cov = covariance + epsilon*np.eye(n,m)
    return regularized_cov
