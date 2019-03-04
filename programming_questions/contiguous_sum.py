"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.
"""

inp = [1,2,3,4,5]
K = 9

def contiguous_sum(arr: list, k: int):
    start_index = 0
    end_index = -1
    current_sum = 0
    for i in range(len(arr)):
        if current_sum < k:
            current_sum += arr[i]
        if current_sum > k:
            current_sum -= arr[start_index]
            start_index += 1
        elif current_sum == k:
            end_index = i
            break
    if end_index != -1:
        return arr[start_index:end_index]
    else:
        return []

print(contiguous_sum(inp, K))
