def print_items(a, b: int) -> None:
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)


# for this  function the time complexity is O(A+B) because the values
# of A and B may not be the same , so the time it will take to compute
# the value of A will be different form B.


def print_items_mulitply(a, b: int) -> None:
    for i in range(a):
        for j in range(b):
            print(i, j)


# for this function the time complexity is O(A*B)
