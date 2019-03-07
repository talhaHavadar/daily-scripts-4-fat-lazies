"""
Given an integer list where each number represents the number of hops you can make,
determine whether you can reach to the last index starting at index 0.

eg.
[2, 0, 1, 0] => True
[1, 1, 0, 1] => False
[2, 3, 1, 0, 0] => True
"""

def __helper__(arr: list, curr_i: int, cache: dict):
    if curr_i == len(arr) - 1:
        return True
    val = arr[curr_i]
    result = False
    for t in range(1, val + 1, 1):
        if not (curr_i + t) in cache:
            result = __helper__(arr, curr_i + t, cache)
        if result:
            return True
        else:
            cache[curr_i + t] = False

    return False

def can_make_it(arr: list):
    cache = {}
    return __helper__(arr, 0, cache)



print(can_make_it([2, 0, 1, 0]))
print(can_make_it([1, 1, 0, 1]))
print(can_make_it([2, 3, 1, 0, 0]))
