"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
"""

def missing_min_integer(arr: list) -> int:
    max_int = max(arr)

    if max_int <= 0:
        return 1

    result = [0 for x in range(max_int + 1)]
    for i in range(len(arr)):
        if arr[i] > 0:
            result[arr[i]] = arr[i]

    for i in range(1, len(result)):
        if result[i] == 0:
            return i
    return max_int + 1

print(missing_min_integer([3, 4, -1, 1]))
print(missing_min_integer([0, 1, 2]))
