from typing import List


exampleList: List[int] = [1, 2, 3, 4, 5, 6, 7]


def updateList(items: List[int], index, value: int) -> List[int]:
    items[index] = value
    return items


def insertElementAnyWhere(items: List[int], index, value: int) -> List[int]:
    # inserting at the beginning or any given location
    items.insert(index, value)  # O(N) time complexity
    return items


def insertElementEnd(items: List[int], value: int) -> List[int]:
    # inserting at the beginning or any given location
    items.append(value)  # O(1) time complexity
    return items


def extendList(items: List[int], value: List[int]) -> List[int]:
    # inserting at the beginning or any given location
    items.extend(value)  # O(N) time and space complexity
    return items


print(updateList(exampleList, 1, 10))
# Time Complexity is O(1), space complexity is also O(1)

print(insertElementAnyWhere(exampleList, 2, -10))
print("####################")
print(insertElementEnd(exampleList, 100))
print("####################")
print(extendList(exampleList, [-6, -7, -9]))
