"""
Find the permutations of a given string
"""
def permutation(string):
    if len(string) == 1:
        return [string]
    elif len(string) == 0:
        return []
    else:
        permutated = permutation(string[:-1])
        last_char = string[-1]
        permutations = []
        for s in permutated:
            for i in range(len(s)):
                string_before = s[:i]
                string_after = s[i:]
                permutations.append(string_before + last_char + string_after)
                if i == len(s) - 1:
                    permutations.append(s + last_char)
        return permutations

print(permutation("abcd"))
