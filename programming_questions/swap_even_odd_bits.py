"""
Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped,
the 3rd and 4th bit should be swapped and so on.

Example;
10101010 should be 01010101
11100010 should be 11010001

Can you do this in 1 line?

"""
a = 0b11100010

val = ((a & 0b01010101) << 1) ^ ((a & 0b10101010) >> 1)
print(bin(val))
