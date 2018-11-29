"""
Given a list of integers, write a function that returns the largest sum of non-adjacent
elements of list.Numbers can be 0 or negative.

Ex.
[2,4,6,2,5] => 13
[5,1,1,5] => 10

Follow-up: Can you do this in O(N) time and constant space?

"""

def max_sum_adj(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr)
    else:
        first_max = max([arr[0], arr[1]])
        arr[1] = first_max
        for i in range(2, len(arr)):
            if arr[i] + arr[i-2] > arr[i]:
                arr[i] += arr[i-2]
            if arr[i - 1] > arr[i]:
                arr[i] = arr[i - 1]

    return arr[-1]

print(max_sum_adj([5,1,1,5]))
