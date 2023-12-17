import array

array1: array.ArrayType = array.array("i", [1, 2, 3, 4, 5, 6, 7])
array2: array.ArrayType = array.array("d", [1.5, 2.8, 3.7])


array2.insert(1, 4.7)  # O(N)


def traverse_array(a: array.ArrayType) -> None:
    for element in a:  # O(N)
        print(element)  # O(1)


# Overall time complexity is O(N) and space complexity is O(1) because
# no need to use another memory for the operation


traverse_array(array2)
