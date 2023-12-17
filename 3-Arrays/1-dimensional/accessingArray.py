import array

array1: array.ArrayType = array.array("i", [1, 2, 3, 4, 5, 6, 7])
array2: array.ArrayType = array.array("d", [1.5, 2.8, 3.7])


# print(array2[3]) # error elements in array2 is not more than 3


def accessArray(a: array.ArrayType, index: int) -> None:
    if index >= len(a):  # O(1) time complexity
        print("array index doesn't exit")  # O(1) time complexity
        return
    print(a[index])  # O(1) time complexity


# Overall :
# O(1) time complexity
# O(1) space complexity : no need for extra memory allocation

accessArray(array1, 10)
accessArray(array1, 4)
accessArray(array2, 2)
