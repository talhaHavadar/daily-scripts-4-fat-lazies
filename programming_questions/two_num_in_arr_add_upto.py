"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
def is_add_up(arr, k):
    # creates an array of zeros with size of k+1
    result = [False for x in range(k+1)]

    for i in range(len(arr)):
        remainder = k - arr[i]
        if arr[i] <= k and result[arr[i]]:
            return True
        elif remainder >= 0:
            result[remainder] = True
    
    return False

def is_add_up_hash(arr, k):
    result = dict()

    for num in arr:
        if num in result:
            return True
        else:
            result[k-num] = True
    return False

print(is_add_up([10,15,3,7], 17))
print(is_add_up_hash([10,25,3,-2, 19], 17))
