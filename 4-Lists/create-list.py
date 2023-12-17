# Lists is similar to array but the main difference is that a list can store different
# data types

from typing import List, Union


list1: List[Union[str, int, bool, float]] = ["egg", 1, True, 3.4]
list2: List[int] = [1, 2, 3, 4]
list3: List[str] = ["one", "two", "three"]
list4: List[List[Union[str, int, bool, float]] | Union[str, int, bool, float]] = [
    [1, 2, 3],
    1,
    True,
    ["one", "two"],
]

print(list4)
