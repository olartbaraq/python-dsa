import array

array1: array.ArrayType = array.array("i", [1, 2, 3, 4, 5])

array1.insert(0, 0)


# tobytes method
print(array1.tobytes())


# frombytes method
intsArray: array.ArrayType = array.array("i", [])
intsArray.frombytes(
    b"\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00"
)
print(intsArray)

# extends - to append a new array to an existing array
# count - to count the number of occurences in an array
# pop - to remove the last element of an array
print(array1.pop())

# append  - to include an element to the end of an array
# tolist - to convert an array to list
print(array1.tolist())

# reverse - to reverse the list from the end to the start

# slice elements from an array
print(array1[:3])
