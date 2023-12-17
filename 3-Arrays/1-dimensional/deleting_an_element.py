import array
from typing import Union


array1: array.ArrayType = array.array("i", [1, 2, 3, 4, 5, 6, 7])
array2: array.ArrayType = array.array("i", [])


def deleteElement(a: array.ArrayType, target: int) -> Union[array.ArrayType, str]:
    if len(a) == 0:
        return "array is empty"
    for i in range(len(a)):
        if a[i] == target:
            a.remove(target)
            return a
    return "element not found"


print(deleteElement(array1, 4))
print(deleteElement(array1, 10))
print(deleteElement(array2, 4))

# if deletion operation is to be performed on the last element
# then its time complexity is O(1) else its O(N)

# Space complexity is always O(1); no extra space/memory needed
