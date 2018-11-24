"""
Given 2 sorted arrays, A and B, where A is long enough to hold
the contents of A and B, write a function yo copy the contents of B
into A without using any buffer or additional memory.
"""

def merge(a: list, b: list):
    b_pointer, a_pointer, final_pointer = 0, 0, 0

    for i in range(len(a) - 1, -1, -1):
        if a[i] != 0:
            a_pointer = i
            break

    b_pointer = len(b) - 1
    final_pointer = len(a) - 1
    
    while final_pointer != a_pointer:
        b_val = b[b_pointer]
        a_val = a[a_pointer]

        if b_val >= a_val:
            a[final_pointer] = b_val
            b_pointer -= 1
        else:
            a[final_pointer], a[a_pointer] = a[a_pointer], a[final_pointer]
            a_pointer -= 1
        
        final_pointer -= 1

    return a

print(merge([1,3,5,0,0,0],[2,4,6]))
