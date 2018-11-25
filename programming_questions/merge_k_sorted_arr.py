"""
Given k sorted arrays, merge them into a single sorted array

eg.
merge({{1,4,7}, {2,5,8}, {3,6,9}})
{1,2,3,4,5,6,7,8,9}
"""

def merge(arrays: list):
    return _merger(arrays)

def _merger(arrays):
    if len(arrays) == 1:
        return arrays
    
    if len(arrays) == 2:
        array = merge_2_sorted(arrays[0], arrays[1])
        return [array]
    else:
        array1 = _merger(arrays[:int(len(arrays) / 2)])
        array2 = _merger(arrays[int(len(arrays) / 2):])
        return merge_2_sorted(array1[0], array2[0])
    
def merge_2_sorted(a: list, b: list):
    b_pointer, a_pointer = 0, 0
    result = []
    while a_pointer < len(a) and b_pointer < len(b):
        a_val = a[a_pointer]
        b_val = b[b_pointer]

        if a_val <= b_val:
            result.append(a_val)
            a_pointer += 1
        else:
            result.append(b_val)
            b_pointer += 1
    
    if a_pointer < len(a):  
        result += a[a_pointer:]
    if b_pointer < len(b):
        result += b[b_pointer:]

    return result


print(merge([[1,4,7], [2,5,8], [3,6,9]]))
