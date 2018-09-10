# double_duty.py

"""Remove the pass statement then implement the following python function so
that it locates the smallest number in the list argument.

Return the smallest value found. Please do not use python's min() function.
"""
def find_min(alist):
    pass


"""Remove the pass statement then implement the following python function so
that it locates the largest number given in the list argument.

Return the largest value found. Please do not use python's max() function.
"""
def find_max(alist):
    alist.sort(reverse=True)
    return alist[0]

##############################################################################
####         STOP here. Do not modify source below.                       ####
##############################################################################


if __name__ == '__main__':
    data_a = [457, 947, 204, 571, 191, 266, 823, 326, 979, 944, 655,
        452, 727, 943, 850, 774, 611, 393, 851, 109, 784, 765, 418, 248,
        295, 239, 275, 114, 329]

    result = find_min(data_a[:])
    if result == 109:
        print ('PASSED\t find_min()')
    else:
        print ('FAILED\t find_min()')

    result = find_max(data_a[:])
    if result == 979:
        print ('PASSED\t find_max()')
    else:
        print ('FAILED\t find_max()')
