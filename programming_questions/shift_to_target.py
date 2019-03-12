"""
Given two strings A and B, return whether or not A can be shifted some number of times to get B.

Example;
    if A is 'abcde' and B is 'cdeab' return true
"""

def is_possible(source: str, target: str) -> bool:
    if not source and not target:
        return True
    if not source or not target:
        return False
    if len(source) != len(target):
        return False

    char = source[0]
    shifted_index = -1
    # search the first char of source in target
    for i in range(len(target)):
        if target[i] == char:
            shifted_index = i

    if shifted_index == -1:
        return False

    for i in range(len(source)):
        index = (shifted_index + i) % len(target)
        if source[i] != target[index]:
            return False

    return True


print(is_possible("abcde", "cdeab"))
print(is_possible("abc", "acb"))
