"""
Given a string and dictionary, write a function 
to determine the minimum number of characters to delete to make
a word.

eg.
dictionary: { "a", "aa", "aaa" }
query = "abc"

output = 2
"""

def get_min_count_to_word(string: str, dictionary: dict) -> int:
    
    if string in dictionary:
        return 0

    start = 0
    size = 1

    while size < len(string):
        for i in range(start, len(string)):
            if i + size > len(string):
                break
            key = string[:i] + string[i + size:]
            if key in dictionary:
                return size

        size += 1 

    return size

d = { "a", "aa", "aaa" }
query = "cc"

print(get_min_count_to_word(query, d))
