"""
Given a string and a set of characters, return the shortest substring containing all the characters in the set.
"""

string = "figehaeci"
s = set(["a", "e", "i"])

def shortest_substr(string: str, s: set):
    if not s:
        return ""
    elif not string:
        return None

    frequency_map = {}
    for x in s:
        frequency_map[x] = 0
    found_unique = 0
    set_len = len(s)
    string_len = len(string)
    start_index = 0
    end_index = -1
    for i in range(len(string)):
        char = string[i]
        if char in frequency_map:
            if found_unique == 0:
                start_index = i
            if frequency_map[char] == 0:
                # first time
                found_unique += 1
                frequency_map[char] += 1
            else:
                frequency_map[char] += 1
            end_index = i

    if found_unique != set_len:
        return None

    for i in range(start_index, len(string)):
        char = string[start_index]
        if char in frequency_map:
            if frequency_map[char] != 1:
                frequency_map[char] -= 1
                start_index += 1
            else:
                break
        else:
            start_index += 1
    return string[start_index:end_index + 1]

print(shortest_substr(string, s))
