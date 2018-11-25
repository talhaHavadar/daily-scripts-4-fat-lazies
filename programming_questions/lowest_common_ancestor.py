"""
Given two nodes in binary tree, write a function to find the lowest
common ancestor.

eg.
        1
       /  \
      2     3
     / \   / \
    4   5 6   7

    lcs(4,3) = 1
    lcs(6,7) = 3
"""

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def lcs(root: Node, key1: int, key2: int) -> int:
    return _lcs_helper(root, key1, key2)

def _lcs_helper(node: Node, key1, key2):

    if node is None:
        return -2, 0

    val1, height1 = _lcs_helper(node.left, key1, key2)
    val2, height2 = _lcs_helper(node.right, key1, key2)

    if val1 == -1 and val2 == -1:
        return node.value, max([height1, height2]) + 1
    elif val1 == -1 or val2 == -1:
        return -1, max([height1, height2]) + 1
    elif val1 != -2 and val2 != -2:
        min_height = min([height1, height2])
        if min_height == height1:
            return val1, height1
        else:
            return val2, height2
    elif val1 != -2 or val2 != -2:
        if val1 != -2:
            return val1, height1
        else:
            return val2, height2
    else:
        if node.value == key1 or node.value == key2:
            return -1, max([height1, height2]) + 1
        else:
            return -2, max([height1, height2]) + 1

root = Node(1)
root.left = Node(2, Node(4), Node(5))
root.right = Node(3, Node(6), Node(7))

print(lcs(root, 6, 7))
