import array
from typing import Union

array1: array.ArrayType = array.array("i", [1, 2, 3, 4, 5, 6, 7])
array2: array.ArrayType = array.array("i", [])


def searchArrayLinear(a: array.ArrayType, target: int) -> Union[int, str]:
    if len(a) == 0:
        return "array is empty"
    for i in range(len(a)):
        if a[i] == target:
            return i
        # print(f"my target is in index {i}")
    return "element doesn't exist in the array"


print(searchArrayLinear(array1, 4))
print(searchArrayLinear(array1, 9))
print(searchArrayLinear(array2, 9))
