from typing import List


exampleList: List[int] = [1, 2, 3, 4, 5, 6, 7, 5, 6]


def deleteByPop(items: List[int], index: int) -> List[int]:
    deletedItem: int = items.pop(index)
    return items


def deleteByRemove(items: List[int], value: int) -> List[int]:
    items.remove(value)
    return items


def deleteByDelete(items: List[int], index: int) -> List[int]:
    del items[index]
    return items


# print(deleteByPop(exampleList, 3))

# print(deleteByRemove(exampleList, 6))

print(deleteByDelete(exampleList, 1))
