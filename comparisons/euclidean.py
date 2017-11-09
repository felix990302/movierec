from math import sqrt


@staticmethod
def euclideanDist(a, b):
    return sqrt(a ** 2 + b ** 2)


@staticmethod
def invEuclideanDist(a, b):
    return 1 / (1 + euclideanDist(a, b))
