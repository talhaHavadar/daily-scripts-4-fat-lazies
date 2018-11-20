def maxSubset(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 1
    elif len(arr) == 2:
        return max(arr)
    else:
        global_max = -99999
        arr[1] = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            max_values = [arr[i - 1], arr[i], arr[i] + arr[i - 2]]
            arr[i] = max(max_values)
            if arr[i] > global_max:
                global_max = arr[i]
        return global_max
        
 print([2,-1,3,5,1,2])
