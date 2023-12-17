# arrays in python can be created using to methods
# 1)  using the array module
import array

array1: array.ArrayType = array.array("i")  # O(1) space and time complexity
print(array1)
# <class 'array.array'>
array2: array.ArrayType = array.array(
    "i", [1, 2, 3, 4]
)  # O(N) space and time complexity
print(array2)  # <class 'array.array'>


# using numpy

import numpy as np


np_array = np.array([], dtype=int)  # O(1) space and time complexity
print(np_array)
# creating an empty array; using numpy doesn't create the
# array in memory if no elements are inside

np_array1 = np.array(
    [1, 2, 3, 4]
)  # O(N) space and time complexity for creating a non empty array
print(np_array1)
