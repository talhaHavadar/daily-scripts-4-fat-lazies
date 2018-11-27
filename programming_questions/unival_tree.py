"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))


# implement a graph solution 
cache = {}


def unival_count(node, cache):
    if node in cache:
        return cache[node]
    if node is None:
        return (0, True)

    unival_left_count, unival_left = unival_count(node.left, cache)
    unival_right_count, unival_right = unival_count(node.right, cache)

    if not node.left is None:
        cache[node.left] = unival_left_count
    if not node.right is None:
        cache[node.right] = unival_right_count

    if unival_left and unival_right:
        if node.left and node.right and (node.value == node.right.value and node.value == node.left.value):
            cache[node] = unival_left_count + unival_right_count + 1
            return (unival_left_count + unival_right_count + 1, True)
        elif node.left is None and node.right is None:
            return (1, True)
        else:
            cache[node] = unival_left_count + unival_right_count
            return (unival_left_count + unival_right_count, False)
    else:
        cache[node] = unival_left_count + unival_right_count
        return (unival_left_count + unival_right_count, False)

print(unival_count(root, cache))
