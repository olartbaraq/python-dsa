import array

array1: array.ArrayType = array.array("i", [1, 2, 3, 4, 5])

array1.insert(0, 0)

print(array1)

# using the array module
# the time complexity to insert an element in the array is O(N)
# while the space complexity is O(1)

# but inserting at the end of the array
