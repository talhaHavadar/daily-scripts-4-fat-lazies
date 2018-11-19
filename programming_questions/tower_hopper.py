"""
Tower hopper problem
"""

def hopper(arr):
    if arr[0] > len(arr) - 1:
        return True
    elif arr[0] == 0:
        return False
    else:
        return hopper(arr[arr[0]:])

print(hopper([1,1,1]))
