import numpy as np

array1 = np.array([[1, 2, 3, 4], [7, 8, 9, 10], [-1, 3, 0, 5]])
array2 = np.array([])
# print(array1[1][3])


# Inserting to a two dimensional array
# insert(array_to_be_inserted_to, index, [[values of array you want to insert], axis])
# arrayToInsert = np.array([3, 19, 100, -4])
# arrayToInsert = arrayToInsert.reshape(-1, 1)
# newArray = np.insert(array1, 1, arrayToInsert, axis=1)
# print(newArray)

# accessing an element in 2D array


def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        return "Invalid Index"
    return array[rowIndex][colIndex]


print(accessElement(array1, 1, 3))
print(accessElement(array1, 4, 3))


# traversing 2D array
def traverse2DArray(arr):
    if len(arr) == 0:
        return "array is empty"
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end="\t")


print(traverse2DArray(array1))


# Searching 2D array
def searchIn2DArray(arr, x):
    if len(arr) == 0:
        return "array is empty"
    # Iterate through each element of arr[]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == x:
                return f"the index for the value {x} is located in {i}, {j}"
    return "the element doesn't exist"


print(searchIn2DArray(array1, -1))
print(searchIn2DArray(array2, -100))


# deletion of a column or row in 2D array
newTDArray = np.delete(array1, 0, axis=1)
print(newTDArray)
