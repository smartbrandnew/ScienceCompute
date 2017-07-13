import array
import sys
import time

import numpy as np

normal_list = []
for i in xrange(1000000):
    normal_list.append(i)

normal_array = array.array('i', normal_list)
np_array = np.array(normal_list)


def compare_size():
    print 'list: ', sys.getsizeof(normal_list)
    print 'array: ', sys.getsizeof(normal_array)
    print 'numpy array: ', sys.getsizeof(np_array)


def compare_speed():
    # type: () -> object
    beg1 = time.time()
    for i in normal_array:
        pass
    end1 = time.time()
    print 'normal list ergodic spend: {}'.format(end1 - beg1)


def multi_np_array():
    multi_array = np.array(
        [
            [1, 2, 3, 4, 5, 6],
            [10, 11, 12, 13, 14, 15],
            [20, 21, 22, 23, 24, 25],
            [30, 31, 32, 33, 34, 35],
        ]
    )
    print 'array is: ', multi_array.shape
    print 'array[3,3] is: ', multi_array[3][3]

    multi_array2 = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
    print 'np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6): ', multi_array2


def metrix_compute():
    '''
        y = x1 + x2:	add(x1, x2 [, y])
        y = x1 - x2:	subtract(x1, x2 [, y])
        y = x1 * x2:	multiply (x1, x2 [, y])
        y = x1 / x2:	divide (x1, x2 [, y]), 
        y = x1 / x2:	true divide (x1, x2 [, y]), 
        y = x1 // x2:	floor divide (x1, x2 [, y]), 
        y = -x:	negative(x [,y])
        y = x1**x2:	power(x1, x2 [, y])
        y = x1 % x2:	remainder(x1, x2 [, y]), mod(x1, x2, [, y]) 
    '''
    m1 = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
    m2 = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
    print 'm1 + m2: ', np.add(m1, m2)
    print 'm1 - m2: ', np.subtract(m1, m2)
    print 'm1 * m2: ', np.multiply(m1, m2)
    print 'm1 / m2: ', np.divide(m1, m2)
    print 'm1 / m2: ', np.true_divide(m1, m2)
    print 'm1 // m2: ', np.floor_divide(m1, m2)
    print '-m1: ', np.negative(m1)
    print 'm1 ** m2: ', np.power(m1, m2)
    print 'm1 % m2: ', np.remainder(m1, m2)


def matrix():
    matrix = np.matrix([[1,2,3],[5,5,6],[7,9,9]])
    print 'matrix compute **', matrix*matrix


if __name__ == '__main__':
    compare_size()
    compare_speed()
    multi_np_array()
    metrix_compute()
    matrix()
