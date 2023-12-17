from typing import List


def accessList(items: List[str], index: int) -> str:
    if len(items) == 0:
        return "list is empty"
    elif index >= len(items):
        return f"array doesn't have index {index}"
    elif index < -len(items):
        return f"array doesn't have index {index}"
    return items[index]


def traverseList(items: List, value: str) -> str:
    if len(items) == 0:
        return "list is empty"
    if value in items:
        return f"{value} was found in the list"
    return f"{value} not in the list"


print(accessList(["cheese", "milk", "tea"], 1))
print(accessList(["cheese", "milk", "tea"], -1))  # "tea"
print(accessList(["cheese", "milk", "tea"], -3))  # "tea"
print(accessList(["cheese", "milk", "tea"], 3))
print(traverseList(["cheese", "milk", "tea"], "milk"))
