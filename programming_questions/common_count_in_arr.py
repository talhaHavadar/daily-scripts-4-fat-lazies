"""
Question: Given two sorted arrays, find the number of elements in common. The arrays are the same length
and each has all distinct elements.

A: 13 27 35 40 49 55 59
B: 17 35 39 40 55 58 60
"""

def get_common_count(arr1, arr2):
    arr1_index = 0
    arr2_index = 0
    common_count = 0
    while arr1_index < len(arr1) and arr2_index < len(arr2):
        arr1_num = arr1[arr1_index]
        arr2_num = arr2[arr2_index]

        if arr1_num < arr2_num:
            arr1_index += 1
        elif arr2_num < arr1_num:
            arr2_index += 1
        else:
            common_count += 1
            arr1_index += 1
            arr2_index += 1
    return common_count

print(get_common_count([13, 27, 35, 40, 49, 55, 59], [17, 35, 39, 40, 55, 58, 60]))
