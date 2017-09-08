import numpy as np


def outlier_threshold(data, m=5.):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    return m * mdev
